from tkinter import *
import time
import vgamepad as vg
from scipy.interpolate import interp1d

gamepad = vg.VX360Gamepad()
print('----- Joystick initialised-----')
stick_down_values = interp1d([0,50,100], [-32768,0,32767])
stick_middle_values = interp1d([-50,0,50], [-32768,0,32767])
trigger_values = interp1d([0,25,100],[0,64,255])

def type1value_map(ch_value):
    return(int(stick_down_values(ch_value)))

def type2value_map(ch_value):
    return(int(stick_middle_values(ch_value)))

def type3value_map(ch_value):
    return(int(trigger_values(int(ch_value))))

def send_values(values):
    roll = type2value_map(int(values[0]))
    pitch = type2value_map(int(values[1]))
    throttle = type1value_map(int(values[2]))
    yaw = type2value_map(int(values[3]))

    gimbal = type3value_map(int(values[5]))

    gamepad.left_joystick(x_value=yaw, y_value=throttle)
    gamepad.right_joystick(x_value=roll, y_value=pitch)
    gamepad.left_trigger(value=gimbal) 
    gamepad.update()
    return([roll,pitch,throttle,yaw,gimbal])

# from PIL import Imagetk,Image
# ---------------------------------------------
root=Tk()
root.geometry("200x530")
root.title('Virtual Joystic Test 01')

def sliderValue(var):
    ch1Value = str(ch1.get())# ROLL
    ch2Value = str(ch2.get())# PITCH
    ch3Value = str(ch3.get())# THROTTLE
    ch4Value = str(ch4.get())# YAW
    ch5Value = str(ch5.get())#
    ch6Value = str(ch6.get())# GIMBAL
    ch7Value = str(ch7.get())#
    ch8Value = str(ch8.get())#
    allValues = [ch1Value, ch2Value, ch3Value, ch4Value, ch5Value, ch6Value, ch7Value, ch8Value]
    sent = send_values(allValues)
    totalVal = ch1Value+" "+ch2Value+" "+ch3Value+" "+ch4Value+" "+ch5Value+" "+ch6Value+" "+ch7Value+" "+ch8Value
    print(totalVal)
    print('Sent to Mission Planner', sent)





# --------------------------------------------------------
Label(root,text="CH1").pack()
ch1=Scale(root,from_=-50,to=50,orient=HORIZONTAL,command=sliderValue)
ch1.pack()
Label(root,text="CH2").pack()
ch2=Scale(root,from_=-50,to=50,orient=HORIZONTAL,command=sliderValue)
ch2.pack()
Label(root,text="CH3").pack()
ch3=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=sliderValue)
ch3.pack()
Label(root,text="CH4").pack()
ch4=Scale(root,from_=-50,to=50,orient=HORIZONTAL,command=sliderValue)
ch4.pack()
Label(root,text="CH5").pack()
ch5=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=sliderValue)
ch5.pack()
Label(root,text="CH6").pack()
ch6=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=sliderValue)
ch6.pack()
Label(root,text="CH7").pack()
ch7=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=sliderValue)
ch7.pack()
Label(root,text="CH8").pack()
ch8=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=sliderValue)
ch8.pack()

# -----------------------------------------------------------------

root.mainloop()
# ----------------------------------------------------------------------
