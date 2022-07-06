 #Add Phidgets Library 
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from gpiozero import Button
from guizero import App, Text, PushButton
#Required for sleep statement
import time 

#Create 
temperatureSensor = TemperatureSensor()
btn = Button(2)
app = App(title="Dashboard")

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

button = PushButton(app, text="Get Temperature", command=getTemp)

app.display()