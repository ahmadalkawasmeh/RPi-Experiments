from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import json
from sense_hat import SenseHat

sense = SenseHat()

# Global list colors holds the color of each LED div element on the website, which is why it contains 64 elements,
# later we convert the index from an integer to x, y coordinates in order to set the sense hat LEDs accordingly
colors = [[10,10,10] for i in range(64)]

# New instance of Flask
app = Flask(__name__)

# Setting password
app.config['SECRET_KEY'] = 'secret!'

# New socket for app flask instance, a socket is used for comms back and forth with website
socketio = SocketIO(app)

# Converts a RGB color expressed in HEX to RGB. HEX comes
# from the server, and RGB array used by SenseHAT.
def hex_to_rgb_color(color: str):
    color = color.strip('#')
    rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
    return rgb

# Button ids on html are integers.
# This function maps the led index to x and y.
def map_index_to_xy(led_index: int):
    return int(led_index%8), int(led_index/8)

@app.route('/')
def index():
    return render_template('Lab3-Colour-Picker.html')

# When users connect to the server using a web browser, a websocket is opened
# and this function is called to send the current LED colors
@socketio.on('connect')
def send_led_colors():
    print (f"sending colors.. {json.dumps(dict(colors=colors))}")
    emit('current_colors', json.dumps(dict(colors=colors)))

# When user clicks on a <div> in the webpage, the javascript sends a
# message encoded as update_led, where data contains the id of the <div>
# and the color of set in the <colorpicker>.
# Once the color is set, the server sends a broadcast message to all
# connected clients, which updates the LED color at each webbrowser screen.
@socketio.on('update_led')
def update_led_color(data):
    # Storing received JSON from website
    data = json.loads(data)
    # Converting the hex color to rgb
    color_rgb = hex_to_rgb_color(data['color'])
    # Setting reference to global variable colors to sync changes across whole script
    global colors
    # Updating rgb value for each LED in colors[id], where id is an int value of 0-63
    colors[int(data['id'])] = color_rgb

    # Iterate the colors[] list, convert each index to x,y coordinates, then set the sense hat LEDs
    for i in range(len(colors)):
        x, y = map_index_to_xy(i)
        sense.set_pixel(x, y, *colors[i])

    # Sends broadcast message to connected users.
    emit('update_led',
         json.dumps(dict(
            id=data['id'],
            color=data['color'])),
         broadcast=True)

@socketio.on('clear_leds')
def clear_led_colors():
    # Referring to global variable colors to sync color changing across the whole script
    global colors
    # Setting rgb color to black
    colors = [[10, 10, 10] for i in range(64)]

    # Iterating over list of each LED color, converting the index to an x,y coordinate, then setting that LED color
    for n in range(len(colors)):
        x, y = map_index_to_xy(n)
        sense.set_pixel(x, y, *colors[n])
        # Sending clear_led message to all connected users
        emit('clear_led', broadcast=True)
        # Updating website gui to reflect clearing LEDs
        emit('current_colors', json.dumps(dict(colors=colors)))

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)