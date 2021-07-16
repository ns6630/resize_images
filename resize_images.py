import os
from PIL import Image
import sys


def resize_image(input_image_path,
                 output_image_path,
                 max_size):
    try:
        with Image.open(input_image_path) as original_image:
            original_image.thumbnail(max_size)
            original_image.save(output_image_path)
    except IOError:
        pass


def resize_imgs_in_dir(processing_dir, dir_to_save_imgs, max_size):
    if not os.path.exists(dir_to_save_imgs):
        os.mkdir(path=dir_to_save_imgs, mode=0o777)

    names = os.listdir(processing_dir)
    for name in names:
        fullname = os.path.join(processing_dir, name)
        if os.path.isfile(fullname):
            print(fullname)
            output_image_path = fullname.replace(processing_dir, dir_to_save_imgs)
            resize_image(
                input_image_path=fullname,
                output_image_path=output_image_path,
                max_size=max_size
            )
        elif os.path.isdir(fullname) and fullname != dir_to_save_imgs:
            resize_imgs_in_dir(
                processing_dir=fullname,
                dir_to_save_imgs=fullname.replace(processing_dir, dir_to_save_imgs),
                max_size=max_size
            )


def main(args):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir_to_save_img = os.path.join(base_dir, 'copies')

    width = 1024
    height = 768
    if len(args) == 2:
        width, height = args
        try:
            width = int(width)
            height = int(height)
        except ValueError:
            print('Внешние аргументы не могут быть интерпретированы, проверьте ввод. '
                  'Ожидается два целых числа - максимальные значения ширины и высоты обрабатываемых изображений в '
                  'пикселях. Выполнение прервано.')
            return
    else:
        print('Максимальные значения ширины и высоты обрабатываемых изображений не были изменены пользователем. '
              'Будут задействованы значения по умолчанию.')
    print(f'Максимальные значения обрабатываемых изображений:\n\rширина: {width} px\n\rвысота: {height} px')

    resize_imgs_in_dir(
        processing_dir=os.path.join(base_dir, 'src'),
        dir_to_save_imgs=dir_to_save_img,
        max_size=(width, height)
    )

    print('Обработка изображений окончена.')


if __name__ == '__main__':
    main(sys.argv[1:])
