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

#Use your Phidgets 
while(True):
    lcd.writeText(LCDFont.FONT_6x12, 0, 0, showTemp)
    print(" Temperature: " + str(temperatureSensor.getTemperature()) + " °C" )
    time.sleep(1)
    lcd.flush()

  
