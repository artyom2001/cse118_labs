import RPi.GPIO as GPIO
import time

LED_PIN = 7
ECHO_PIN = 16
TRIGGER_PIN = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT) # LED
GPIO.setup(ECHO_PIN, GPIO.IN) # ECHO
GPIO.setup(TRIGGER_PIN, GPIO.OUT) # TRIGGER

def distance():
	GPIO.output(TRIGGER_PIN, GPIO.LOW)
	time.sleep(0.25)
	GPIO.output(TRIGGER_PIN, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(TRIGGER_PIN, GPIO.LOW)
	
	startTime = time.time()
	stopTime = time.time()
	
	while GPIO.input(ECHO_PIN) == 0:
		startTime = time.time()
		
	while GPIO.input(ECHO_PIN) == 1:
		stopTime = time.time()
	
	delta = stopTime - startTime
	distance = (delta * 34300) / 2 # 34300 is the speed of sound in cm/s and divide by 2 because sound travels back and forth
	return distance

print("Hey There!")
print("Starting...")

pwm = GPIO.PWM(LED_PIN, 100)
pwm.start(0)

try:
	while True:
		d = distance()
		if d > 100:
			d = 100
		pwm.ChangeDutyCycle(d)
		print("Distance: %.1f cm" % d)
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
	print("Keyboard Input Detected: Finshed!")

pwm.stop()
GPIO.cleanup()
