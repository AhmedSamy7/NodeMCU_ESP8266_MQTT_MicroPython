#works with this CloudMQTT the MQTT service provider
#https://api.cloudmqtt.com/console/25142656/websocket

#examples for the subscribe function
#https://github.com/micropython/micropython-lib/blob/mqtt/umqtt.simple/example_pubsub.py
#https://github.com/micropython/micropython-lib/blob/mqtt/umqtt.simple/example_sub.py
#https://github.com/micropython/micropython-lib/blob/mqtt/umqtt.simple/example_sub_led.py

import machine
from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin


CLIENT_ID = 'Home-Board'       #name your board any name you want
SERVER = 'm15.cloudmqtt.com'   #info from servce provider
Port=18570		       #info from servce provider
User='USERNAME'                #info from servce provider
Password='PASSWORD'            #info from servce provider


client = MQTTClient(CLIENT_ID, SERVER, Port, User, Password)
client.connect()   # Connect to MQTT broker


################################################################
##### very important to make the subscribe function work #######
################################################################
def sub_cb(topic, msg): #you have to set a callback, which means, what you gonna do with the subscribed msg
    print((topic, msg)) #the subsribed msg will be printed in the python consol
################################################################
################################################################

while True:
	
	TOPIC = b'test'
	msg=b'BOBO'
	client.publish(TOPIC, msg)
	sleep(2)


	client.set_callback(sub_cb) ##### very important to make the subscribe function work #######
	client.subscribe(b'Proportional') 
	sleep(2)
