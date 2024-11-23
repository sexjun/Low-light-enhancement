import json
import time
from cds_arithmetic.cds_retinex import *
from retinex.retinex import *


test_png = "./cds_arithmetic/data/src/3.jpg"


def cds_algo(img):
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


def retinex_algo(img):
    with open("./retinex/config.json", "r") as f:
        config = json.load(f)
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
    cv.imshow("origin-png", img)
    cv.imshow("retinex", img_msrcr)
    cv.imshow("Automated_retinex", img_amsrcr)
    cv.imshow("MSRCP", img_msrcp)


if __name__ == "__main__":
    img = read_img_from_disk(test_png)  # 读取图像
    # 获取原始图像的尺寸
    height, width = img.shape[:2]
    print("原始图像高度:", height)
    print("原始图像宽度:", width)

    # 调整图像大小为500*500
    img = cv.resize(img, (500, 500))
    cds_algo(img)
    retinex_algo(img)
    cv.waitKey(0)
    print("关闭所有窗口")
    # 关闭所有窗口
    cv.destroyAllWindows()
