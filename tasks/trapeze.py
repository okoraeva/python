import math
class Trapeze():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, can_continue = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.can_continue = can_continue

    def check_existence(self):
        if ((self.y2 == self.y3) and (self.y1 == self.y4)) or ((self.x1 == self.x2) and (self.x3 == self.x4)):
            self.can_continue = 1
            print('Такая трапеция существует')
        else:
            self.can_continue = 0
            print('Такой трапеции не существует')

    def check_sides(self):
        if self.can_continue == 1:
            a = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
            b = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
            c = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
            d = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
            if a == c or b == d:
                print('Трапеция равнобокая')
            else:
                print('Трапеция неравнобокая')
        else:
            print('Отказ. Действие с несуществующей трапецией')

    def sides(self):
        if self.can_continue == 1:
            a = round((math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))), 2)
            b = round((math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))), 2)
            c = round((math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))), 2)
            d = round((math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))), 2)
            print(f'Длина сторон: \nAB: {a} \nBC: {b} \nCD: {c} \nAD: {d}')
        else:
            print('Отказ. Действие с несуществующей трапецией')

    def perim(self):
        if self.can_continue == 1:
            a = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
            b = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
            c = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
            d = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
            P = round((a + b + c + d), 2)
            print('Периметр: ', P)
        else:
            print('Отказ. Действие с несуществующей трапецией')

    def area(self):
        if self.can_continue == 1:
            a = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
            b = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
            c = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
            d = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
            h = math.sqrt((a**2)-((((d-b)**2)+(a**2)-(c**2))/(2*(d-b)))**2)
            S = round(((b+d)/2) * h, 2)
            print('Площадь: ', S)
        else:
            print('Отказ. Действие с несуществующей трапецией')

trap = Trapeze(0,0,3,3,5,3,8,0)
trap.check_existence()
trap.check_sides()
trap.sides()
trap.perim()
trap.area()
trap1 = Trapeze(0,1,3,6,6,3,7,0)
trap1.check_existence()
trap1.check_sides()
trap1.sides()
trap1.perim()
trap1.area()