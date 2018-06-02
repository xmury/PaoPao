# Генератор поля
# def __init__(self, area):
#     super(Stalker, self).__init__()
#     self.area = area

from area import *

class Stalker(object):
    """Проходчик поля."""

    x_size = None; y_size = None    # Размеры поля
    free_box = None                 # Хранилище свободных ячеек
    area = None

    def way(self , dot , route ):   # dot = [x,y]
        x = dot[0]; y = dot[1]
        dx = 0; dy = 0
        if   route == "+x": dx =  1; x += dx;
        elif route == "-x": dx = -1; x += dx;
        elif route == "+y": dy =  1; y += dy;
        elif route == "-y": dy = -1; y += dy;

        while x <= self.x_size and y <= self.y_size:
            wr = str(x) + str(y)
            if self.area[wr] == 1: self.free_box += [wr]
            else: break
            x += dx; y += dy

        wr = str(x) + str(y)
        if x > self.x_size or y > self.y_size: self.free_box += [wr]

x = 3 # x ↓
y = 5 # y →

area = area_generator(x , y)
area_print_box(x , y , area)
area_print_coor(x , y)

M = Stalker()
M.free_box = [] ; M.area =  area
M.x_size = x ; M.y_size = y

M.way([1 , 1] , '+x')
print(M.free_box)
