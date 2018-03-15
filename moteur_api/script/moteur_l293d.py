#!/usr/bin/python
import RPi.GPIO as GPIO
import time,sys,getopt


# Servo Control
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO_led=17
GPIO_moteur_pap=5
GPIO_moteur_1_pwm=18
GPIO_moteur_1_av=27
GPIO_moteur_1_ar=12


# GPIO_led will be an output pin
GPIO.setup(GPIO_led, GPIO.OUT)

# GPIO_moteur_pas_a_pas
#GPIO.setup(GPIO_moteur_pap, GPIO.OUT)
#p = GPIO.PWM(GPIO_moteur_pap,50)
#p.start(7.5)

# GPIO_moteur classique via l293d
GPIO.setup(GPIO_moteur_1_pwm, GPIO.OUT)
GPIO.setup(GPIO_moteur_1_av, GPIO.OUT)
GPIO.setup(GPIO_moteur_1_ar, GPIO.OUT)


#Gestion des parametres en entree
#statu="neutre"
#mode = 0

def avance(GPIO_moteur_1_pwm,GPIO_moteur_1_av,GPIO_moteur_1_ar):
	print "en route"
	GPIO.output(GPIO_led, True)
	GPIO.output(GPIO_moteur_1_pwm, True)
	GPIO.output(GPIO_moteur_1_av, True)
	GPIO.output(GPIO_moteur_1_ar, False)

def recule(GPIO_moteur_1_pwm,GPIO_moteur_1_av,GPIO_moteur_1_ar):
	print "en arriere"
	GPIO.output(GPIO_moteur_1_pwm, True)
	GPIO.output(GPIO_moteur_1_av, False)
	GPIO.output(GPIO_moteur_1_ar, True)

def arrete(GPIO_moteur_1_pwm,GPIO_moteur_1_av,GPIO_moteur_1_ar):
	GPIO.output(GPIO_led, False)
	print "halte"
	GPIO.output(GPIO_moteur_1_pwm, False)


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

#delay_period=0.5
#delay_period2=0.05

#pos90=7.5
#pos180=12.5
#pos0=2.5

#if statu == "start":
#	print "Start ..."
#	p.ChangeDutyCycle(2)
#	time.sleep(delay_period)
#	p.ChangeDutyCycle(7.5)
#	time.sleep(delay_period2)

#elif statu == "stop":
#	print "Stop ..."
#	GPIO.output(GPIO_moteur_pap,GPIO.LOW)

#el

if statu == "avance":
	print "Avance ... {} , {}, {}" .format(GPIO_moteur_1_pwm, GPIO_moteur_1_av, GPIO_moteur_1_ar)
	avance(GPIO_moteur_1_pwm,GPIO_moteur_1_av,GPIO_moteur_1_ar)

elif statu == "recule":
	print "Recule ..."
	recule(GPIO_moteur_1_pwm,GPIO_moteur_1_av,GPIO_moteur_1_ar)

elif statu == "arrete":
	print "Arrete ..."
	arrete(GPIO_moteur_1_pwm,GPIO_moteur_1_av,GPIO_moteur_1_ar)

else:
	print "ordre inconnu ou absent"
	print statu

#p.stop()
#GPIO.cleanup()


