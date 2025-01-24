import paho.mqtt.client as mqtt  

client_id = 'car'
broker = "192.168.1.7" 
port = 1883 
keepalive = 60 

CarState = 0

TopicMoveV = "car/moveV" 
TopicMoveH = "car/moveH" 
TopicMoveT = "car/moveT" 
TopicStop = "car/stop" 

TopicArmF = "car/arm/F" 
TopicArmR = "car/arm/R" 
TopicArmCO = "car/arm/CO" 
TopicArmCC = "car/arm/CC"
TopicCarStart = "car/Start"

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.user_data_set([])
mqttc.connect(broker, port, keepalive)
mqttc.loop_forever()

def driveCar(topic, speed):
    mqttc.publish(topic, speed) 
# test 慎重运行 保证小车在安全的位置
# mqttc.publish(TopicMoveV, 50) 