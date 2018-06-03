class Stalker(object):
    """Проходчик поля."""

    x_size = None; y_size = None    # Размеры поля
    area = None
    free_box_d1 = None; free_box_d2 = None;

    def way(self , dot , route ):   # dot = [x,y]
        x = dot[0]; y = dot[1]
        dx = 0; dy = 0
        free_box = []
        if   route == "+x": dx =  1; x += dx;
        elif route == "-x": dx = -1; x += dx;
        elif route == "+y": dy =  1; y += dy;
        elif route == "-y": dy = -1; y += dy;

        while x <= self.x_size and y <= self.y_size:
            wr = str(x) + str(y)
            if self.area[wr] == 1: free_box += [wr]
            else: break
            x += dx; y += dy

        wr = str(x) + str(y)
        if x > self.x_size or y > self.y_size: free_box += [wr]
        return free_box

    def give_route(dot):
        free_box = []
        free_box += [self.way(dot, '+x')]
        free_box += [self.way(dot, '-x')]
        free_box += [self.way(dot, '+y')]
        free_box += [self.way(dot, '-y')]
        return free_box

    def search_perspec_box():
        perspec_box = []
        for cr1 in self.free_box_d1:
            for cr2 in self.free_box_d2:
                x1 = int(cr1[0]); y1 = int(cr1[0]);
                x2 = int(cr2[0]); y2 = int(cr2[0]);

                if  x1 == x2: perspec_box += [x1, y1, 'y']
                if  y1 == y2: perspec_boy += [y1, y1, 'x']
        return perspec_box

    def run_perspec(perspec_box):       # perspec_box = [x , y , 'route']
        for cr int perspec_box:
            if perspec_box[2] == 'x':
