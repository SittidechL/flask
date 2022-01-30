#https://dsdi.msu.ac.th/?article=programming&fn=micropython
#https://www.youtube.com/watch?v=ApOwrmX0TB0
from machine import Pin
import time

p = Pin(5, Pin.OUT)


def toggle(max):
    lap = 0
    
    while(lap < max):
        p.value(1)
        time.slee(1)
        p.value(0)
        time.sleep(1)
        lap +=1
toggle(5)
