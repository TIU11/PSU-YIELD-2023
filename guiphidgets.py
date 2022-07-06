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
    
    # Print on GUI 
    message.value = showTemp
    # Print for Debugging in console comment later
    print(" Temperature: " + showTemp )

def convertTemp():
    convertTemp = (temperatureSensor.getTemperature() * 1.8) + 32 
    showTemp = str(convertTemp) + " °F"
    message.value = showTemp

# When button is pressed get temperature    
btn.when_pressed = getTemp
message = Text(app)
button = PushButton(app, text="Get Temperature", command=getTemp)
button2 = PushButton(app, text="Convert Temperature to Fahrenheit", command=convertTemp)

app.display()