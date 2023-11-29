import cv2

cams = []

#эту часть кода можно изменить, если нужно добавить камеры
#########################################################################################
cam1 = cv2.VideoCapture(0) #создание объекта камеры

cams.append(cam1) # добавление камеры в список
#########################################################################################


results = [] # список потоков записи
#заполнение списка
for index, item in enumerate(cams):
    size = int(item.get(3)), int(item.get(4))
    results.append(cv2.VideoWriter(f'camera{index+1}.avi', #тут указывается название файла, куда производится запись
                                  cv2.VideoWriter_fourcc(*'MJPG'), 10, size))


while True:
    rets = []
    frames = []
    rets, frames = zip(*(cam.read() for cam in cams))

    if not all(rets):
        print("Камера недоступна")
        break


    for index, item in enumerate(results):
        item.write(frames[index])

    for index, item in enumerate(frames):
        cv2.imshow(f'Camera{index+1}', cv2.resize(item, (640, 480)))

    if cv2.waitKey(1) & 0xFF == ord('q'): # остановка работы всех камер при нажатии клавиши q
        break


for cam in cams: #прекращаем вывод изображения
    cam.release()

for result in results: #прекращаем запись
    result.release()

cv2.destroyAllWindows() #закрытие окна