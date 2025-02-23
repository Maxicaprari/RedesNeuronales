# -*- coding: utf-8 -*-
"""arquitectura_2_autoencoder(3 capas).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11cgE_GrvtHFH6YO25LqjUaU3ENztN7r8
"""

class Autoencoder_Conv(nn.Module):
    def __init__(self, n=28 * 28, p=0.2):
        super().__init__()
        self.n = n
        self.p = p
        # ENCODER
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),  # (16, 28, 28)
            nn.ReLU(),
            nn.Dropout(self.p),
            nn.MaxPool2d(2, 2),  # (16, 14, 14)

            # CONV2
            nn.Conv2d(16, 32, kernel_size=3, padding=1),  # (32, 14, 14)
            nn.ReLU(),
            nn.Dropout(self.p),
            nn.MaxPool2d(2, 2),  # (32, 7, 7)
            # CONV3
            nn.Conv2d(32, 64, kernel_size=3, padding=1),  # (64, 7, 7)
            nn.ReLU(),
            nn.Dropout(self.p),

            # Aquí reducimos con MaxPool2d(2,2), pero usamos output_size=4
            nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True),  # (64, 4, 4)
            # LINEAR
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, self.n),
            nn.ReLU(),
            nn.Dropout(self.p),
            )
        # DECODER
        self.decoder = nn.Sequential(
            nn.Linear(self.n, 64 * 4 * 4),
            nn.ReLU(),
            nn.Dropout(self.p),
            nn.Unflatten(dim=1, unflattened_size=(64, 4, 4)),  # (64, 4, 4)
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding = 0),  # (32, 7, 7)
            nn.ReLU(),
            nn.Dropout(self.p),
            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2, padding=1, output_padding=1),  # (16, 14, 14)
            nn.ReLU(),
            nn.Dropout(self.p),
            nn.ConvTranspose2d(16, 1, kernel_size=3, stride=2, padding=1, output_padding = 1),  # (1, 28, 28)
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
