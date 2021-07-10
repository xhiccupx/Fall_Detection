# video-fall-detection
it takes the video input either from the web cam (live) or pre recorded video and detects the fall and the send an alert notification to the mentioned contacts for help

# How it works
Each frame read from the video will be converted into grey and then the background is removed based on the motion detected. 
Then we draw the contours if the height of the contour is lower than the width, it will be a fall and the count is increased by one,
if the count is greater than 22, will be drawing a rectangle around the fallen person.
after the fall is detected an alert is sent to the mentioned contacts using IFTTT web hooks and sms service.
