import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support
from model import SpatialISLTransformer

def train_and_evaluate():
    # 0. Create reports directory
    os.makedirs("reports", exist_ok=True)

    # 1. Load Data
    X = np.load("X.npy")
    y = np.load("y.npy")
    classes = np.load("classes.npy", allow_pickle=True)
    num_classes = len(classes)
    print(f"Training on {len(X)} samples across {num_classes} classes.")

    # Convert to PyTorch Tensors
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.long)

    # 2. Split into Train (80%) and Validation (20%)
    dataset = TensorDataset(X_tensor, y_tensor)
    val_size = int(0.2 * len(dataset))
    train_size = len(dataset) - val_size
    train_dataset, val_dataset = random_split(dataset,[train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

    # 3. Initialize Model, Loss, and Optimizer
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SpatialISLTransformer(num_classes=num_classes).to(device)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Tracking metrics for plotting
    history = {'train_loss': [], 'val_loss': [], 'train_acc': [], 'val_acc':[]}

    # 4. Training Loop
    epochs = 30
    for epoch in range(epochs):
        model.train()
        train_loss = 0
        correct_train = 0
        total_train = 0
        
        for batch_X, batch_y in train_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total_train += batch_y.size(0)
            correct_train += (predicted == batch_y).sum().item()
            
        train_acc = 100 * correct_train / total_train
            
        # Validation during training
        model.eval()
        val_loss = 0
        correct_val = 0
        total_val = 0
        with torch.no_grad():
            for batch_X, batch_y in val_loader:
                batch_X, batch_y = batch_X.to(device), batch_y.to(device)
                outputs = model(batch_X)
                loss = criterion(outputs, batch_y)
                val_loss += loss.item()
                
                _, predicted = torch.max(outputs.data, 1)
                total_val += batch_y.size(0)
                correct_val += (predicted == batch_y).sum().item()
                
        val_acc = 100 * correct_val / total_val
        
        # Save history
        history['train_loss'].append(train_loss/len(train_loader))
        history['val_loss'].append(val_loss/len(val_loader))
        history['train_acc'].append(train_acc)
        history['val_acc'].append(val_acc)
        
        print(f"Epoch {epoch+1:02d}/{epochs} | "
              f"Train Loss: {history['train_loss'][-1]:.4f} | Train Acc: {train_acc:.2f}% | "
              f"Val Loss: {history['val_loss'][-1]:.4f} | Val Acc: {val_acc:.2f}%")

    # 5. Save the Model
    torch.save(model.state_dict(), "isl_model.pth")
    print("\nTraining complete! Model saved as 'isl_model.pth'")

    # ==========================================
    # 6. EVALUATION AND REPORT GENERATION
    # ==========================================
    print("\nGenerating Evaluation Reports...")
    model.eval()
    all_preds = []
    all_targets =[]

    with torch.no_grad():
        for batch_X, batch_y in val_loader:
            batch_X = batch_X.to(device)
            outputs = model(batch_X)
            _, predicted = torch.max(outputs.data, 1)
            all_preds.extend(predicted.cpu().numpy())
            all_targets.extend(batch_y.numpy())

    # --- A. Generate Classification Report (Precision, Recall, F1) ---
    report_dict = classification_report(all_targets, all_preds, target_names=classes, output_dict=True)
    report_text = classification_report(all_targets, all_preds, target_names=classes)
    
    # --- B. Generate Confusion Matrix & Extract TP, FP, FN, TN ---
    cm = confusion_matrix(all_targets, all_preds)
    
    with open("reports/evaluation_metrics.txt", "w") as f:
        f.write("========================================\n")
        f.write("      FINAL YEAR PROJECT ML REPORT      \n")
        f.write("========================================\n\n")
        
        f.write(f"Overall Model Accuracy: {accuracy_score(all_targets, all_preds) * 100:.2f}%\n\n")
        
        f.write("1. DETAILED CLASSIFICATION REPORT:\n")
        f.write("(Precision, Recall, F1-Score per class)\n")
        f.write("-" * 40 + "\n")
        f.write(report_text + "\n\n")
        
        f.write("2. CLASS-WISE TRUE/FALSE POSITIVES:\n")
        f.write("-" * 40 + "\n")
        for i, class_name in enumerate(classes):
            tp = cm[i, i]
            fp = cm[:, i].sum() - tp
            fn = cm[i, :].sum() - tp
            tn = cm.sum() - (tp + fp + fn)
            f.write(f"Class '{class_name}':\n")
            f.write(f"   True Positives (TP) : {tp}\n")
            f.write(f"   False Positives (FP): {fp}\n")
            f.write(f"   True Negatives (TN) : {tn}\n")
            f.write(f"   False Negatives (FN): {fn}\n\n")
            
    print("Saved text metrics to 'reports/evaluation_metrics.txt'")

    # --- C. Plot and Save Confusion Matrix ---
    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
    plt.title('Confusion Matrix', fontsize=16)
    plt.ylabel('Actual Label', fontsize=12)
    plt.xlabel('Predicted Label', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("reports/confusion_matrix.png", dpi=300)
    plt.close()
    print("Saved Confusion Matrix plot to 'reports/confusion_matrix.png'")

    # --- D. Plot and Save Training Curves ---
    plt.figure(figsize=(14, 5))
    
    # Loss Curve
    plt.subplot(1, 2, 1)
    plt.plot(history['train_loss'], label='Training Loss', color='blue', marker='o')
    plt.plot(history['val_loss'], label='Validation Loss', color='red', marker='x')
    plt.title('Model Loss over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    # Accuracy Curve
    plt.subplot(1, 2, 2)
    plt.plot(history['train_acc'], label='Training Accuracy', color='blue', marker='o')
    plt.plot(history['val_acc'], label='Validation Accuracy', color='green', marker='x')
    plt.title('Model Accuracy over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("reports/training_curves.png", dpi=300)
    plt.close()
    print("Saved Training Curves plot to 'reports/training_curves.png'")
    print("\nAll reports generated successfully! Check the 'reports/' folder.")

if __name__ == "__main__":
    train_and_evaluate()