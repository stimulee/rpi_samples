#!/usr/bin/python
import RPi.GPIO as GPIO
import time,sys,getopt


# Servo Control
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
p = GPIO.PWM(5,50)
p.start(7.5)


#GPIO.setup(11, GPIO.OUT)
#p1 = GPIO.PWM(11,50)
#p1.start(7.5)


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

print "mode="
print mode

i = 0
#if mode > 0:
#	while i <=  mode:
#		print "Appui sur mode | " 
#	        p1.ChangeDutyCycle(12.5)
#	        time.sleep(delay_period)
#        	p1.ChangeDutyCycle(7.5)
#	        time.sleep(delay_period2)
#		i =i + 1
#	print "sortie de boucle"

if statu == "fermeture":
	print "Appui bouton bas ..."
	p.ChangeDutyCycle(2)
	time.sleep(delay_period)
	p.ChangeDutyCycle(7.5)
	time.sleep(delay_period2)
	print "Fermeture en cours"

elif statu == "ouverture":
	print "Appui bouton haut..."
	p.ChangeDutyCycle(12.5)
        time.sleep(delay_period)
        p.ChangeDutyCycle(7.5)
	time.sleep(delay_period2)
	print "Ouverture en cours"
else:
	print "ordre inconnu ou absent"
	print statu

p.stop()
#p1.stop()
GPIO.cleanup()


