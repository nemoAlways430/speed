树莓派中需要进行的操作：
1. 打开板子开关， remote到树莓派系统里, (192.168.1.7) username:speed
2. 找到桌面上speed文件夹，进到robotCar下
<!-- 切换到root账户 -->
3. sudo su 
<!-- 切换到nemoenv这个虚拟环境下，这里面已经装好了我们需要的包 -->
4. source nemoenv/bin/activate 
<!-- 获取视频流并且可以通过http://192.168.1.7:5000/video_feed访问 -->
<!-- 打开你的浏览器访问http://192.168.1.7:5000/video_feed可以看到视频了 -->
5. python flask/flaskCam.py 
<!-- 启动mqtt server并且订阅信息和执行相应的运动行为 -->
6. python CAR/MQTT.py
   
   