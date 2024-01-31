import os
import glob
from mmseg.apis import MMSegInferencer


def find_png_files(directory):
    png_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'):
                png_files.append(os.path.join(root, file))
    return png_files


# inferencer = MMSegInferencer(model='deeplabv3plus_r18-d8_4xb2-80k_cityscapes-512x1024')
inferencer = MMSegInferencer(model='segformer_mit-b0_8xb1-160k_cityscapes-1024x1024')

directory = '/mmsegmentation/data/cityscapes/leftImg8bit/val'
img_paths = find_png_files(directory)
print('\n\nImage namber is: ', len(img_paths))


for index,img_path in enumerate(img_paths):
    print('Index: ',index, '    image path is: ',img_path)
    inferencer(img_path, out_dir='outputs', img_out_dir='vis', pred_out_dir='pred')

# inferencer('demo/demo.png', out_dir='outputs', img_out_dir='vis', pred_out_dir='pred')


# --------------------------------------------------------------------
# pspnet 网络
# --------------------------------------------------------------------
# from mmseg.apis import init_model, inference_model, show_result_pyplot
# config_path = 'configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024.py'
# checkpoint_path = 'checkpoints/pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth'
# img_path = 'demo/demo.png'

# model = init_model(config_path, checkpoint_path)
# result = inference_model(model, img_path)
# vis_iamge = show_result_pyplot(model, img_path, result, show=False, save_dir='result/')


# --------------------------------------------------------------------
# segformer 网络
# --------------------------------------------------------------------
# from mmseg.apis import init_model, inference_model, show_result_pyplot

# config_path = 'configs/segformer/segformer_mit-b0_8xb2-160k_ade20k-512x512.py'
# checkpoint_path = 'checkpoints/segformer_mit-b0_512x512_160k_ade20k_20210726_101530-8ffa8fda.pth'
# model = init_model(config_path, checkpoint_path)

# img_path = 'demo/demo.png'

# result = inference_model(model, img_path)
# vis_iamge = show_result_pyplot(model, img_path, result, show=False, save_dir='result123/')
