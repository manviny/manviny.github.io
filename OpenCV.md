
##### Envorinment
- source yolo_env/bin/[activate|deactivate]
- conda activate anylabeling_env

## Pasos para el entrenamiento y predición de imágenes
- Cargar zip en formato yolo en ./label-studio
- Descomprimir zip en carpetas ./mydata   (borra las carpetas anteriores)
  - ```python organizar_etiquetado.py ```
- Crear el yaml para los ficheros cargados (zip) del paso anterior
  - ```python crear_yaml.py ```
- Entrenar el modelo
  - ```python train.py ```
- Predicciones del modelo
  - ```python predict.py ```
- Funciones auxiliares
  - ```python split_in_640_chunks.py ```        # trocea imagen en partes de 640
  - ```python script.py ```                     # detecta objetos en imagen
  - ```python webcam.py ```        # detecta objetos por camara


## Índice
- [Entorno](#entorno)
- [Pasos para el Entrenamiento y Predicción](#pasos-para-el-entrenamiento-y-predicci%C3%B3n-de-im%C3%A1genes)
- [YOLOv8](#yolo8)
- [Label Studio](#label-studio)
- [Dependencias](#dependencias)
- [Uso](#uso)
- [Dividir Imágenes en Fragmentos](#dividir-una-imagen-en-chunck)
- [Entrenamiento](#entrenar)
- [Predicción](#predecir)
- [Datasets](#datasets)
- [AutoLabel Recursos Web](#autolable-recursos-web)
- [Docker en AWS](#docker-on-aws)
- [NGROQ](#ngroq)

## Proyectos
- [OpenCV](OpenCV/Basket_Ball_Shot_Predictor_Recording/)




## Yolo8
### Train Yolov8 object detection on a custom dataset

[![Integrating Ultralytics YOLOv8 with Label Studio](https://img.youtube.com/vi/etjkjZoG2F0/0.jpg)](https://www.youtube.com/watch?v=etjkjZoG2F0)

[![Integrating Ultralytics YOLOv8 with Label Studio](https://img.youtube.com/vi/m9fH9OWn8YM/0.jpg)](https://www.youtube.com/watch?v=m9fH9OWn8YM)


### Learn Computer Vision in 30 Days
[![Integrating Ultralytics YOLOv8 with Label Studio](https://img.youtube.com/vi/HiTw5KFw7ic/0.jpg)](https://www.youtube.com/watch?v=HiTw5KFw7ic)

### 20 vision projects
- copiar proyectos a GitHub public y enlazar con aules
[![Integrating Ultralytics YOLOv8 with Label Studio](https://img.youtube.com/vi/jkevWUGOP4w/0.jpg)](https://www.youtube.com/watch?v=jkevWUGOP4w)




### Label Studio
label-studio

#### 1. colocar el zip en la carpeta label_studio y ejecutar:
- python organizar_etiquetado.py


### ENVIRONMENT
- python -m venv yolo_env
- source yolo_env/bin/activate
- conda info --envs
- conda activate ---

### DEPENDENCIES
- pip install ultralytics===8.3.27
- pip install six  

### USE

#### detectar imagen
- yolo predict model=yolo11n.pt source='./imagen_1.jpg'
- [python -m ultralytics yolo predict model=yolo11n.pt source='./imagen_1.jpg']

#### ver imagen detectada

### Dividir una imagen en chunck
- divide la imagen en trozos de 640x640 apropiado para train de yolo11
- de esta forma los tamaños del test escaneado y entrenado se parecen
python split.py

### Entrenar
- entrena lo indicado en "./mydata/data.yaml"
python train.py 
- la salida se encuentra como best.pt en:
runs/detect/train12

### Predecir
- predice cuadrados en la imagen con el ultimo  modelo entrenado en /runs/trainX/weights/best.pt
  python predict.py 

## Datasets
- [RoboFlow datasets](https://universe.roboflow.com/search?q=class%3Ayolo)
- [Coches kaggle](https://www.kaggle.com/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo)
- [Señales tráfico](https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-dataset-in-yolo-format)
- [Coches vista aerea](https://www.kaggle.com/code/braunge/yolov8-training-on-custom-dataset)
- [Cartas pocker](https://universe.roboflow.com/ec-ioptime-esa8g/card_detect_200)

## AutoLable Recursos Web
### [YOLO ML backend GitHub](https://github.com/HumanSignal/label-studio-ml-backend/blob/master/label_studio_ml/examples/yolo/README.md)

### Integrating Ultralytics YOLOv8 with Label Studio NGROQ
[![Integrating Ultralytics YOLOv8 with Label Studio](https://img.youtube.com/vi/UyaecID1iG8/0.jpg)](https://www.youtube.com/watch?v=UyaecID1iG8)

[![Título del video](https://img.youtube.com/vi/GgehjwFmVSw/0.jpg)](https://www.youtube.com/watch?v=GgehjwFmVSw)

[![Título del video](https://img.youtube.com/vi/R1ozTMrujOE/0.jpg)](https://www.youtube.com/watch?v=R1ozTMrujOE)
[![Título del video](https://img.youtube.com/vi/A1V8yYlGEkI/0.jpg)](https://www.youtube.com/watch?v=A1V8yYlGEkI)
[![Título del video](https://img.youtube.com/vi/UUP_omOSKuc/0.jpg)](https://www.youtube.com/watch?v=UUP_omOSKuc)


[![Título del video](https://img.youtube.com/vi/ZOxeNHzIbfg/0.jpg)](https://www.youtube.com/watch?v=ZOxeNHzIbfg)
[![Título del video](https://img.youtube.com/vi/K727xhe6VmA/0.jpg)](https://www.youtube.com/watch?v=K727xhe6VmA)


## Docker on AWS

[![Título del video](https://img.youtube.com/vi/1_AlV-FFxM8/0.jpg)](https://www.youtube.com/watch?v=1_AlV-FFxM8)

## NGROQ
[![Título del video](https://img.youtube.com/vi/NqCYquO3byk/0.jpg)](https://www.youtube.com/watch?v=NqCYquO3byk)
[![Título del video](https://img.youtube.com/vi/frvY3Ywxs-I/0.jpg)](https://www.youtube.com/watch?v=frvY3Ywxs-I)
[![Título del video](https://img.youtube.com/vi/p2NrmWpK8qM/0.jpg)](https://www.youtube.com/watch?v=p2NrmWpK8qM)



