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


if __name__ == '__main__':
    
    width_original = 1920
    height_original = 1024

    if scale:
        if width or height:
            #ошибка
            pass
    elif width and height:
        if not get_resolve_resize(width ,height,width_original, height_original):
            pass
    else:
        #расчет пропорций
        pass