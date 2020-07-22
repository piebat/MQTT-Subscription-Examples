from paho.mqtt.client import Client
import json


def on_message(client, userdata, message):
    topic = message.topic
    tras = json.loads(message.payload)
    # mess = json.loads(tras)
    for idx, mess in enumerate(tras):
        if idx == 0:
            print('Topic:' + topic + ' -> from gateway: ' + mess['mac'])
        else:
            print(mess['timestamp'] + ' ' + mess['mac'])

    # print("Received message '" + str(message.payload) + "' on topic '"
    #       + message.topic + "' with QoS " + str(message.qos))


client = Client(client_id="client_1")
client.connect("10.10.1.215", 1883)
client.subscribe("/GW/status")

client.on_message = on_message

client.loop_forever()
