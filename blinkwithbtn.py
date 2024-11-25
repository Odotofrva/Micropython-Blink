import RPi.GPIO as GPIO                   
import time

LED_PIN = 18                              # GPIO pin for the Onboard LED
BUTTON_PIN = 23                           # GPIO pin for the button

GPIO.setmode(GPIO.BCM)                    # Use BCM pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)             # Set LED pin as output


# Set button pin as input with pull-down resistor.
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)     

led_state = False                         # initialize LED state


def toggle_led(channel):
    global led_state
    led_state = not led_state             # toggle the state 
    GPIO.output(LED_PIN, led_state)       # set the LED state


# add event detection for button press
GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=toggle_led, bouncetime=200)


try:
    print("Press the button to toggle the LED!")
    while True:
        time.sleep(0.1)                   # delay half sec.  

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    GPIO.cleanup()                        # Clean up GPIO settings