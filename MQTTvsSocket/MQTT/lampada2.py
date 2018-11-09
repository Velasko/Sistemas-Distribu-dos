
import paho.mqtt.client as mqtt
import time

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
    client.subscribe("Lampada2/#")
 

def on_message(client, obj, msg):
    print("Lampada2 Status: "+str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Connect
mqttc.connect("m15.cloudmqtt.com", 16002)
mqttc.username_pw_set("dvgmojbv","j85EzWMG7ygv")

# Continue the network loop, exit when an error occurs
time.sleep(1)
mqttc.loop_forever()
