import cv2 as cv


def video_demo():
    # 0是代表摄像头编号，只有一个的话默认为0
    url = "http://admin:admin@192.168.123.58:8081/"
    capture = cv.VideoCapture(url)
    while capture.isOpened():
        print(capture.isOpened())
        ref, frame = capture.read()
        print(ref)
        cv.imshow("1", frame)
        # 等待30ms显示图像，若过程中按“Esc”退出
        c = cv.waitKey(30) & 0xFF
        if c == 27:
            capture.release()
            break


print("done")
video_demo()
cv.destroyAllWindows()
