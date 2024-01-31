## Introduction
官方readme： [英文版](README-original.md)  | [中文版](README_zh-CN.md)

## 数据集的准备    
文档：docs/zh_cn/user_guides/2_dataset_prepare.md

数据集位置：segmentation/data

## 模型训练和测试  
文档：docs/zh_cn/user_guides/4_train_test.md

脚本位置：tools/train.py

预训练模型位置： segmentation/checkpoints


## 各个模型的config位置
**segformer**： segmentation/configs/segformer
这里就有每个数据集对应的预训练模型下载链接   https://github.com/xiaoyuyang0901/segmentation/tree/master/configs/segformer

**pspnet**：segmentation/configs/pspnet
这里就有每个数据集对应的预训练模型下载链接   https://github.com/xiaoyuyang0901/segmentation/blob/master/configs/pspnet/README.md

## 接口使用
推理接口使用 segmentation/image_inference.py

图像合成视频 segmentation/image_to_video.py
