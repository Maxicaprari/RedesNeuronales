# Autoencoder y Clasificador Convolucional para Fashion-MNIST

Este repositorio contiene la implementación y análisis de un Autoencoder Convolucional y un Clasificador Convolucional aplicados al dataset Fashion-MNIST. El objetivo del proyecto es estudiar cómo distintas configuraciones del espacio latente afectan la reconstrucción de imágenes y evaluar el desempeño de encoders pre-entrenados reutilizados en tareas de clasificación.

# Arquitecturas
**1. Autoencoder Convolucional**

Encoder: Red convolucional con varias capas de convolución y \textit{max-pooling} para reducir progresivamente la dimensión de las imágenes y capturar representaciones latentes.

Latent Space: Configurable, lo que permite controlar el nivel de compresión.

Decoder: Red convolucional transpuesta para reconstruir las imágenes a partir del espacio latente.

**2. Clasificador Convolucional**

Entrenado desde cero: Red convolucional estándar entrenada directamente para la tarea de clasificación.

Con encoder pre-entrenado: Se reutiliza el encoder del autoencoder para inicializar el clasificador y se comparan los resultados entre diferentes estrategias de entrenamiento (congelando o ajustando los pesos).

# 1. Carpetas principales
**Resultados/**: Contiene gráficos, matrices de confusión y archivos de resultados del entrenamiento y validación.
# 2. Archivos de código 📝

A continuación, se describen los archivos de código clave:

**2capas_no_lineal_bn32.py**: Implementación de una red feedforward con dos capas ocultas y activaciones no lineales (ReLU), tamaño de lote de 30.

**loops_clasificador.py**: Código con los loops de entrenamiento y validación para el clasificador.

matriz_de_confusión.py: Genera y visualiza la matriz de confusión para evaluar el desempeño del clasificador.

**clasificador_para_autoencoder_1capa_nolineal.py**: Clasificador que utiliza representaciones generadas por un autoencoder de una capa no lineal.

**clasificador_sin_preentrenar_1.py y código_completo_clasificador_sin_preentrenar.py**: Clasificador desarrollado sin preentrenamiento con autoencoders.

# 3. Arquitecturas de Autoencoders 🔄
**arquitectura_1_autoencoder.py**: Autoencoder básico de una sola capa.

**arquitectura_2_autoencoder(3_capas).py**: Autoencoder más profundo con tres capas ocultas.

**arquitectura_3_autoencoder(1capa).py y arquitectura_3_autoencoder(1capa,_no_lineal).py:** Autoencoders de una capa con activaciones no lineales para mejor representación de las características.

**arquitectura_autoencoder_no__lineal_1.py:** Versión alternativa del autoencoder no lineal.

# Resultados

**Clasificador**
**Encoder pre-entrenado**: Ofrece una mejor representación inicial, acelerando la convergencia en las primeras épocas. Sin embargo, para alcanzar el mejor desempeño, fue necesario ajustar el modelo para la tarea específica de clasificación.

**Entrenado desde cero**: Aunque requiere más tiempo de entrenamiento, logró mejores resultados cuando se optimizó correctamente.

# Requisitos

Python 3.x

PyTorch

Numpy

Matplotlib
