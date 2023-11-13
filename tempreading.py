# Read and print the temperature at the probe

from time import sleep
# Import the ThermSensor library

from w1thermsensor import W1ThermSensor 

sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    # Long way 
    F = temperature*1.8+32 # Convert Celsius to Fahrenheit
    F = round(F, 2) # Round to two decimal places
    # Short way 
    # temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    print("The temperature is %s" % F) # Print with formatting
    sleep(1)


