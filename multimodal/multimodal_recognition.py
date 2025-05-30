import cv2
import threading
from gesture.gesture_recognition import GestureRecognition
from video.video_recognition import VisualRecognition
from audio.audio_recognition import AudioRecognition

# 手势识别参数
DEVICE_ID = 0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
DESIRED_FPS = 90

# 全局变量
stop_event = threading.Event()  # 用于停止线程的事件
user_id = "user123"   # 后面改成从配置文件中读取

if __name__ == '__main__':
    try:
        capture = cv2.VideoCapture(DEVICE_ID)
        capture.set(cv2.CAP_PROP_FPS, DESIRED_FPS)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        gesture_recognition = GestureRecognition(capture,user_id)
        visual_recognition = VisualRecognition(user_id)

        audio_thread = AudioRecognition(stop_event,user_id)
        audio_thread.start()

        try:
            while True:
                ret, frame = capture.read()
                if ret:
                    # 处理手势识别
                    result = gesture_recognition.process_frame(frame)
                    frame = result.get('frame')
                    # gesture_recognized_text = result.get('text')
                    # print(gesture_recognized_text)
                    
                    # 处理视觉识别
                    frame = visual_recognition.process_frame(frame)
                    
                    cv2.imshow('Combined Recognition', frame)

                    key = cv2.waitKey(1)
                    if key in (27, ord('q')):
                        stop_event.set()  # 设置停止事件
                        break
                else:
                    break
        except KeyboardInterrupt:
            stop_event.set()  # 设置停止事件
            print("关闭...")
        finally:
            capture.release()
            cv2.destroyAllWindows()

        audio_thread.join()

    except Exception as e:
        print(f"程序运行失败: {str(e)}")
        print(e)
    finally:
        stop_event.set()
        print('程序运行结束')