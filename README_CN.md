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
### 使用预训练模型
版本回退之后，不能使用下载的预训练模型，需要使用网络的预训练模型，由程序进行直接下载。才能进行训练和预测。
### cord的训练
A4000训练12个小时以上，基于donut-base的预训练模型，可以有结构化的数据出现（正确率不到70%），效果非常不错了
### 预训练模型的训练信息
https://github.com/clovaai/donut/issues/190
1. 预训练时，每个GPU的batch size是3。
2. 使用了cosine 训练策略。
3. 总共训练了3个epoch，11M的IIT数据和2M合成数据。
4. 使用了64个 A100 GPU，

## 2023-06-07 05:20:25
没有白熬夜，模型训练的效果非常好。
Prediction: <s_full_name><s_fn>北京银信长远科技股份有限公司</s_fn></s_full_name><s_code_name><s_cn>300231</s_cn></s_code_name><s_short_name><s_sn>银信科技</s_sn></s_short_name>                                                                                                                                
    Answer: <s_full_name><s_fn>北京银信长远科技股份有限公司</s_fn></s_full_name><s_code_name><s_cn>300231</s_cn></s_code_name><s_short_name><s_sn>银信科技</s_sn></s_short_name>                                                                                                                                
 Normed ED: 0.0                                                                                                                                                                                                                                                                                                 
Prediction: <s_full_name><s_fn>冠契生物科技股份有限公司</s_fn></s_full_name><s_code_name><s_cn>300238</s_cn></s_code_name><s_short_name><s_sn>冠契生物</s_sn></s_short_name>                                                                                                                                    
    Answer: <s_full_name><s_fn>冠昊生物科技股份有限公司</s_fn></s_full_name><s_code_name><s_cn>300238</s_cn></s_code_name><s_short_name><s_sn>冠昊生物</s_sn></s_short_name>                                                                                                                                    
 Normed ED: 0.013888888888888888                                                                                                                                                                                                                                                                                
Prediction: <s_full_name><s_fn>河北常山生物业股份有限公司</s_fn></s_full_name><s_code_name><s_cn>300255</s_cn></s_code_name><s_short_name><s_sn>常山药业</s_sn></s_short_name>                                                                                                                                  
    Answer: <s_full_name><s_fn>河北常山生化药业股份有限公司</s_fn></s_full_name><s_code_name><s_cn>300255</s_cn></s_code_name><s_short_name><s_sn>常山药业</s_sn></s_short_name>                                                                                                                                
 Normed ED: 0.0136986301369863   