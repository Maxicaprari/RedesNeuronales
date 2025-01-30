# -*- coding: utf-8 -*-
"""arquitectura_autoencoder_no _lineal 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ebM0vyQT1Ij9CCQKdmTCZWZRvLjye2I8
"""

class Autoencoder_Conv(nn.Module):
    def __init__(self, n=28 * 28, p=0.2):
        super().__init__()
        self.n = n
        self.p = p
        # ENCODER
        self.encoder = nn.Sequential(
            # CONV1
            nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1),  # Output: (16, 28, 28)
            nn.ReLU(),
            nn.Dropout(self.p),
            nn.MaxPool2d(kernel_size=2, stride=2),  # Output: (16, 14, 14)
            # CONV2
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),  # Output: (32, 14, 14)
            nn.ReLU(),
            nn.Dropout(self.p),
            nn.MaxPool2d(kernel_size=2, stride=2),  # Output: (32, 7, 7)
        )
        # DECODER
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(
                in_channels=32, out_channels=16, kernel_size=3, stride=2, padding=1, output_padding=1
            ),  # Output: (16, 14, 14)
            nn.ReLU(),
            nn.Dropout(self.p),
            nn.ConvTranspose2d(
                in_channels=16, out_channels=1, kernel_size=3, stride=2, padding=1, output_padding=1
            ),  # Output: (1, 28, 28)
            nn.Sigmoid(),  # Escala la salida entre [0, 1]
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x