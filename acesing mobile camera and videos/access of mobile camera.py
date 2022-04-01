import cv2

camera = "http://192.168.137.43:8080/video"
#connect your laptop and android device with same network either wifi or hotspot
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)# here 0 is the path of any video
cap.open(camera)
print("check==",cap.isOpened())
#fourcc is a 4 byte code which is use to specify the video code
fourcc = cv2.VideoWriter_fourcc(*"XVID")#*"mp4" is a video format
#it contain 4 parameter , name , codec,fps,resolution (fourcc is four byte code)
output = cv2.VideoWriter("D:\\hero.mp4",fourcc,20.0,(640,40),0)# create output.avi file with the help of fourcc


# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    frame= cv2.resize(frame,(700,700))
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    output.write(frame)

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



