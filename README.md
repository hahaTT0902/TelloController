# Tello 无人机键盘控制器

这是一个使用 `OpenCV` 和 `djitellopy` 库开发的简单图形界面程序，用于通过键盘控制 DJI Tello 无人机的飞行方向,同时还具备人脸跟踪功能

## ✈️ 功能简介

- 显示一个简单的窗口
- 支持以下键盘按键进行无人机控制：
  - `W`: 向前移动
  - `S`: 向后移动
  - `A`: 向左移动
  - `D`: 向右移动
  - `R`: 上升
  - `F`: 下降
  - `Q`: 逆时针旋转
  - `E`: 顺时针旋转
  - `L`: 降落并退出程序
  - `SPACEBAR`: 开启人脸跟踪功能
- 飞行前自动起飞
- 实时显示电量（控制台）

## ⬇️ 安装依赖

请确保您已安装 Python 3，然后使用以下命令安装依赖项：

```bash
pip install -r requirements.txt
```
或者运行
```bash
pip install opencv-python
pip install djitellopy
