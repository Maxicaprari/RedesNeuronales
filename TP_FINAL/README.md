# Computational Neuroscience and Deep Learning Projects 🧠💻  
Este repositorio contiene una colección de trabajos prácticos desarrollados en el marco de proyectos relacionados con modelos neuronales y aprendizaje profundo (Deep Learning). Cada sección incluye el código, las arquitecturas utilizadas, los loops de entrenamiento y validación, así como los resultados obtenidos y sus respectivos informes.

## Contenido 📂  

### Trabajo 1: Modelo de Hodgkin y Huxley  
- Implementación del modelo clásico para el análisis del potencial de acción en neuronas.  
- Resolución numérica mediante el método de Runge-Kutta de cuarto orden (RK4).  
- Análisis de respuesta neuronal ante diferentes estímulos de corriente y evolución de los canales iónicos.  

### Trabajo 2: Clasificación con Redes Neuronales Feedforward (MLP)  
- Implementación de una red neuronal feedforward para la clasificación de imágenes del dataset Fashion-MNIST.  
- Diseño de una arquitectura con dos capas ocultas y función de activación ReLU.  
- Entrenamiento y evaluación utilizando diferentes hiperparámetros: learning rate, tamaño de lote, y optimizadores como Adam y SGD.  
- Análisis de la pérdida y precisión en el conjunto de validación para comparar el rendimiento de la red.  

### Trabajo Final: Autoencoder y Clasificador Convolucional para Fashion-MNIST  
Este trabajo incluye la implementación y análisis de un **Autoencoder Convolucional** y un **Clasificador Convolucional** aplicados al dataset Fashion-MNIST. El objetivo es estudiar cómo distintas configuraciones del espacio latente afectan la reconstrucción de imágenes y evaluar el desempeño de encoders preentrenados reutilizados en tareas de clasificación.  

#### Arquitecturas 🔄  

##### Autoencoder Convolucional  
- **Encoder:** Red convolucional con varias capas de convolución y *max-pooling* para reducir progresivamente la dimensión de las imágenes y capturar representaciones latentes.  
- **Latent Space:** Configurable, lo que permite controlar el nivel de compresión.  
- **Decoder:** Red convolucional transpuesta para reconstruir las imágenes a partir del espacio latente. *Nota: Los autoencoders no lineales no tienen una capa lineal intermedia, lo que les permite capturar relaciones más complejas entre las variables de entrada.*  

##### Clasificador Convolucional  
- **Entrenado desde cero:** Red convolucional estándar entrenada directamente para la tarea de clasificación.  
- **Con encoder pre-entrenado:** Se reutiliza el encoder del autoencoder para inicializar el clasificador. Se realizan comparaciones entre diferentes estrategias de entrenamiento (congelando o ajustando los pesos), utilizando **transfer learning** y evitando **fine-tuning** debido al riesgo de sobreajuste.  

#### Estructura del Proyecto 🛠️  
##### Carpetas principales  
- `Resultados/`: Contiene gráficos, matrices de confusión y archivos de resultados del entrenamiento y validación.  
- `Informes/`: Incluye el PDF del trabajo final con los detalles del proyecto.  

##### Archivos de código 📝  
- `2capas_no_lineal_bn32.py`: Implementación de una red feedforward con dos capas ocultas y activaciones no lineales (ReLU), tamaño de lote de 30.  
- `loops_clasificador.py`: Código con los loops de entrenamiento y validación para el clasificador.  
- `matriz_de_confusión.py`: Genera y visualiza la matriz de confusión para evaluar el desempeño del clasificador.  
- `clasificador_para_autoencoder_1capa_nolineal.py`: Clasificador que utiliza representaciones generadas por un autoencoder de una capa no lineal.  
- `clasificador_sin_preentrenar_1.py` y `código_completo_clasificador_sin_preentrenar.py`: Clasificador desarrollado sin preentrenamiento con autoencoders.  

##### Arquitecturas de Autoencoders 🔄  
- `arquitectura_1_autoencoder.py`: Autoencoder básico de una sola capa.  
- `arquitectura_2_autoencoder(3_capas).py`: Autoencoder más profundo con tres capas ocultas.  
- `arquitectura_3_autoencoder(1capa).py` y `arquitectura_3_autoencoder(1capa,_no_lineal).py`: Autoencoders de una capa con activaciones no lineales para mejor representación de las características.  
- `arquitectura_autoencoder_no_lineal_1.py`: Versión alternativa del autoencoder no lineal.  

#### Resultados 📊  
- **Clasificador con encoder pre-entrenado:** Ofrece una mejor representación inicial, acelerando la convergencia en las primeras épocas. Sin embargo, para alcanzar el mejor desempeño, fue necesario ajustar el modelo para la tarea específica de clasificación.  
- **Entrenado desde cero:** Aunque requiere más tiempo de entrenamiento, logró mejores resultados cuando se optimizó correctamente.  

#### Requisitos 🖥️  
- Python 3.x  
- PyTorch  
- Numpy  
- Matplotlib  

#### Bibliografía 📚  
1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. Capítulo 9, "Convolutional Networks".  
2. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly Media.  
3. LeCun, Y., Bengio, Y., & Hinton, G. (2015). *Deep Learning*. *Nature*, 521(7553), 436-444.  
4. Stanford University. *CS231n: Convolutional Neural Networks for Visual Recognition*. Disponible en: [CS231n](http://cs231n.stanford.edu/).  
5. Chollet, F. (2017). *Deep Learning with Python*. Manning Publications.  
