# version2.pyx

import math

def great_circle(float lon1,float lat1,float lon2,float lat2):
    cdef float radius=3956.0
    cdef float pi=3.14159265
    cdef float x=pi/180.0
    cdef float a,b,theta,c

    a=(90.0-lat1)*(x)
    b=(90.0-lat2)*(x)
    theta=(lon2-lon1)*(x)
    c=math.acos((math.cos(a)*math.cos(b) +
            math.sin(a)*math.sin(b)*math.cos(theta)))
    return c*radius  