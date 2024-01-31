数据集的准备    见 docs/zh_cn/user_guides/2_dataset_prepare.md


模型训练和测试  见 docs/zh_cn/user_guides/4_train_test.md
脚本位置：tools/train.py


预训练模型位置： segmentation/checkpoints
数据集位置：segmentation/data


各个模型的config位置：
segformer： segmentation/configs/segformer
pspnet：segmentation/configs/pspnet


DIY的几个脚本
推理接口使用 segmentation/image_inference.py
图像合成视频 segmentation/image_to_video.py