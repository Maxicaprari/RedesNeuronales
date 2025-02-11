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

# Estructura del Código

**train_loop:** Contiene el bucle de entrenamiento para el autoencoder y el clasificador, incluyendo validación y registro de métricas.

**test_loop:** Evalúa el rendimiento del modelo entrenado en el conjunto de prueba y calcula las métricas finales.
autoencoder.py: Implementación del Autoencoder Convolucional, con parámetros configurables para el tamaño del espacio latente.

**classifier:** Implementación del Clasificador Convolucional, compatible con encoders pre-entrenados.

# Resultados

**Clasificador**
Encoder pre-entrenado: Ofrece una mejor representación inicial, acelerando la convergencia en las primeras épocas. Sin embargo, para alcanzar el mejor desempeño, fue necesario ajustar el modelo para la tarea específica de clasificación.

Entrenado desde cero: Aunque requiere más tiempo de entrenamiento, logró mejores resultados cuando se optimizó correctamente.

# Requisitos

Python 3.x

PyTorch

Numpy

Matplotlib
