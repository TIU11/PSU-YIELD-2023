
#Add Phidgets library
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
#Required for sleep statement
import time
import csv

#Create
temperatureSensor = TemperatureSensor()

#Open
temperatureSensor.openWaitForAttachment(1000)

#Record data points
count = 0

# Create a new log file 
with open ('phidgets_temperature.csv','w') as datafile:
    writer = csv.writer(datafile)
    # Column Headers for CSV File
    writer.writerow(['Time', 'Temp', 'Light'])
    def read_data():
        now = time().strftime('%I:%M:%S %p') # 2:05:01 PM
        temp = temperatureSensor.getTemperature()
        light = lightSensor.getLuminance()
        return [now, temp, light]
    #Use your Phidgets
    
    while (True):
        #Update user
        print("Logging data...")
       #Write data to file in CSV format 
        writer.write_row(read_data())
        datafile.flush()
        print("row was written")
        #Increment count
        count += 1
        
        #If 10 data points have been recorded, close file and exit program
        if(count == 10):
            print("Logging complete, exiting program")
            exit()
        
        time.sleep(10)
  
