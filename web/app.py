from flask import *
from time import time, strftime, sleep
from gpiozero import LED
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *

red = LED(17)

app = Flask(__name__)

@app.route('/')
def index():
    now = time()
    now = strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': now
      }
    return render_template('index.html', **templateData)

# Change LED value POST request.
#@app.route("/change_led_status/<int:status>", methods=['POST'])

def get_temp_data():
        #Create 
    temperatureSensor = TemperatureSensor()

    #Open 
    temperatureSensor.openWaitForAttachment(1000)
    readTemp = temperatureSensor.getTemperature()

    return render_template('index.html',readTemp=readTemp)
    

""" def change_led_status(status):

  if status == 0:
    red.off()
  elif status == 1:
    red.on()
  else:
    return ('Error', 500)
  return ('', 200)
 """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)