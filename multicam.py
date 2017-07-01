#!/usr/bin/python

# Developed from
# http://www.arducam.com/multi-camera-adapter-module-raspberry-pi/
# Rongzhong Li
# Jun. 30, 2017

import RPi.GPIO as gp
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

pins=[7,11,12]
enable=[[0,0,1],[1,0,1],[0,1,0],[1,1,0]]

def main():
    frame=0
    try:
        while 1:
            for cam in range(4):
                for p in range(3):
                    gp.output(pins[p], enable[cam][p])
                capture(frame,cam)
            frame+=1
    except KeyboardInterrupt:
        pass
    finally:
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
            

def capture(frame,cam):
    cmd = "raspistill -o capture_%d_%d.jpg" % (frame,cam)
    print (cmd)
    os.system(cmd)

if __name__ == "__main__":
    main()



