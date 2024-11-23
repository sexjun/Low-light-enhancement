import numpy as np
import cv2 as cv
import sys


def localStd(img):
    # 归一化
    # img = img / 255.0
    # 计算均值图像和均值图像的平方图像
    img_blur = cv.blur(img, (21, 21))
    reslut_1 = img_blur**2
    # 计算图像的平方和平方后的均值
    img_2 = img**2
    reslut_2 = cv.blur(img_2, (21, 21))

    reslut = np.sqrt(np.maximum(reslut_2 - reslut_1, 0))
    return reslut


def get_reflect(img, img_illumination):
    # get_img_illumination = get_illumination(img)
    get_img_reflect = (img + 0.001) / (img_illumination + 0.001)
    return get_img_reflect


def enhancement_reflect(img):
    # 通过高斯滤波器
    gaussian_blur_img = cv.GaussianBlur(img, (21, 21), 0)
    enhancement_reflect_img = img * gaussian_blur_img
    return enhancement_reflect_img


def get_enhancment_img(img_enhance_illumination, img_enahnce_reflect):
    img = img_enhance_illumination * img_enahnce_reflect
    img = img.astype("uint8")
    return img


def read_img_from_disk(file_path):
    # 0. 读取图像
    img = cv.imread(file_path, cv.IMREAD_COLOR)
    return img


def get_illumination(img):
    return cv.GaussianBlur(img, (15, 15), 0)


"""
enhancment_illumination 增强反射分量，传入反射分量，返回增强后的反射分量
"""


def enhancment_illumination(img_illumination):
    img_hsv = cv.cvtColor(img_illumination, cv.COLOR_BGR2HSV)
    img_hsv = (img_hsv - np.min(img_hsv)) / (np.max(img_hsv) - np.min(img_hsv))
    h, s, v = cv.split(img_hsv)
    wsd = 5
    gm = np.mean(v) / (1 + wsd * np.std(v))  # 一个数字
    cst = localStd(v)  # 300 * 400 的矩阵
    lm = gm * v / (1 + wsd * cst)  # 300 * 400 的矩阵
    c = np.exp(gm)  # 一个常数
    wg = v**0.2  # 300 *400
    wl = 1 - wg
    outM = v**c / (v**c + (wl * lm) ** c + (wg * gm) ** c + 0.001)
    outM = 1.5 * outM - 0.5 * cv.GaussianBlur(outM, (21, 21), 0)
    outM = (outM - np.min(outM)) / (np.max(outM) - np.min(outM))
    paramerter = 0.9
    img_illumination[:, :, 0] = (
        outM * (img_illumination[:, :, 0] / (v + 0.01)) ** paramerter
    )
    img_illumination[:, :, 1] = (
        outM * (img_illumination[:, :, 1] / (v + 0.01)) ** paramerter
    )
    img_illumination[:, :, 2] = (
        outM * (img_illumination[:, :, 2] / (v + 0.01)) ** paramerter
    )
    return img_illumination
