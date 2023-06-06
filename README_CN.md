基于https://github.com/clovaai/donut.git 进行二次开发，用于评估donut在中文的效果。
## 2023-06-04 
install debugpy 方便调试代码
## 调试代码遇到的问题
### 依赖库的问题
不能直接安装pip install . 安装
需要按照以下版本进行安装
```
torch == 1.11.0+cu113
torchvision == 0.12.0+cu113
pytorch-lightning == 1.6.4
transformers == 4.11.3
timm == 0.5.4
```
否则程序会报错
### 