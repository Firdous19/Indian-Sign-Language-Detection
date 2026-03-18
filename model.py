import torch
import torch.nn as nn
import math

class SpatialISLTransformer(nn.Module):
    def __init__(self, num_classes, input_dim=3, seq_length=42, d_model=64, nhead=4, num_layers=2, dim_feedforward=128, dropout=0.3):
        super(SpatialISLTransformer, self).__init__()
        
        # Project the 3 coordinates (x,y,z) into a higher dimensional space
        self.input_proj = nn.Linear(input_dim, d_model)
        
        # Positional Encoding to tell the Transformer which joint is which
        self.positional_encoding = nn.Parameter(torch.randn(1, seq_length, d_model))
        
        encoder_layers = nn.TransformerEncoderLayer(
            d_model=d_model, 
            nhead=nhead, 
            dim_feedforward=dim_feedforward, 
            dropout=dropout,
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layers, num_layers=num_layers)
        
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(d_model, num_classes)

    def forward(self, x):
        # x shape: (batch_size, 42, 3)
        x = self.input_proj(x) # Shape: (batch_size, 42, d_model)
        x = x + self.positional_encoding # Add positional info
        
        # Pass through Transformer
        x = self.transformer_encoder(x)
        
        # Global Average Pooling over the 42 landmarks
        x = x.mean(dim=1) 
        
        x = self.dropout(x)
        out = self.fc(x)
        return out