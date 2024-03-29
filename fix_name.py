import os


def ai_image():
    root_path = './AI_img/'
    file_name = os.listdir(root_path)

    for f in file_name:
        # new_f = f.split('.')[0]
        # new_f = new_f.split('-')
        # new_f[2] = new_f[2].replace('(', '').replace(')', '').zfill(3)
        # os.rename(root_path+f, root_path+'-'.join(new_f)+'.png')
        new_f = f.replace('-0000', '')
        os.rename(root_path + f, root_path + new_f)


def reindex_img(root_path):
    file_name = os.listdir(root_path)

    for index, f in enumerate(file_name):
        add_format = f.split('.')[-1]
        os.rename(root_path + f, root_path + f'image-{str(index+1).zfill(3)}.{add_format}')


def rename_jfif2jpg():
    root_path = './temp/'
    file_name = os.listdir(root_path)

    for f in file_name:
        new_f = f.replace('jfif', 'jpg')
        os.rename(root_path + f, root_path + new_f)


# ai_image()
reindex_img('./AI_img2/')
# rename_jfif2jpg()
