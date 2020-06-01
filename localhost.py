import paho.mqtt.client as paho
import time
import matplotlib.pyplot as plt
import numpy as np
mqttc = paho.Client()

# Settings for connection
host = "localhost"
topic = "AccX"
topic2 = "AccY"
topic3 = "AccZ"
topic4 = "tilt"
port = 1883


x = []
y = []
z = []
tilt = []

# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
    print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n");
    if msg.topic == "AccX":
        x.append(float(msg.payload))
    elif msg.topic == "AccY":
        y.append(float(msg.payload))
    elif msg.topic == "AccZ":
        z.append(float(msg.payload))
    elif msg.topic == "tilt":
        tilt.append(float(msg.payload))
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)
mqttc.subscribe(topic2, 0)
mqttc.subscribe(topic3, 0)
mqttc.subscribe(topic4, 0)

while(len(tilt) < 39):
    mqttc.loop()
t = np.linspace(1,20,39)
plt.figure(2)
plt.plot(t, x, 'b', label = 'X')
plt.plot(t ,y , 'r', label = 'Y')
plt.plot(t, z, 'g', label = 'Z')
plt.xlabel("timestamp")
plt.ylabel("acc value")
plt.legend()
plt.show()
plt.figure(3)
plt.plot(t, tilt, 'y', label = 'Tilt')
plt.xlabel("timestamp")
plt.ylabel("Tilt")
plt.legend()
plt.show()