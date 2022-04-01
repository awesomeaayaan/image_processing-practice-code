import cv2
"""
 #below code is used to read a video from a device
cap = cv2.VideoCapture(r"C:\Users\Hp\Desktop\testvideo.mp4")
print("cap",cap)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(700,450))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#convert color video to gray 
    cv2.imshow("frame", frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(25)#if wait key value is less i.e let 5 then the video play will be fast and if more then the video paly back would be slow
    if k == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()#deallocate the space in the memory
"""
'''
#capture the video from webcam and save into memory
cap = cv2.VideoCapture(0)
print(cap)
while cap.isOpened():
    ret, frame = cap.read()#ret is a boolean value whether the comming image is true or not
    if ret == True:
        frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#convert color video to gray 
        cv2.imshow("frame", frame)
        cv2.imshow("gray",gray)
        if cv2.waitKey(1) & 0xFF == ord('q'): #press to exit
            break
    
cap.release()
cv2.destroyAllWindows()
'''
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)

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

