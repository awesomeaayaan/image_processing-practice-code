#break video into multiple images and store in a folder
import cv2

vidcap = cv2.VideoCapture("D:\hello.mp4")
ret,image = vidcap.read()#read the video
count = 0
while True:
    if ret == True:
        image = cv2.resize(image,(600,500))
        cv2.imwrite("D:\\frames\\imgN%d.jpg"%count,image)#it will saves the images in D drive
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        cv2.imshow("res",image)
        
        count +=1
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()
    
vidcap.release()
cv2.destroyAllWindows()

