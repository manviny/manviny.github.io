
## Enlaces de interés a Jetson nano

- [Intro](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro)
- [Community Projects](https://developer.nvidia.com/embedded/community/jetson-projects)
- [Hello AI](https://github.com/dusty-nv/jetson-inference/blob/master/docs/jetpack-setup-2.md)
- [Pose](https://github.com/NVIDIA-AI-IOT/trt_pose)
- [Setup NVIDIA Jetson with Ultralytics YOLOv8](https://www.youtube.com/watch?v=mUybgOlSxxA)
- [Setup a Jetson Nano 2GB for computer vision with Roboflow](https://www.youtube.com/watch?v=sVyFHFUxAz0)
- [Jetson nano 3D cases for printing](https://www.yeggi.com/q/jetson+nano+case/)
- [![Hello world course](https://img.youtube.com/vi/PLsjK_a5MFguIUJJ1GPt1I2eN6cihKg2kG/0.jpg)](https://www.youtube.com/watch?v=PLsjK_a5MFguIUJJ1GPt1I2eN6cihKg2kG)
- [Hello World](https://www.youtube.com/watch?v=Gzb4MyjrjMw&list=PLsjK_a5MFguIUJJ1GPt1I2eN6cihKg2kG&index=2)

## Preparar software para visión en Jetson Nano
### Instalar Pytorch en Jetson Nano

### Descargar e instalar el OS
https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write-mac


### Ultralitycs + GPU
```bash
## necesitamos python >= 3.8
python3 --version
python -m venv yolo
source yolo/bin/activate
pip install ultralytics
deactivate


## Instalar Python 3.10  compatible con wheels, versiones maypores puede3n no fucnionar
sudo apt update && sudo apt upgrade -y && \
sudo apt install -y build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev uuid-dev wget && \
wget https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz && \
tar -xf Python-3.10.10.tgz && \
cd Python-3.10.10 && \
./configure --enable-optimizations && \
make -j$(nproc) && \
sudo make altinstall && \
cd .. && \
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.10 1 && \
sudo update-alternatives --config python3

# pythorch
sudo apt install -y python3-pip libopenblas-dev libopenmpi-dev git cmake build-essential && \
python3.10 -m pip install --upgrade pip && \
git clone --recursive https://github.com/pytorch/pytorch.git && \
cd pytorch && \
git checkout v1.9.0 && \
python3.10 -m pip install -r requirements.txt && \
python3.10 setup.py bdist_wheel && \
pip3 install dist/*.whl


```
- [![Ultralitycs + GPU ](https://img.youtube.com/vi/pAEkHsNkul0/0.jpg)](
https://www.youtube.com/watch?v=pAEkHsNkul0)


- [![Pytorch](https://img.youtube.com/vi/ZXbOV83EXdQ/0.jpg)](
https://www.youtube.com/watch?v=ZXbOV83EXdQ)


### Planificador de viajes
- [![Ultralitycs + GPU ](https://img.youtube.com/vi/F-KHlSPNdSg/0.jpg)](
https://www.youtube.com/watch?v=F-KHlSPNdSg)


### Object tracking
[![Object tracking](https://img.youtube.com/vi/joAZEUbZZy8/0.jpg)](https://www.youtube.com/watch?v=joAZEUbZZy8)