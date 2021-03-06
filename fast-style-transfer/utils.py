import scipy.misc, numpy as np, os, sys
from tensorflow.python.lib.io import file_io

def save_img(out_path, img):
    out_path = file_io.FileIO(out_path, mode='w')
    img = np.clip(img, 0, 255).astype(np.uint8)
    scipy.misc.imsave(out_path, img)
    out_path.close()

def scale_img(style_path, style_scale):
    scale = float(style_scale)
    _style_path = file_io.FileIO(style_path, mode='r')
    o0, o1, o2 = scipy.misc.imread(_style_path, mode='RGB').shape
    _style_path.close()
    scale = float(style_scale)
    new_shape = (int(o0 * scale), int(o1 * scale), o2)
    style_target = _get_img(style_path, img_size=new_shape)
    return style_target

def get_img(src, img_size=False):
    src = file_io.FileIO(src, mode='r')
    img = scipy.misc.imread(src, mode='RGB') # misc.imresize(, (256, 256, 3))
    src.close()
    if not (len(img.shape) == 3 and img.shape[2] == 3):
        img = np.dstack((img,img,img))
    if img_size != False:
        img = scipy.misc.imresize(img, img_size)
    return img

def exists(p, msg):
    # assert os.path.exists(p), msg
    assert file_io.file_exists(p), msg

def list_files(in_path):
    files = []
    # for (dirpath, dirnames, filenames) in os.walk(in_path):
    for (dirpath, dirnames, filenames) in file_io.walk(in_path):
        files.extend(filenames)
        break

    return files

