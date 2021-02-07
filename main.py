# Hardware setup
import machine

pwm_r = machine.PWM(machine.Pin(0), 5000)
pwm_g = machine.PWM(machine.Pin(4), 5000)
pwm_b = machine.PWM(machine.Pin(5), 5000)

is_on=False
r_value = 1023
g_value = 1023
b_value = 1023

def light_on():
    is_on = True
    apply_lights_value()

def light_off():
    is_on = False
    pwm_r.duty(0)
    pwm_g.duty(0)
    pwm_b.duty(0)

def apply_lights_value():
    if not is_on:
        return
    pwm_r.duty(r_value)
    pwm_g.duty(g_value)
    pwm_b.duty(b_value)

light_off()

# Server setup
import picoweb
import ulogging as logging

app = picoweb.WebApp(__name__)

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

@app.route('/light/values', methods=['POST'])
def homepage(request, response):
    light_off()
    yield from picoweb.jsonify(response, {'light': 'off'})
    return

logging.basicConfig(level=logging.INFO)

app.run(debug=True, host='0.0.0.0', port=80)
