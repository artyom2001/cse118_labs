import RPi.GPIO as GPIO
import time

LED_PIN = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT) # LED

print("Hey There!")
print("Starting...")

pwm = GPIO.PWM(LED_PIN, 100)
pwm.start(0)

try:
	# pwm.ChangeDutyCycle(100)
	# pwm.ChangeDutyCycle(75)
	# pwm.ChangeDutyCycle(50)
	# pwm.ChangeDutyCycle(25)
	for dc in range(0,100,1): # Sweep from no light to full brightness
		pwm.ChangeDutyCycle(dc)
		print(dc)
		time.sleep(0.1)
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
	print("Keyboard Input Detected: Finshed!")

pwm.stop()
GPIO.cleanup()
