#to acces youtube video directly

import cv2
import pafy

url = "https://www.youtube.com/watch?v=zJQI0irlfQs"
data = pafy.new(url)#pafy will fetch the data from the given url
data = data.getbest(preftype="mp4")

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)# here 0 is the path of any video
cap.open(data.url)
print("check==",cap.isOpened())


# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    frame= cv2.resize(frame,(700,700))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    cv2.imshow("gray",gray)
    

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
