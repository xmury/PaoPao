import random
def area_generator(x , y):
    area = {};
    x += 1; y += 1
    for w in range(1 , x):
        for r in range(1 , y):
            wr = str(w) + str(r)
            area[wr] = random.randint(1,2)
    return area
area = area_generator(1,5)

def area_print_box(x , y , area):
    x += 1; y += 1
    for w in range(1 , x):
        for r in range(1 , y):
            wr = str(w) + str(r)
            print(area[wr] , end='|')
        print()
    print()

def area_print_coor(x , y):
    x += 1; y += 1
    for w in range(1 , x):
        for r in range(1 , y):
            wr = str(w) + str(r)
            print(wr , end='|')
        print()
    print()
