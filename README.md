## Let's Talk: American Sign Language (ASL) Recognition 
### This project allows to recognize and translate ASL gestures in real-time using  web-camera. 
![alt text](https://github.com/aabdysheva/Lets_Talk/blob/main/alsu.gif)
### Libraries we used
- [OpenCV](https://opencv.org/)
to work with pictures and web-camera. While our programm works it recieves video stream using OpenCV. 
- [MediaPipe](https://google.github.io/mediapipe/solutions/holistic)
to extract and save landmark coordinates of hand's position. 
![alt text](https://google.github.io/mediapipe/images/mobile/holistic_sports_and_gestures_example.gif)
- [Keras](https://github.com/keras-team/keras)
to build and train LSTM model. 
### Dataset
Dataset includes more than 5000 video samples, each sample includes 30 frames (video).
39 classes:
- 26 alphabet letters
- 10 words
- 3 special signs (model_start, model_stop, NaN)
### Model
- 3 LSTM layers with ReLU activation and a fully-connected output layer with softmax activation.
- Categorical accuracy on validation set was greater than 95%.
### How to run Let's talk
- clone repository
- install all libraries in requirements.txt
- run "main_ui.py"
### GitHub-accounts of groupmates
This project was completed in 10 days by:<br>
https://github.com/plazinho <br>
https://github.com/IlyaGaluzinskiy <br>
https://github.com/aabdysheva
