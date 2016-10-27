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


def get_output_filename(output, original_image, width, height):
    if output:
        return output
    else:
        list_filepath = os.path.splitext(original_image.name)
        file_name = list_filepath[0]
        file_ext = list_filepath[1]
        return file_name + '_' + str(width) + 'x' + str(height) + file_ext


def create_parser():
    parser = argparse.ArgumentParser(prog='Image resizer')

    parser.add_argument('file', nargs=1, type=Image.open)

    parser.add_argument('-s', '--scale', nargs='?', type=float)

    parser.add_argument('-w', '--width', nargs='?', type=int)
    parser.add_argument('-H', '--height', nargs='?', type=int)

    parser.add_argument('-o', '--output', nargs='?',type=Image.open)

    return parser


if __name__ == '__main__':

    parser = create_parser()

    # namespace = parser.parse_args(sys.argv[1:])                #!!!TODO del comment
    namespace = parser.parse_args(['blabla.bla.jpg', '-s', '2'])

    image_file = namespace.file[0]

    original_width = image_file.width
    original_height = image_file.height
    original_resolution = original_width/original_height

    if namespace.scale:
        if namespace.width or namespace.height:
            print('Error')
            print(parser.print_help())
            exit(1)
        width = namespace.scale*original_width
        height = namespace.scale*original_height
    else:
        width = namespace.width if namespace.width else original_width*namespace.height/original_height
        height = namespace.height if namespace.height else original_height*namespace.width/original_width

    width = int(width)
    height = int(height)

    if get_resolve_resize(width, height, original_width, original_height):
        output = get_output_filename(namespace.output, image_file, width, height)


    print(original_width, original_height)
    print(width, height)