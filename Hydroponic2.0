# All the outputs we are using. - Scott Benson
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
powerPlug.setHubPort(3)

#Open
powerPlug.openWaitForAttachment(5000)
lcd.openWaitForAttachment(1000)
phSensor.openWaitForAttachment(1000)
temp.openWaitForAttachment(1000)

#this controls the brightness of the LCD screen.
#Makes it easier to see in the dark! - Scott Benson
lcd.setBacklight(0.25)

powerPlug.setState(1)

while (True):
    lcd.writeText(LCDFont.FONT_6x12, 0, 15, "PH Level: " + str(phSensor.getPH()) + " PH")
    #ptint("PH Level: " + str(phSensor.getPH()))
    time.sleep(0.25)
    lcd.writeText(LCDFont.FONT_6x12, 0, 35, "Temp: " + str(temp.getTemperature()))
    #ptint("Temp: " + str(VoltageInput.TemperatureSensor()))
    time.sleep(0.25)
    lcd.flush()
