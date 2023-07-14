from flask import *
from time import time, strftime, sleep
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *

#red = LED(17)

def get_temp_data():
        #Create 
    temperatureSensor = TemperatureSensor()

    #Open 
    temperatureSensor.openWaitForAttachment(1000)
    readTemp = str(temperatureSensor.getTemperature())

    return (readTemp)
app = Flask(__name__)

@app.route('/') 
   
def index():
    readTemp = get_temp_data()
    now = time()
    now = strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': now,
      'readTemp': readTemp
      }
    return render_template('index.html', **templateData)

# Change LED value POST request.
#@app.route("/change_led_status/<int:status>", methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)