from openxlab.dataset import get
import openxlab
openxlab.login(ak="zwlbvxmj0korwg7mejwk", sk="2dxomqj8go6alr3vnap03b79dyalezd1p70rqg5z", relogin=True)
get(dataset_repo='OpenDataLab/ADE20K_2016', target_path='/mmsegmentation/ade/')  # target_path：下载文件指定的本地路径