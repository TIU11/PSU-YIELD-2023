#Add Phidgets Library 
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.LCD import *
from Phidget22.Devices.PHSensor import *
from Phidget22.Devices.TemperatureSensor import *
import time

#Create
lcd = LCD()
powerPlug = DigitalOutput()
phSensor = PHSensor()
temp = TemperatureSensor()

#Address
powerPlug.setIsHubPortDevice(True)
powerPlug.setHubPort(3) #This number indicates the port that is being used on the VINT Hub for the Power Plug.

#Open
powerPlug.openWaitForAttachment(5000)
lcd.openWaitForAttachment(1000)
phSensor.openWaitForAttachment(1000)
temp.openWaitForAttachment(1000)

#Use your Phidgets

lcd.setBacklight(0.25) #This controls the brightness of the LCD screen.

#The PowerPlug controls the pump.
while (True):
    powerPlug.setState(1) #Turns pump on
    time.sleep(3*60) # Stays on for this many seconds
    powerPlug.setState(0) #Turns pump off
    time.sleep(3*60) #Stays off for this many seconds

# The following loop displays the pH and temperature readings on the LCD screen.
while (True):
    lcd.writeText(LCDFont.FONT_6x12, 0, 15, "pH Level: " + str(phSensor.getPH()) + " pH")
    #ptint("PH Level: " + str(phSensor.getPH()))
    time.sleep(0.25)
    lcd.writeText(LCDFont.FONT_6x12, 0, 35, "Temp: " + str(temp.getTemperature()))
    #ptint("Temp: " + str(VoltageInput.TemperatureSensor()))
    time.sleep(0.25)
    lcd.flush()
