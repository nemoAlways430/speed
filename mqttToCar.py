import paho.mqtt.client as mqtt  
import local_status

client_id = 'car'
broker = "192.168.1.5" 
port = 1883 
keepalive = 60

CarState = 0

def listen():
    local_status.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    local_status.mqttc.user_data_set([])
    local_status.mqttc.connect(broker, port, keepalive)
    print(f"[MQTT Ready]")

def driveCar(topic, speed):
    local_status.mqttc.publish(topic, speed) 
# test 慎重运行 保证小车在安全的位置
# mqttc.publish(TopicMoveV, 50) 