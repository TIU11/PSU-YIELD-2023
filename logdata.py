
#Add Phidgets library
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.PHSensor import *
#Required for sleep statement
import time
import csv

#Create
temperatureSensor = TemperatureSensor()
phSensor = PHSensor()
#Open
temperatureSensor.openWaitForAttachment(1000)
phSensor.openWaitForAttachment(1000)
#Record data points
count = 0

#Use your Phidgets
while (True):
    # Update user
    print("Logging data...")

    # Write data to file in CSV format
    with open ('phidgets_temperature.csv','a') as datafile:
        writer = csv.writer(datafile)

        # This is how it writes headers to my file
        writer.writerow('Temperature','pH')
        for count in range(20):
            writer.writerow([str(temperatureSensor.getTemperature()),str(phSensor.getPH())])
            count += 1
        # datafile.write(str(temperatureSensor.getTemperature()) + "\n")
            time.sleep(10)
            print("Logging" + count)

            #exit()
    #Increment count
    #count += 1
    #If 10 data points have been recorded, close file and exit program
    #if(count == 10):
