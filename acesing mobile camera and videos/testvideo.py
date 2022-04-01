import cv2

camera = "http://192.168.137.43:8080/"
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
#capture the video from webcam and save it into the memory
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#DIVX, XVID,MJPG,X264,WMV1,WMV2(these are the format to save the video in location)
#fourcc is a 4 byte code which is use to specify the video code
fourcc = cv2.VideoWriter_fourcc(*"XVID")#*"XVID" is a video format
#it contain 4 parameter , name , codec,fps,resolution (fourcc is four byte code)
output = cv2.VideoWriter("D:\\output.avi",fourcc,20.0,(640,40),0)# create output.avi file with the help of fourcc


# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,0)

    # Display the resulting frame
    cv2.imshow('Frame',frame)
    cv2.imshow('gray',gray)
    output.write(gray)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()
output.release()
# Closes all the frames
cv2.destroyAllWindows()


