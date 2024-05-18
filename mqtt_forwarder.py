#!python3
#http://www.steves-internet-guide.com/client-connections-python-mqtt/

import paho.mqtt.client as mqtt
import datetime

# MQTT Broker Configuration
broker_address = "127.0.0.1"  # Replace with your broker's IP or hostname
broker_port = 1883  # Default MQTT port
broker_user= "emonpi"
proker_pass="emonpimqtt2016"
#shelly EM configuration
shelly_device_name="shellyem-123456ABCDEF"
k_power=1

# Shelly Topic and emonHub Topic
#shelly_topic = "shellies/+/voltage"  # Subscribe to all energy topics under "shellies"
shelly_topic_voltage = f"shellies/{shelly_device_name}/emeter/0/voltage"
shelly_topic_power1 = f"shellies/{shelly_device_name}/emeter/0/power"
shelly_topic_power2 = f"shellies/{shelly_device_name}/emeter/1/power"


emonhub_topic = "emon/shelly"  #topic to publish

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(shelly_topic_voltage)
        client.subscribe(shelly_topic_power1)
        client.subscribe(shelly_topic_power2)
    else:
        print("Bad connection Returned code= ",rc)


def on_message(client, userdata, msg):
    topic = msg.topic.split("/")[-1]  # Extract subtopic from Shelly topic
    clamp = msg.topic.split("/")[-2]
    payload = float(msg.payload.decode())  # Decode payload as string
    if topic == 'power':
        new_payload=k_power*payload
    else:
        new_payload=payload
    new_topic = f"{emonhub_topic}/{topic}{clamp}"  # Construct emonHub topic
    client.publish(new_topic, new_payload)  # Publish data to emonHub topic
    print(datetime.datetime.now())
    print(f"Received from Shelly: {msg.topic} - {payload}")
    print(f"Published to emonHub: {new_topic} - {new_payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=broker_user,password=proker_pass)

client.connect(broker_address, broker_port)

# Run the client in a loop
client.loop_forever()
