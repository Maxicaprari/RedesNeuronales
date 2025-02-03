La variación de hiperparametros al modelo de dos capas no lineal del autoencoder, va en el siguiente orden:

* Optimizador SGD
* Optimizador ADAM, p=0.2 (Parametro del Dropout)
* ADAM, con batch_size 256, y variando la learning rate a -4, manteniendo p=0.2
* Misma variación de learning rate, pero con parametro p=0.4
