#-*- coding:utf-8 -*-
'''
Author: Lance Zhang
Date: 2018
Description: read in a video file, create a display window,and draw user defined text on the window
File: 
'''
import numpy as np
#from dateutil.parser import parse
import cv2
import time,datetime

if __name__ == "__main__":
    # check the configuration every time
    videoname = '2018-7-18-18-52-55_Maker.avi'
    videodataname = '2018-7-18-18-52-55.txt'
    txtname = 'data.txt'
    video_start_time = '2018-7-18 18:52:55'
    #video_start_time = time.mktime(time.strptime(video_start_time, '%Y-%m-%d %H:%M:%S'))
    #print(video_start_time)
    video_start_time = 1531911140
    print(video_start_time)

    # load in the video file
    videoCapture=cv2.VideoCapture(videoname)
    sucess,frame=videoCapture.read() # get a frame
    # load in the data file
    videotime = np.loadtxt(videodataname,str)[:,1] # string format
    #print(videotime[1])
    data = np.loadtxt(txtname,str)

    # state variable
    xpos = data[:,0]
    ypos = data[:,1]
    theta = data[:,2]
    current = data[:,3]
    voltage = data[:,4]
    # control variable
    PWM1 = data[:,5]
    PWM2 = data[:,6]
    rudder = data[:,7]
    sail = data[:,8] 
    datatime = data[:,9]

    # get frames in a loop and do process 
    i = 1600 # index of recorded data
    frame_count = 0 
    time0 = time.time()
    frame_start = time0

    while(sucess):
        if float(datatime[i])-video_start_time < frame_start-time0: # recorded data time < video playing time
            # let the data go to next, while frame stays
            i += 1
            
            displayImg=cv2.resize(frame,(1024,768))
            cv2.putText(displayImg,"X: "+xpos[i],(850,50),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Y: "+ypos[i],(850,100),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Theta: "+theta[i],(850,150),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Current: "+current[i],(850,200),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Voltage: "+voltage[i],(850,250),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"PWM1: "+PWM1[i],(850,300),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"PWM2: "+PWM2[i],(850,350),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Rudder: "+rudder[i],(850,400),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Sail: "+sail[i],(850,450),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Time: "+str(float(datatime[i])-video_start_time),(850,500),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)

            cv2.namedWindow('test Video')    
            cv2.imshow("test Video",displayImg)
            keycode=cv2.waitKey(1)
        elif float(datatime[i])-video_start_time >= frame_start-time0: # recorded data time > video playing time
            # let the video frame go to next, while data stays
            frame_start = time.time()
            sucess,frame=videoCapture.read()
            displayImg=cv2.resize(frame,(1024,768)) #resize it to (1024,768)
            frame_count += 1
            #print(frame_count)
            #print(float(datatime[i+1]))
            #print(frame_start-time0)

            cv2.putText(displayImg,"X: "+xpos[i],(850,50),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Y: "+ypos[i],(850,100),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Theta: "+theta[i],(850,150),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Current: "+current[i],(850,200),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Voltage: "+voltage[i],(850,250),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"PWM1: "+PWM1[i],(850,300),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"PWM2: "+PWM2[i],(850,350),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Rudder: "+rudder[i],(850,400),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Sail: "+sail[i],(850,450),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)
            cv2.putText(displayImg,"Time: "+str(float(datatime[i])-video_start_time),(850,500),cv2.FONT_HERSHEY_PLAIN,1.0,(0,0,255),2)

            cv2.namedWindow('test Video')    
            cv2.imshow("test Video",displayImg)

            keycode=cv2.waitKey(1) # trigger interruption
            # pause

            if keycode==27:
                cv2.destroyWindow('test Video')
                videoCapture.release()
                break

            while time.time()-frame_start < 0.1:
                pass
            # ensure the video to be 15 sec
            # ensure 10 frames per sec, or read the time stamp from video
    print('Total frame: ',str(frame_count))
