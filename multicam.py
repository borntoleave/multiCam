#!/usr/bin/python

# Developed from
# http://www.arducam.com/multi-camera-adapter-module-raspberry-pi/
# Rongzhong Li
# Jun. 30, 2017

import RPi.GPIO as gp
import os


import numpy as np
import cv2
from  picamera import PiCamera
from picamera.array import PiRGBArray
import time 
import sys
from matplotlib import pyplot as plt

gp.setwarnings(False)
gp.setmode(gp.BOARD)

pins=[7,15,16]
for p in range(3):
    gp.setup(pins[p], gp.OUT)
    
enable=[[0,0,1],[1,0,1],[0,1,0],[1,1,0]]
flip=[1,1],[0,0],[1,1],[0,0]#[w,h]

W=640#camW/3
H=480#camH/3		#rpi camera will round up the resolution to certain intervals. 
resolution=(W,H)



camera=PiCamera()
camera.resolution=resolution

time.sleep(0.1)
			
output=np.zeros(H*W*3,dtype=np.uint8)
print output
def main():
    f=0
    try:
        while 1:
            for c in range(4):
                for p in range(3):
                    gp.output(pins[p], enable[c][p])
                print ("frame: %d, camera: %d")%(f,c)
                camera.hflip=flip[c][0]
		camera.vflip=flip[c][1]
                camera.capture(output,'bgr' )#,use_video_port=True)
                frame=output.reshape(H,W,3)
                print frame.shape
                plt.subplot(2,2,c)
                plt.imshow(frame)
                #cv2.imshow('img',frame)
                #cv2.imwrite("capture_%d_%d.jpg" % (f,c),frame)
                #if  cv2.waitKey(1) & 0xFF==ord('q'):
                #    cv2.destroyAllWindows()
                #    break
                #camera.start_preview()
                #camera.stop_preview()
                plt.draw()
            f+=1
    except KeyboardInterrupt:
        time.sleep(2)
    finally:
        print ("cleaning")
        for p in range(3):
            gp.output(pins[p], False)
            

def capture(frame,c):
    camera.capture(output,'rgb' ,use_video_port=True)
    #camera.capture(rawCapture,'rgb' )#,use_video_port=True)

    return output
    #cmd = "raspistill -o capture_%d_%d.jpg" % (frame,c)
    #print (cmd)
    #os.system(cmd)

if __name__ == "__main__":
    main()



