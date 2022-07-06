 #Add Phidgets Library 
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.LCD import *

#Required for sleep statement
import time 

#Create 
temperatureSensor = TemperatureSensor()
lcd = LCD()

#Open 
temperatureSensor.openWaitForAttachment(1000)
lcd.openWaitForAttachment(1000)

#Set Temperature Variable
showTemp = str(temperatureSensor.getTemperature()) + " °C"

def getTemp():
    lcd.writeText(LCDFont.FONT_6x12, 0, 0, showTemp)
    # Print for Debugging in console comment later
    print(" Temperature: " + str(temperatureSensor.getTemperature()) + " °C" )
    lcd.flush()


#Use your Phidgets 
while(True):
    getTemp()
    time.sleep(1)
    autoFlush = lcd.getAutoFlush()

  
