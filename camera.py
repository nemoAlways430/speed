import cv2
import numpy as np
import requests
import local_status

def listen():
    # 设置树莓派视频流地址
    video_url = "http://192.168.1.5:5000/video_feed"  # 替换为树莓派的实际 IP 地址
    # 打开视频流请求
    stream = requests.get(video_url, stream=True)
    
    if stream.status_code != 200:
        print(f"Failed to connect to video stream: {stream.status_code}")
        exit()
    
    print(f"[Camera Ready]")

    # 读取 HTTP 响应内容
    byte_data = b""
    for chunk in stream.iter_content(chunk_size=1024):
        byte_data += chunk
        # 搜索 JPEG 图片的开始和结束位置
        start = byte_data.find(b'\xff\xd8')  # JPEG 开始标志
        end = byte_data.find(b'\xff\xd9')  # JPEG 结束标志

        if start != -1 and end != -1:
            # if local_status.Catch_Img == True:
         # 提取 JPEG 数据
            jpg_data = byte_data[start:end+2]
            byte_data = byte_data[end+2:]
            # 将 JPEG 数据解码为图像
            frame = cv2.imdecode(np.frombuffer(jpg_data, np.uint8), cv2.IMREAD_COLOR)
            # callback(frame)
            cv2.imshow("Video Stream", frame)
               
                