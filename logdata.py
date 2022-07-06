
#Add Phidgets library
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
#Required for sleep statement
import time

#Create
temperatureSensor = TemperatureSensor()

#Open
temperatureSensor.openWaitForAttachment(1000)

#Record data points
count = 0

#Use your Phidgets
while (True):
    #Update user
    print("Logging data...")
    
    #Write data to file in CSV format
    with open ('phidgets_temperature.csv','a') as datafile:
        datafile.write(str(temperatureSensor.getTemperature()) + "\n")
    
    #Increment count
    count += 1
    
    #If 10 data points have been recorded, close file and exit program
    if(count == 10):
        print("Logging complete, exiting program")
        exit()
    
    time.sleep(0.5)
  