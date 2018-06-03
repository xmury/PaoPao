# Генератор поля
from area import *
from stalker import *
x = 3 # x ↓
y = 5 # y →

area = area_generator(x , y)
area_print_box(x , y , area)
area_print_coor(x , y)

M = Stalker()
M.area =  area
M.x_size = x ; M.y_size = y

M.way([1 , 1] , '+x')
