# 光照不均匀图像增强处理系统设计与实现

[toc]



## 概述

本文主要针对光照不均图像进行矫正处理，其中算法思想是拉高欠曝光区域亮度，降低高曝光区域亮度。从而促使整张图看起来和谐。

意外的是，本文算法对低光照图像处理也有特别好的效果。

**备注：**

本仓库首次上传代码时间为：6-5号，在答辩结束之后才会将论文上传上来。原理在论文内解释。
![](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20200605173632.png)

## 目录结构

```
C:.
├─.idea
│  └─inspectionProfiles
├─cds_arithmetic
│  └─data
│      ├─done
│      │  ├─179
│      │  ├─6
│      │  ├─778
│      │  ├─girl
│      │  └─matlab
│      └─src
│          ├─high
│          └─low
└─retinex
    ├─data
    └─__pycache__


```



![](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20200605172448.png)

## 配置环境

- python3.x
- opencv3.x or opencv4.x

## 使用方法

配置好环境可以直接运行。



```git
git remote add origin git@github.com:sexjun/-1602--.git
git push -u origin master
```





