import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)                          # set the GPIO mode

LED_PIN = 18                                    # GPIO pin #18 is Physical pin #12 (Pi 4B)

GPIO.setup(LED_PIN, GPIO.OUT)                   # Define the GPIO pin for the LED

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)         # Turn on LED
        time.sleep(0.5)

        GPIO.output(LED_PIN, GPIO.LOW)          # Turn off LED
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()                              # Clean up GPIO on CTRL + C
finally:
    GPIO.cleanup()                              # clean up GPIO on normal exit

