# Lane detection
### Level 2 VSP lv 2 Assignment, challenge #9 
#### by Sean Sminia and Ray Mindiola.
 
 
###  Introduction
The task description, was to, from any given video to detect the lines of the lane a car is driving. . This was done using CV2 and python. 

### Method

To complete this task, the following steps have been taken in our software. 

1) First: we define a region of interest. This is to reduce the noise in the image and to avoid line dectitions outside the area we are interested in 

2) Second: then apply canny edge detection to reduce the noise within the image, as shown in the following screenshot

![Cannyedge](https://i.imgur.com/Dqwp8NR.png)

3) Third: Afterwards, using the results of the canny edge detection, then a Hough Line Transform function is applied within the limits of the region of interested. Tuning the values such that we reduce the amount of horizontal lines detected. The results are then drawn over the original video. The resulting image is shown while running the program.

![result](https://i.imgur.com/PVctC1Y.png)

### Results
As previously mentioned, the resulting video is outputted into the mp4 file "outpy.mp4". You can check the whole video in the file available in the repository.

![result](result.gif)

### Conclusion
The task was successfully completed, however, the performance of the program we have deviced can be further improved. It is possible to apply thresholding after the region masking so then the canny edge dectection would give better results. Perhaps it would be possible to further improve the area of interest by fine tuning the polygon shape used to mask what is not needed in the frame of the video.
 
