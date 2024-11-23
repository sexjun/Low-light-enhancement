# 光照不均匀图像增强处理系统设计与实现

[toc]

## 配置环境

- python3.x
- opencv3.x or opencv4.x

```
conda install opencv
```

## 使用方法 & 效果展示

配置好环境可以直接运行。

```
cd /home/cds/github/Low-light-enhancement
python main.py
```
![alt text](image.png)


## 概述

本文主要针对光照不均图像进行矫正处理，其中算法思想是拉高欠曝光区域亮度，降低高曝光区域亮度。从而促使整张图看起来和谐。

意外的是，本文算法对低光照图像处理也有特别好的效果。

**备注：**

本仓库首次上传代码时间为：6-5号，在答辩结束之后才会将论文上传上来。原理在论文内解释。

## 目录结构

```
├── cds_arithmetic  这个目录是本论文的算法
│   ├── __pycache__
│   ├── cds_retinex.py
│   ├── data
│   ├── readme.md
│   └── video.py
├── main.py   主函数在这里
├── readme.md
└── retinex 这个目录实现各种retinex算法
    ├── README.md
    ├── __pycache__
    ├── config.json
    ├── data
    ├── retinex.py
    ├── run.py
    └── run_cds.py
```
![](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20200605172448.png)


## note

为了快速预览效果，我把图像resize到 `500*500`区间了

删除下面这行代码即可看到原始图像的处理
```
    调整图像大小为500*500
    img = cv.resize(img, (500, 500))
```
