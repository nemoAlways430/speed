import time
from mqttToCar import driveCar

TopicMoveV = "car/moveV" 
TopicMoveH = "car/moveH" 
TopicMoveT = "car/moveT" 
TopicStop = "car/stop" 

TopicArmF = "car/arm/F" 
TopicArmR = "car/arm/R" 
TopicArmCO = "car/arm/CO" 
TopicArmCC = "car/arm/CC"
TopicCarStart = "car/Start"

AlittleTime = 0.5

# 往前走一点
def goStraightALittle():
    driveCar(TopicMoveV, -20)
    time.sleep(AlittleTime)
    driveCar(TopicStop, 20)
# 往后走一点
def goStraightBackALittle():
    driveCar(TopicMoveV, 20)
    time.sleep(AlittleTime)
    driveCar(TopicStop, 20)
# 左横着走一点
def goHorizonLeftALittle():
    driveCar(TopicMoveH, 20)
    time.sleep(AlittleTime)
    driveCar(TopicStop, 20)
# 右横着走一点
def goHorizonRightALittle():
    driveCar(TopicMoveH, -20)
    time.sleep(AlittleTime)
    driveCar(TopicStop, 20)
# 往左转一点
def turnLeftALittle():
    driveCar(TopicMoveT, -20)
    time.sleep(AlittleTime)
    driveCar(TopicStop, 20)
# 往左转设定的时长
def turnLeftWithTime(interval):
    driveCar(TopicMoveT, -20)
    if isinstance(interval, (int, float)) and 0 <= interval <= 10:
     time.sleep(interval)
     driveCar(TopicStop, 20)
    else:
     return
# 往右转一点
def turnRightALittle():
    driveCar(TopicMoveT, 20)
    time.sleep(AlittleTime)
    driveCar(TopicStop, 20)
# 往右转设定的时长
def turnRightWithTime(interval):
    driveCar(TopicMoveT, 20)
    if isinstance(interval, (int, float)) and 0 <= interval <= 10:
     time.sleep(interval)
     driveCar(TopicStop, 20)
    else:
     return
# 向左前走一点
def goLeftAheadAlittle():
    turnLeftALittle()
    goStraightALittle()
# 向右前走一点
def goLeftAheadAlittle():
    turnRightALittle()
    goStraightALittle()
# 停止所有动作
def stopAllActions():
   driveCar(TopicStop, 20)
# 打开夹子
def openClap():
   driveCar(TopicArmCO, 20)
#  合上夹子
def closeClap():
   driveCar(TopicArmCC, 20)


# driveCar(TopicMoveV, 20) #向后走 夹子在前
# driveCar(TopicMoveV, -20) #向前走 夹子在后
# driveCar(TopicMoveT, -20) #左转
# driveCar(TopicMoveT, 20) #右转
# driveCar(TopicMoveH, 20) #横着走
# driveCar(TopicArmCO, 20) #打开夹子
# driveCar(TopicArmCC, 20) #关闭夹子
# driveCar(TopicStop, 20) #停
