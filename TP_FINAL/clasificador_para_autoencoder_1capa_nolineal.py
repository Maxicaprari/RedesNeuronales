# -*- coding: utf-8 -*-
"""Cladificador_para_autoenc_1capa_nolineal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17PawOBRfzjj-9Gk4_mvUzzvyvEXUO_bK
"""

import torch
import torch.nn as nn
import copy

class Clasificador_Conv(nn.Module):
    def __init__(self, autoencoder_conv=None, copy_encoder=True, n1=128, n2=256, p=0.2):
        super().__init__()

        self.n1 = n1
        self.n2 = n2
        self.p = p

        if autoencoder_conv is None:
            print("Creating encoder...")
            self.encoder = nn.Sequential(
                nn.Conv2d(1, 16, kernel_size=3, padding=1),
                nn.ReLU(),
                nn.Dropout(self.p),
                nn.MaxPool2d(2, 2),

                nn.Conv2d(16, 32, kernel_size=3, padding=1),
                nn.ReLU(),
                nn.Dropout(self.p),
                nn.MaxPool2d(2, 2),

                nn.Flatten()  # Aplanar salida antes de la capa lineal
            )
        else:
            print("Copying encoder from pretrained autoencoder...")
            if copy_encoder:
                self.encoder = nn.Sequential(
                    copy.deepcopy(autoencoder_conv.encoder),
                    nn.Flatten()  #  Aplanar salida antes de la capa lineal
                )
            else:
                self.encoder = nn.Sequential(
                    autoencoder_conv.encoder,
                    nn.Flatten()
                )

        # CLASIFICADOR con 3 capas densas
        self.clasificador = nn.Sequential(
            nn.Linear(3136, self.n1),  #  Tamaño corregido
            nn.ReLU(),
            nn.Dropout(self.p),

            nn.Linear(self.n1, self.n2),
            nn.ReLU(),
            nn.Dropout(self.p),

            nn.Linear(self.n2, 10)  # Salida de 10 clases
        )

    def forward(self, x):
        x = self.encoder(x)
        #print("Forma después del encoder:", x.shape)  #  Depuración
        x = self.clasificador(x)
        return x