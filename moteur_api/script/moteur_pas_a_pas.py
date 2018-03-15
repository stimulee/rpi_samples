#!/usr/bin/python
import RPi.GPIO as GPIO
import time,sys,getopt


# Servo Control
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO_led=17
GPIO_moteur=5


GPIO.setup(GPIO_moteur, GPIO.OUT)
p = GPIO.PWM(GPIO_moteur,50)
p.start(7.5)

# GPIO_led will be an output pin
GPIO.setup(GPIO_led, GPIO.OUT)


#Gestion des parametres en entree
statu="neutre"
mode = 0

try:
	opts,args = getopt.getopt(sys.argv[1:],'hs:m:')
except getopt.GetoptError:
	print "error ARg"
	sys.exit(1)
for opt,arg in opts:
	if opt == '-s':
		statu=arg
        elif opt == '-m':
                mode=int(arg)

delay_period=0.5
delay_period2=0.05

pos90=7.5
pos180=12.5
pos0=2.5

if statu == "start":
	print "Avance ..."
	p.ChangeDutyCycle(2)
	time.sleep(delay_period)
	p.ChangeDutyCycle(7.5)
	time.sleep(delay_period2)

elif statu == "stop":
	print "Arret ..."
	GPIO.output(GPIO_moteur,GPIO.LOW)

else:
	print "ordre inconnu ou absent"
	print statu

p.stop()
GPIO.cleanup()


