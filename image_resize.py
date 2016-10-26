import os
import sys
import argparse
from PIL import Image


def resize_image(path_to_original, path_to_result):
    pass


def get_resolve_resize(width ,height, width_original, height_original):
    if width/height != width_original/height_original:
        answer = input('Новые пропорции не совпадают с исходными. Продолжить [Y]/n?')
        return answer.upper() in ['Y', '']
    return True


def get_new_size(width ,height, width_original, height_original):
    pass


   


def create_parser():
    parser = argparse.ArgumentParser(prog='Image resizer')

    # parser.add_argument('file', nargs='?', type=argparse.FileType())
    # parser.add_argument('-w', '--width', type=int)
    # parser.add_argument('-H', '--height', type=int)
    # parser.add_argument('-s', '--scale', type=float)
    # parser.add_argument('-o', '--output', type=argparse.FileType(mode='w'))


    subparsers = parser.add_subparsers(dest='command')

    scale_parser = subparsers.add_parser('scale')
    scale_parser.add_argument('file', nargs='+', type=Image.open)
    # scale_parser.add_argument('-s', '--scale', nargs='?', type=float)
    scale_parser.add_argument('-o', '--output', type=argparse.FileType(mode='w'))

    size_parser = subparsers.add_parser('size')
    size_parser.add_argument('file', nargs='+', type=argparse.FileType())
    size_parser.add_argument('-w', '--width', nargs='?', type=int)
    size_parser.add_argument('-H', '--height', nargs='?', type=int)
    size_parser.add_argument('-o', '--output', type=argparse.FileType(mode='w'))

    return parser



if __name__ == '__main__':

    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    
    # if namespace.scale:
    #     if namespace.width or namespace.height:


    # width = 100
    # height = 200

    # list_filepath = os.path.splitext(namespace.file.name)
    # file_name = list_filepath[0]
    # file_ext = list_filepath[1]

    # if namespace.output:
    #     resultpath = namespace
    # else:
    #     resultpath = file_name + '_' + str(width) + 'x' + str(height) + file_ext

    # print()
    # print(resultpath)


    print()
    print(namespace)

    # if namespace.filepath:
    #     print ("Привет, {}!".format (namespace.filepath) )
    # else:
    #     print ("Привет, мир!")

    # width_original = 1920
    # height_original = 1024

    # if scale:
    #     if width or height:
    #         #ошибка
    #         pass
    # elif width and height:
    #     if not get_resolve_resize(width ,height,width_original, height_original):
    #         pass
    # else:
    #     #расчет пропорций
    #     pass