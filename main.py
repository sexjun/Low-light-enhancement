import json
import time
from cds_arithmetic.cds_retinex import *
from retinex.retinex import *


test_png = "./cds_arithmetic/data/src/3.jpg"


def cds_algo():
    img = read_img_from_disk(test_png)  # 读取图像
    img_illumination = get_illumination(img)  # 获得高频分量
    img_reflect = get_reflect(img, img_illumination)  # 获得反射分量
    img_enhancement_reflect = enhancement_reflect(img_reflect)  # 增强反射分量
    img_enhancement_illumination = enhancment_illumination(
        img_illumination
    )  # 增强照射分量
    img_done = get_enhancment_img(
        img_enhancement_illumination, img_reflect
    )  # 照射分量与反射分量融合
    cv.imshow("src", img)
    cv.imshow("cds-algo", img_done)


def retinex_algo():
    with open("./retinex/config.json", "r") as f:
        config = json.load(f)
    img = cv.imread(test_png)
    # img = cv.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv.INTER_NEAREST)
    img_msrcr = MSRCR(
        img,
        config["sigma_list"],
        config["G"],
        config["b"],
        config["alpha"],
        config["beta"],
        config["low_clip"],
        config["high_clip"],
    )

    img_amsrcr = automatedMSRCR(img, config["sigma_list"])

    img_msrcp = MSRCP(
        img, config["sigma_list"], config["low_clip"], config["high_clip"]
    )

    shape = img.shape
    cv.imshow("原图", img)
    cv.imshow("retinex", img_msrcr)
    cv.imshow("Automated_retinex", img_amsrcr)
    cv.imshow("MSRCP", img_msrcp)


if __name__ == "__main__":
    cds_algo()
    retinex_algo()
    # 记录开始时间
    start_time = time.time()

    while True:
        # 等待按键事件，返回值为按下键的ASCII码
        key = cv.waitKey(1)

        # 计算已经过去的时间
        elapsed_time = time.time() - start_time

        print("倒计时60 s 关闭窗口", elapsed_time)

        # 如果已经过去了60秒，就退出循环
        if elapsed_time >= 60:
            break

    print("关闭所有窗口")
    # 关闭所有窗口
    cv.destroyAllWindows()
