Steps for using the code:
First of all, you need to download the complete haarcascades folder from the official opencv github
Link: https://github.com/opencv/opencv/tree/4.x/data/haarcascades

What are haarcascades?
haarcascades - the folder contains trained classifiers for detecting objects
               of a particular type, e.g. faces (frontal, profile), pedestrians etc.
               Some of the classifiers have a special license - please,
               look into the files for details.

Now, in the line 4 of the face_detection_webcam.py 
faceCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

Modify the path of the haarcascade folder according to your stored location, you'll need to navigate to the 
haarcascade_frontalface_default.xml classifier and provide it's local path in the CascadeClassifier Function.

Boom! Now your code is ready to run.
