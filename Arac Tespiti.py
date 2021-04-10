import cv2
cars="cars.xml"
video='araç.mp4'
cam=cv2.VideoCapture(video)
cars_detector=cv2.CascadeClassifier(cars)

while True:
    ret, frame=cam.read()

    if (type(frame)==type(None)):
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    car=cars_detector.detectMultiScale(gray,1.1,1)
    for x,y,w,h in car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Arac Tespit",frame)
    if cv2.waitKey(33)==27:
        break
cv2.destroyAllWindows()
