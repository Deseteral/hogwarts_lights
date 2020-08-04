import picoweb
import machine

app = picoweb.WebApp(__name__)

pwm_r = machine.PWM(machine.Pin(0), 5000)
pwm_g = machine.PWM(machine.Pin(4), 5000)
pwm_b = machine.PWM(machine.Pin(5), 5000)

def light_on():
    pwm_r.duty(1023)
    pwm_g.duty(1023)
    pwm_b.duty(1023)

def light_off():
    pwm_r.duty(0)
    pwm_g.duty(0)
    pwm_b.duty(0)

light_off()

@app.route('/', methods=['POST'])
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hogwarts lights")

@app.route('/light/on', methods=['POST'])
def homepage(request, response):
    light_on()
    yield from picoweb.jsonify(response, {'light': 'on'})
    return

@app.route('/light/off', methods=['POST'])
def homepage(request, response):
    light_off()
    yield from picoweb.jsonify(response, {'light': 'off'})
    return

import ulogging as logging
logging.basicConfig(level=logging.INFO)

app.run(debug=True, host='0.0.0.0', port=80)
