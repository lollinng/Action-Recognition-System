<h1>Action-Recognition-System</h1> 
contains different MediaPipe sub projects which I intend to merge together in near future to create a proper action detection system. This action detection system can be used in various use cases for different client requirements with some tweaks in code. <br>
<h5>This Directory currently contain 3 projects</h5>


<h2> 1. Sign_language Detection</h2> Uses <strong>lstm</strong> and <strong>ann</strong> to create a sequential model to detect the action/word that the user is trying to convey using sign_language. The lstm is trained on the dataset of different coordinates of various nodes and keypoints provided by the mediapipe .
<br>
<h4>Project Video<h4>

https://user-images.githubusercontent.com/55660103/183247537-feb565b6-29e9-43cd-aa89-3cede1abeca7.mp4

<br>
<h2> 2. BicepCurl </h2> Used to count the number of reps in realtime of bicup curl (a gym exercise) . 
<br>
<h4>Project Video<h4>

https://user-images.githubusercontent.com/55660103/183285881-66b1c980-fd08-46d2-b5e5-8de0ee1b453a.mp4

<br>
<h2> 3. PoseNet </h2> 
A module created to get the landmarks mark them on human body using mediapipe. It's used in bicep curl as module
<br>

