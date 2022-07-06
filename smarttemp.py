 #Add Phidgets Library 
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
#Required for sleep statement
import time 

#Create 
temperatureSensor = TemperatureSensor()

#Open 
temperatureSensor.openWaitForAttachment(1000)

#Use your Phidgets 
while(True):
    print(" Temperature: " + str(temperatureSensor.getTemperature()) + " °C" )
    time.sleep(0.15)
  
