# Autoencoder y Clasificador Convolucional para Fashion-MNIST  

Este repositorio contiene la implementación y análisis de un **Autoencoder Convolucional** y un **Clasificador Convolucional** aplicados al dataset **Fashion-MNIST**. El objetivo del proyecto es estudiar cómo distintas configuraciones del espacio latente afectan la reconstrucción de imágenes y evaluar el desempeño de **encoders pre-entrenados** reutilizados en tareas de clasificación.  

## 📐 Arquitecturas  

### 1. Autoencoder Convolucional  
- **Encoder**: Red convolucional con varias capas de convolución y *max-pooling* para reducir progresivamente la dimensión de las imágenes y capturar representaciones latentes.  
- **Latent Space**: Configurable, lo que permite controlar el nivel de compresión.  
- **Decoder**: Red convolucional transpuesta para reconstruir las imágenes a partir del espacio latente.  

### 2. Clasificador Convolucional  
- **Entrenado desde cero**: Red convolucional estándar entrenada directamente para la tarea de clasificación.  
- **Con encoder pre-entrenado**: Se reutiliza el encoder del autoencoder para inicializar el clasificador, comparando diferentes estrategias de entrenamiento:  
  - **Transfer learning**: Congelando los pesos del encoder pre-entrenado.  
  - **Fine-tuning**: Ajustando los pesos del encoder, aunque esto llevó a sobreajuste.  

---

## 📁 Estructura del Repositorio  

### 1. Carpetas principales  
- **Resultados/**: Contiene gráficos, matrices de confusión y archivos de resultados del entrenamiento y validación.  

### 2. Archivos de código 📝  

- `2capas_no_lineal_bn32.py`: Red feedforward con dos capas ocultas, activaciones ReLU y tamaño de lote de 30.  
- `loops_clasificador.py`: Código para los loops de entrenamiento y validación del clasificador.  
- `matriz_de_confusión.py`: Genera y visualiza la matriz de confusión para evaluar el desempeño del clasificador.  
- `clasificador_para_autoencoder_1capa_nolineal.py`: Clasificador que utiliza representaciones generadas por un autoencoder de una capa no lineal.  
- `clasificador_sin_preentrenar_1.py` y `código_completo_clasificador_sin_preentrenar.py`: Clasificador desarrollado sin preentrenamiento con autoencoders.  

### 3. Arquitecturas de Autoencoders 🔄  

- `arquitectura_1_autoencoder.py`: Autoencoder básico de una sola capa.  
- `arquitectura_2_autoencoder(3_capas).py`: Autoencoder más profundo con tres capas ocultas.  
- `arquitectura_3_autoencoder(1capa).py` y `arquitectura_3_autoencoder(1capa,_no_lineal).py`: Autoencoders de una capa con activaciones no lineales para mejor representación de las características.  
- `arquitectura_autoencoder_no__lineal_1.py`: Versión alternativa del autoencoder no lineal.  

---

## 📊 Resultados  

### Clasificador con Encoder pre-entrenado  
- Ofrece una mejor representación inicial, acelerando la convergencia en las primeras épocas.  
- Para alcanzar el mejor desempeño, fue necesario ajustar el modelo para la tarea específica de clasificación.  

### Clasificador entrenado desde cero  
- Requiere más tiempo de entrenamiento, pero logra mejores resultados cuando se optimiza correctamente.  

> **Nota**: Los **autoencoders no lineales** no tienen capas lineales intermedias, lo que mejora la representación de las características complejas.  

---

## ⚙️ Requisitos  

- Python 3.x  
- PyTorch  
- Numpy  
- Matplotlib  

---

## 📚 Referencias  

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. Capítulo 9, "Convolutional Networks".  
2. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly Media.  
3. LeCun, Y., Bengio, Y., & Hinton, G. (2015). *Deep Learning*. *Nature*, 521(7553), 436-444.  
4. Stanford University. *CS231n: Convolutional Neural Networks for Visual Recognition*. Disponible en: [http://cs231n.stanford.edu/](http://cs231n.stanford.edu/)  
5. Chollet, F. (2017). *Deep Learning with Python*. Manning Publications.  

