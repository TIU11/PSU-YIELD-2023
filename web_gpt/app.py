from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.LightSensor import *
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
import csv
import time

# Initialize Flask app
app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configure Phidgets
try:
    temperature_sensor = TemperatureSensor()
    light_sensor = LightSensor()
    soil_moisture_sensor = VoltageRatioInput()
    ph_sensor = VoltageInput()
    water_pump = DigitalOutput()
    temperature_sensor.setDeviceSerialNumber(123456)  # Replace with your temperature sensor device serial number
    light_sensor.setDeviceSerialNumber(789012)  # Replace with your light sensor device serial number
    soil_moisture_sensor.setDeviceSerialNumber(345678)  # Replace with your soil moisture sensor device serial number
    ph_sensor.setDeviceSerialNumber(901234)  # Replace with your pH sensor device serial number
    water_pump.setDeviceSerialNumber(567890)  # Replace with your water pump device serial number
    temperature_sensor.setChannel(0)  # Replace with the channel of the temperature sensor
    light_sensor.setChannel(0)  # Replace with the channel of the light sensor
    soil_moisture_sensor.setChannel(0)  # Replace with the channel of the soil moisture sensor
    ph_sensor.setChannel(0)  # Replace with the channel of the pH sensor
    water_pump.setChannel(0)  # Replace with the channel of the water pump
    temperature_sensor.openWaitForAttachment(5000)
    light_sensor.openWaitForAttachment(5000)
    soil_moisture_sensor.openWaitForAttachment(5000)
    ph_sensor.openWaitForAttachment(5000)
    water_pump.openWaitForAttachment(5000)
except PhidgetException as e:
    print("PhidgetException %d: %s" % (e.code, e.details))
    exit(1)

# Create CSV file and headers
csv_file = open("hydroponics_data.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Timestamp", "Temperature (°C)", "Light Level (lux)", "Soil Moisture Level", "pH Level", "Water Pump State"])

# Control the water pump based on sensor readings and write data to CSV
def control_and_record_data():
    while True:
        # Read timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Read temperature
        temperature = temperature_sensor.getTemperature()

        # Read light level
        light_level = light_sensor.getIlluminance()

        # Read soil moisture level
        moisture_level = soil_moisture_sensor.getVoltageRatio()

        # Read pH level
        ph_level = ph_sensor.getVoltage()

        # Control water pump based on moisture level
        if moisture_level < 0.5:  # Adjust the threshold as needed
            water_pump.setState(True)  # Turn on the water pump
            water_pump_state = "On"
        else:
            water_pump.setState(False)  # Turn off the water pump
            water_pump_state = "Off"

        # Write data to CSV
        csv_writer.writerow([timestamp, temperature, light_level, moisture_level, ph_level, water_pump_state])
        csv_file.flush()

        time.sleep(5)  # Delay between readings

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for data display
@app.route('/data')
def data():
    data_list = []
    with open('hydroponics_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        for row in csv_reader:
            data_list.append(row)
    return render_template('data.html', headers=headers, data=data_list)

if __name__ == '__main__':
    # Start recording data in a separate thread
    import threading

    data_thread = threading.Thread(target=control_and_record_data)
    data_thread.start()

    # Run the Flask app
    app.run(debug=True)
