#!/usr/bin/python
"""
  ARDrone3 demo with autonomous navigation to two color Parrot Cap
  usage:
       ./demo.py <task> [<metalog> [<F>]]
"""
import sys
import cv2
import time
import math
import datetime

from bebop import Bebop
from commands import movePCMDCmd
from capdet import detectTwoColors, loadColors

# this will be in new separate repository as common library fo robotika Python-powered robots
from apyros.metalog import MetaLog, disableAsserts
from apyros.manual import myKbhit, ManualControlException


if __name__ == "__main__":
    dPsi = math.pi # 0 rad
    # print "drone.trim()"
    # print "drone.takeoff()"
    # print "drone.flyToAltitude( 1.5 )"
    drone = Bebop()
    drone.trim()
    # drone.videoDisable()
    drone.takeoff()
    time.sleep(3)
    print "Take Off Successfull"
    
    # drone.hover()
    # print("Flying To Altitude Of " + str(2))
    # drone.flyToAltitude(2, timeout=20, speed=100) 
    # time.sleep(5)


    # # print "Battery:", drone.battery
    drone.takePicture()
    print "Picture Taken."
    print "Rotating by " + str(dPsi)
    drone.moveBy( 0, 0, 0, dPsi)
    print "Waiting " + str(5) +" seconds"
    time.sleep(5)
    print "Finished first rotation"    

    drone.takePicture()
    print "Picture Taken."
    print "Rotating by " + str(dPsi)
    drone.moveBy( 0, 0, 0, dPsi)
    print "Waiting " + str(5) +" seconds"
    time.sleep(5)
    print "Finished second rotation"
    # #Bebop_Drone_2018-04-25T201835+0000_.jpg
    # # for i in xrange(200):
    # #     print i,

    # drone.hover()
    # print"Flying To Altitude Of 1.5"
    # drone.flyToAltitude(1.5, timeout=20, speed=50) 
    # time.sleep(5)
    
    # drone.hover()
    # print "drone.land()"
    drone.land()
    print "Landing."
    #time.sleep(10)
    print "Python Executed"

# vim: expandtab sw=4 ts=4 

