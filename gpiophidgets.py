 #Add Phidgets Library 
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.LCD import *
from gpiozero import Button
#Required for sleep statement
import time 

#Create 
temperatureSensor = TemperatureSensor()
btn = Button(2)
#Open 
temperatureSensor.openWaitForAttachment(1000)

# Get Temperature Function
def getTemp():
    #Set Temperature Variable
    showTemp = str(temperatureSensor.getTemperature()) + " °C"
    # Print for Debugging in console comment later
    print(" Temperature: " + showTemp )

# When button is pressed get temperature    
btn.when_pressed = getTemp
