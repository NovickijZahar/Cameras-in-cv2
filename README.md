# Cameras-in-cv2
Изначельно нужно установить модули opencv-python, pyautogui и numpy
```python
pip install opencv_python
```
```python
pip install pyautogui
```
```python
pip install numpy
```
## cameras.py
Программа, позволяющая подключить несколько камер через ip или провода, просматривать вывод с этих камер и затем посмотреть полученные записи.
___
Камеры можно добавить двумя способами:
1. Указав ее номер(нулевой номер указывает на встроенную веб-камеру ноутбука)
2. Указав ее ip
```python
cam1 = cv2.VideoCapture(0) #создание объекта камеры
cam2 = cv2.VideoCapture('https://192.168.0.104:8080/video')

cams.append(cam1) # добавление камеры в список
cams.append(cam2)
```
___
Здесь при необходимости можно изменить название файлов, куда производится запись(если не указывать полный путь, то файлы записи будут сохраняться в директорию, где находится исходный файл)
```python
for index, item in enumerate(cams):
    size = int(item.get(3)), int(item.get(4))
    results.append(cv2.VideoWriter(f'camera{index+1}.avi', #тут указывается название файла, куда производится запись
                                  cv2.VideoWriter_fourcc(*'MJPG'), 10, size))
```
___
Остановка процессов записи происходит по нажатию клавиши 'q'
```python
if cv2.waitKey(1) & 0xFF == ord('q'): # остановка работы всех камер при нажатии клавиши q
        break
```

## screencapture.py
Программа позводяющая производить захват экрана, а затем просматривать получившуюся запись
___
Здесь можно изменить название сохраняемого файла(аналогично cameras.py)
```python
result = cv2.VideoWriter('screencapture.avi', cv2.VideoWriter_fourcc(*'MJPG'), 13, pyautogui.size())
```
___
Остановка процессов записи происходит по нажатию клавиши 'q'
```python
if cv2.waitKey(1) & 0xFF == ord('q'): # остановка работы всех камер при нажатии клавиши q
        break
```
