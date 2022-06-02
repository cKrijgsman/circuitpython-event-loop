import event
import board
import p9813

# --- chainable leds variables
pin_clk = board.D7
pin_data = board.D13
num_leds = 1
chain = p9813.P9813(pin_clk, pin_data, num_leds)

# --Button and slider varibles
button_port = board.D2
slider_port = board.A4

# Global variable to indicate if the LED is fading
fading = 0

# Set an timeout for every second the first 10 seconds long.
# Here lambda functions are used. 
event.set_timeout(lambda : print("its been 10 seconds sins the start"), 10)
event.set_timeout(lambda : print("its been 10 seconds sins the start"), 1)
event.set_timeout(lambda : print("its been 10 seconds sins the start"), 2)
event.set_timeout(lambda : print("its been 10 seconds sins the start"), 3)
event.set_timeout(lambda : print("its been 10 seconds sins the start"), 4)
event.set_timeout(lambda : print("its been 10 seconds sins the start"), 5)
event.set_timeout(lambda : print("its been 10 seconds sins the start"), 6)
event.set_timeout(lambda : print("its been 10 seconds sins the start"), 7)

# start and save an interval that will print every two seconds.
interval_variable = event.set_interval(lambda : print("its been 2 seconds"), 2)

# set a timer for 12 seconds and afterwards stop the interval.
event.set_timeout(lambda : event.stop_interval(interval_variable), 12)

# function that fades the LED
def start_fade(state):
    global fading
    if state:
        if fading:
            event.stop_async_for(fading)
        fading = event.async_for(range(0, 200, 2), fade)
    else:
        if fading:
            event.stop_async_for(fading)
        fading = event.async_for(range(200, 0, -2), fade, off)


def fade(value):
    chain[0] = (value, value, value)
    chain.write()


def off():
    chain[0] = (0, 0, 0)
    chain.write()


# Examples of events on the digital port
#event.digital_on("change", button_port, start_fade)
event.digital_on("change", button_port, start_fade)
#event.digital_on("click", button_port, lambda _=0: print("Button Pressed!"))
#event.digital_on("change", button_port, lambda x=0: print(x))

# Examples of events on the analog port
# event.analog_on("change", slider_port, lambda val=0: print(val), 10, 300)
# event.analog_on("above", slider_port, lambda: start_fade(True), 80, 100)
# event.analog_on("below", slider_port, lambda: start_fade(False), 10, 100)

# The while loop
def whileTrue():
    print("TRUE")
    


# This starts the while True loop.
event.event_loop(whileTrue)


