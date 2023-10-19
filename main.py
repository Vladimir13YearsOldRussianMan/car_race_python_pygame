import pygame as pg
from random import randrange
from time import sleep

pg.init()

BGCOLOR = (100,100,100)

mw = pg.display.set_mode((500, 500))
mw.fill(BGCOLOR)

clock = pg.time.Clock()

class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color = None):
        self.rect = pg.Rect(x, y, width, height)
        self.color = (20, 20, 20)
        if color:
            self.color = color

    def new_color(self, color):
        self.color = color

    def fill(self):
        pg.draw.rect(mw, self.color, self.rect)
        
    def border(self, color, width):
        pg.draw.rect(mw, color, self.rect, width)

    def collide_point(self, x, y):
        return self.rect.collidepoint(x, y)

class Picture(Area):
    def __init__(self, file_name, x=0, y=0, width=10, height=10, color = (255,255,255)):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=color)
        self.image = pg.image.load(file_name)
    def draw(self, shift_x=0, shift_y=0):
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def change_image(self, file_name):
        self.image = pg.image.load(file_name)

class Label(Area):
    def setText(self, text='', size=35, tColor = (0,0,0)):
        self.image = pg.font.SysFont('verdana', size).render(text, True, tColor)

    def draw(self, shift_x = 0, shift_y = 0):
        pg.draw.rect(mw, self.color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

car = Picture('pngegg.png',50, 250, 45, 80, BGCOLOR)
car.image = pg.transform.scale(car.image, (95, 95))
car.move_right = False
car.move_left = False

line1 = Area(48, 100, 5, 100, (255,255,255))
line2 = Area(48, 350, 5, 100, (255,255,255))
line3 = Area(98, 100, 5, 100, (255,255,255))
line4 = Area(98, 350, 5, 100, (255,255,255))
line5 = Area(148, 100, 5, 100, (255,255,255))
line6 = Area(148, 350, 5, 100, (255,255,255))

lines = []
lines.append(line1)
lines.append(line2)
lines.append(line3)
lines.append(line4)
lines.append(line5)
lines.append(line6)

bomb1 = Picture('pngbomb.png',randrange(10,210, 50), 150-500, 35, 35,(BGCOLOR))
bomb2 = Picture('pngbomb.png',randrange(10,210, 50), 150-500, 35,35,(BGCOLOR))
bomb3 = Picture('pngbomb.png',randrange(10,210, 50), 400-500, 35,35,(BGCOLOR))
bomb4 = Picture('pngbomb.png',randrange(10,210, 50), 400-500, 35,35,(BGCOLOR))

bomb1.image = pg.transform.scale(bomb1.image, (70, 70))
bomb2.image = pg.transform.scale(bomb2.image, (70, 70))
bomb3.image = pg.transform.scale(bomb3.image, (70, 70))
bomb4.image = pg.transform.scale(bomb4.image, (70, 70))

bes = []
bes.append(bomb1)
bes.append(bomb2)
bes.append(bomb3)
bes.append(bomb4)

coin = Area(randrange(5, 205, 50), 100, 45, 45, (255, 220, 0))

print_score = Label(0,0,0,0,BGCOLOR)
b_start = Label(180, 290, 140, 40, (50,255,50))
b_start.setText('начать игру', 34)
b_leave = Label(180, 110, 140, 40, (255,50,50))
b_leave.setText('покинуть игру',28)
print_game_over = Label(0,0,0,0,BGCOLOR)

b_difficult = Label(180, 230, 140, 40, (250, 250, 50))
b_difficult.setText('сложность', 35)
info = 1
run = True
b_easy = Label(30, 230, 140, 40, (50, 255, 50))
b_easy.setText('лёгкая', 35)
b_normal = Label(180, 230, 140, 40, (250, 250, 50))
b_normal.setText('средняя',35)
b_hard = Label(330, 230, 140, 40, (255, 50, 50))
b_hard.setText('сложная',35)
b_shop = Label(180,170, 140, 40, (250,50,230))
b_shop.setText('магазин',35)
speed = 5
score = 0
b_cost1 = Label(100-80, 150-60, 140, 40, (150, 150, 50))
b_cost1.setText('выбранно',35)
b_cost1.chosen = True

b_cost2 = Label(100-80,210-60,140,40, (200,200,50))
b_cost2.setText('20 монеток', 35)
b_cost2.bought = False
b_cost2.chosen = False

b_cost3 = Label(100-80,270-60,140,40, (200,200,50))
b_cost3.setText('20 монеток', 35)
b_cost3.bought = False
b_cost3.chosen = False

b_cost4 = Label(100-80,330-60,140,40, (200,200,50))
b_cost4.setText('20 монеток', 35)
b_cost4.bought = False
b_cost4.chosen = False

b_cost5 = Label(100-80,390-60,140,40, (200,200,50))
b_cost5.setText('20 монеток', 35)
b_cost5.bought = False
b_cost5.chosen = False

b_cost6 = Label(100-80,450-60,140,40, (200,200,50))
b_cost6.setText('20 монеток', 35)
b_cost6.bought = False
b_cost6.chosen = False

esc = Label(20, 20, 25, 25, (230,0,0))
esc.setText('<',40, (255,255,255))
car_type = 1
car_exemple = Picture('pngegg.png',0-80,0+350,0,0,(BGCOLOR))
car_exemple.image = pg.transform.scale(car_exemple.image, (95, 95))
car_exemple.image = pg.transform.rotate(car_exemple.image, 90)

car_exemple2 = Picture('car1.png',0-80,0+338,0,0,(BGCOLOR))
car_exemple2.image = pg.transform.scale(car_exemple2.image, (115, 100))
car_exemple2.image = pg.transform.rotate(car_exemple2.image, 90)

car_exemple3 = Picture('car6.png',0-80,0+345-95,0,0,(BGCOLOR))
car_exemple3.image = pg.transform.scale(car_exemple3.image, (200, 180))
car_exemple3.image = pg.transform.rotate(car_exemple3.image, 90)

car_exemple4 = Picture('car7.png',0-80,0+345,0,0,(BGCOLOR))
car_exemple4.image = pg.transform.scale(car_exemple4.image, (100, 100))
car_exemple4.image = pg.transform.rotate(car_exemple4.image, 90)

car_exemple5 = Picture('car8.png',0-80,0+345,0,0,(BGCOLOR))
car_exemple5.image = pg.transform.scale(car_exemple5.image, (100, 100))
car_exemple5.image = pg.transform.rotate(car_exemple5.image, 90)

car_exemple6 = Picture('car9.png',0-80,0+345,0,0,(BGCOLOR))
car_exemple6.image = pg.transform.scale(car_exemple6.image, (100, 100))
car_exemple6.image = pg.transform.rotate(car_exemple6.image, 90)

luci = Picture('luci2.png', 0,-1000, 0,0, (BGCOLOR))
luci.image = pg.transform.scale(luci.image, (100, 100))
luci.draw(200, 0)



while run:
    mw.fill(BGCOLOR)
    b_start.draw(5,5) if info == 1 else b_start.draw(20, 5)
    b_start.border((0,0,0), 3)
    b_leave.draw(3,10)
    b_leave.border((0,0,0),3)
    b_difficult.draw(5,5)
    b_difficult.border((0,0,0),3)
    b_shop.draw(15,6)
    b_shop.border((0,0,0), 3)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if b_shop.collide_point(x,y):
                b_shop.new_color((150,50,130))
                b_shop.draw(15,6)
                b_shop.border((0,0,0),3)
                pg.display.update()
                sleep(0.1)
                b_shop.new_color((250,50,230))
                b_shop.draw(15,6)
                b_shop.border((0,0,0),3)
                pg.display.update()
                sleep(0.1)
                Break = True
                luci.image = pg.image.load('luci1.png')
                luci.image = pg.transform.scale(luci.image, (100, 100))
                luci.rect.y = 0
                while Break:
                    mw.fill(BGCOLOR) #!!!!!!!!!!!!!!!
                    print_score.setText(f'баланс: {score}',40)
                    esc.draw()
                    esc.border((0,0,0),3)
                    print_score.draw(100, 50)
                    car_exemple.draw(250, -285)
                    car_exemple2.draw(250, -220)
                    car_exemple3.draw(210, -115)
                    car_exemple4.draw(250, -100)
                    car_exemple5.draw(250, -53)
                    car_exemple6.draw(250, 16)
                    luci.draw(400)
                    
                    b_cost1.draw(5,5)
                    b_cost1.border((0,0,0),3)
                    b_cost2.draw(5,5)
                    b_cost2.border((0,0,0),3)
                    b_cost3.draw(5,5)
                    b_cost3.border((0,0,0),3)
                    b_cost4.draw(5,5)
                    b_cost4.border((0,0,0),3)
                    b_cost5.draw(5,5)
                    b_cost5.border((0,0,0),3)
                    b_cost6.draw(5,5)
                    b_cost6.border((0,0,0),3)
                    for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                            x,y = event.pos
                            if esc.collide_point(x,y):
                                esc.new_color((150,0,0))
                                esc.draw()
                                esc.border((0,0,0),3)
                                pg.display.update()
                                sleep(0.1)
                                esc.new_color((230,0,0))
                                esc.draw()
                                esc.border((0,0,0),3)
                                pg.display.update()
                                sleep(0.1)
                                Break = False
                                break
                            if b_cost1.collide_point(x,y):
                                if b_cost1.chosen != True:
                                    b_cost1.chosen = True
                                    b_cost2.chosen = False
                                    b_cost3.chosen = False
                                    b_cost4.chosen = False
                                    b_cost5.chosen = False
                                    b_cost6.chosen = False
                                    b_cost1.new_color((150,150,50))
                                    b_cost1.setText('выбрано',35)
                                    b_cost1.draw(5,5)
                                    b_cost1.border((0,0,0), 3)
                                    b_cost2.setText('выбрать',35)
                                    b_cost2.new_color((200,200,50))
                                    b_cost2.draw(5,5)
                                    b_cost2.border((0,0,0),3)
                                    car_exemple.draw(250, -285)
                                    car_exemple2.draw(250, -220)
                                    car_exemple3.draw(210, -115)
                                    car_exemple4.draw(250, -100)
                                    car_exemple5.draw(250, -53)
                                    car_exemple6.draw(250, 16)
                                    
                                    b_cost1.draw(5,5)
                                    b_cost1.border((0,0,0),3)
                                    b_cost2.draw(5,5)
                                    b_cost2.border((0,0,0),3)
                                    b_cost3.draw(5,5)
                                    b_cost3.border((0,0,0),3)
                                    b_cost4.draw(5,5)
                                    b_cost4.border((0,0,0),3)   
                                    b_cost5.draw(5,5)
                                    b_cost5.border((0,0,0),3)   
                                    b_cost6.draw(5,5)
                                    b_cost6.border((0,0,0),3)   
                                    car_type = 1
                                    car.image = pg.image.load('pngegg.png')
                                    print_score.setText(f'баланс: {score}',40)
                                    print_score.draw(100, 50)
                                    pg.display.update()
                                    sleep(2)
                                    
                            if b_cost2.collide_point(x,y):
                                if b_cost2.bought == False:
                                    if score < 20:
                                        mw.fill(BGCOLOR)
                                        print_score.setText('недостаточно средств',35)
                                        print_score.draw(90,50)
                                        pg.display.update()
                                        sleep(2)
                                        break
                                    else:
                                        score -= 20
                                        mw.fill(BGCOLOR)
                                        b_cost2.bought = True
                                        b_cost2.chosen = True
                                        b_cost1.chosen = False
                                        b_cost3.chosen = False
                                        b_cost4.chosen = False
                                        b_cost5.chosen = False
                                        b_cost6.chosen = False
                                        b_cost2.new_color((150,150,50))
                                        b_cost2.setText('выбрано',35)
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0), 3)
                                        b_cost1.setText('выбрать',35)
                                        b_cost1.new_color((200,200,50))
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        car_exemple.draw(250, -285)
                                        car_exemple2.draw(250, -220)
                                        car_exemple3.draw(210, -115)
                                        car_exemple4.draw(250, -100)
                                        car_exemple5.draw(250, -53)
                                        car_exemple6.draw(250, 16)
                                        
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0),3)
                                        b_cost4.draw(5,5)
                                        b_cost4.border((0,0,0),3)
                                        b_cost5.draw(5,5)
                                        b_cost5.border((0,0,0),3)
                                        b_cost6.draw(5,5)
                                        b_cost6.border((0,0,0),3)
                                        car_type = 2
                                        car.image = pg.image.load('pngegg1.png')
                                        print_score.setText(f'баланс: {score}',40)
                                        print_score.draw(100, 50)
                                        esc.draw()
                                        esc.border((0,0,0),3)
                                        pg.display.update()
                                    sleep(2)
                                    
                                
                                if b_cost2.bought == True and b_cost2.chosen == False:
                                    b_cost2.chosen = True
                                    b_cost1.chosen = False
                                    b_cost3.chosen = False
                                    b_cost4.chosen = False
                                    b_cost5.chosen = False
                                    b_cost6.chosen = False
                                    b_cost2.new_color((150,150,50))
                                    b_cost2.setText('выбрано',35)
                                    b_cost2.draw(5,5)
                                    b_cost2.border((0,0,0), 3)
                                    car_exemple.draw(250, -285)
                                    car_exemple2.draw(250, -220)
                                    car_exemple3.draw(210, -115)
                                    car_exemple4.draw(250, -100)
                                    car_exemple5.draw(250, -53)
                                    car_exemple6.draw(250, 16)
                                    
                                    b_cost1.draw(5,5)
                                    b_cost1.border((0,0,0),3)
                                    b_cost2.draw(5,5)
                                    b_cost2.border((0,0,0),3)
                                    b_cost3.draw(5,5)
                                    b_cost3.border((0,0,0),3)
                                    b_cost4.draw(5,5)
                                    b_cost4.border((0,0,0),3)
                                    b_cost5.draw(5,5)
                                    b_cost5.border((0,0,0),3)
                                    b_cost6.draw(5,5)
                                    b_cost6.border((0,0,0),3)
                                    car_type = 2
                                    car.image = pg.image.load('pngegg1.png')
                                    print_score.setText(f'баланс: {score}',40)
                                    print_score.draw(100, 50)
                                    pg.display.update()
                                    sleep(2)

                            if b_cost3.collide_point(x,y):
                                if b_cost3.bought == False:
                                    if score < 20:
                                        mw.fill(BGCOLOR)
                                        print_score.setText('недостаточно средств',35)
                                        print_score.draw(90,50)
                                        pg.display.update()
                                        sleep(2)
                                        break
                                    else:
                                        score -= 20
                                        mw.fill(BGCOLOR)
                                        b_cost3.bought = True
                                        b_cost3.chosen = True
                                        b_cost1.chosen = False
                                        b_cost2.chosen = False
                                        b_cost4.chosen = False
                                        b_cost5.chosen = False
                                        b_cost6.chosen = False
                                        b_cost3.new_color((150,150,50))
                                        b_cost3.setText('выбрано',35)
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0), 3)
                                        b_cost1.setText('выбрать',35)
                                        b_cost1.new_color((200,200,50))
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.setText('выбрать',35) if b_cost2.bought == True else None
                                        b_cost2.new_color((200,200,50))
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        car_exemple.draw(250, -285)
                                        car_exemple2.draw(250, -220)
                                        car_exemple3.draw(210, -115)
                                        car_exemple4.draw(250, -100)
                                        car_exemple5.draw(250, -53)
                                        car_exemple6.draw(250, 16)
                                        
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0),3)
                                        b_cost4.draw(5,5)
                                        b_cost4.border((0,0,0),3)
                                        b_cost5.draw(5,5)
                                        b_cost5.border((0,0,0),3)
                                        b_cost6.draw(5,5)
                                        b_cost6.border((0,0,0),3)
                                        car_type = 3
                                        car.image = pg.image.load('car6.png')
                                        print_score.setText(f'баланс: {score}',40)
                                        print_score.draw(100, 50)
                                        esc.draw()
                                        esc.border((0,0,0),3)
                                        pg.display.update()
                                    sleep(2)
                                    
                                
                                if b_cost3.bought == True and b_cost2.chosen == False:
                                    b_cost3.chosen = True
                                    b_cost1.chosen = False
                                    b_cost2.chosen = False
                                    b_cost4.chosen = False
                                    b_cost5.chosen = False
                                    b_cost6.chosen = False
                                    b_cost3.new_color((150,150,50))
                                    b_cost3.setText('выбрано',35)
                                    b_cost3.draw(5,5)
                                    b_cost3.border((0,0,0), 3)
                                    car_exemple.draw(250, -285)
                                    car_exemple2.draw(250, -220)
                                    car_exemple3.draw(210, -115)
                                    car_exemple4.draw(250, -100)
                                    car_exemple5.draw(250, -53)
                                    car_exemple6.draw(250, 16)
                                    
                                    b_cost1.draw(5,5)
                                    b_cost1.border((0,0,0),3)
                                    b_cost2.draw(5,5)
                                    b_cost2.border((0,0,0),3)
                                    b_cost3.draw(5,5)
                                    b_cost3.border((0,0,0),3)
                                    b_cost4.draw(5,5)
                                    b_cost4.border((0,0,0),3)
                                    b_cost5.draw(5,5)
                                    b_cost5.border((0,0,0),3)
                                    b_cost6.draw(5,5)
                                    b_cost6.border((0,0,0),3)
                                    car_type = 3
                                    car.image = pg.image.load('car6.png')
                                    print_score.setText(f'баланс: {score}',40)
                                    print_score.draw(100, 50)
                                    pg.display.update()
                                    sleep(2)

                            if b_cost4.collide_point(x,y):
                                if b_cost4.bought == False:
                                    if score < 20:
                                        mw.fill(BGCOLOR)
                                        print_score.setText('недостаточно средств',35)
                                        print_score.draw(90,50)
                                        pg.display.update()
                                        sleep(2)
                                        break
                                    else:
                                        score -= 20
                                        mw.fill(BGCOLOR)
                                        b_cost4.bought = True
                                        b_cost4.chosen = True
                                        b_cost1.chosen = False
                                        b_cost2.chosen = False
                                        b_cost3.chosen = False
                                        b_cost5.chosen = False
                                        b_cost6.chosen = False
                                        b_cost4.new_color((150,150,50))
                                        b_cost4.setText('выбрано',35)
                                        b_cost4.draw(5,5)
                                        b_cost4.border((0,0,0), 3)
                                        b_cost1.setText('выбрать',35)
                                        b_cost1.new_color((200,200,50))
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.setText('выбрать',35) if b_cost2.bought == True else None
                                        b_cost2.new_color((200,200,50))
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        b_cost3.setText('выбрать',35) if b_cost3.bought == True else None
                                        b_cost3.new_color((200,200,50))
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0),3)
                                        car_exemple.draw(250, -285)
                                        car_exemple2.draw(250, -220)
                                        car_exemple3.draw(210, -115)
                                        car_exemple4.draw(250, -100)
                                        car_exemple5.draw(250, -53)
                                        car_exemple6.draw(250, 16)
                                        
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0),3)
                                        b_cost4.draw(5,5)
                                        b_cost4.border((0,0,0),3)
                                        b_cost5.draw(5,5)
                                        b_cost5.border((0,0,0),3)
                                        b_cost6.draw(5,5)
                                        b_cost6.border((0,0,0),3)
                                        car_type = 4
                                        car.image = pg.image.load('car7.png')
                                        print_score.setText(f'баланс: {score}',40)
                                        print_score.draw(100, 50)
                                        esc.draw()
                                        esc.border((0,0,0),3)
                                        pg.display.update()
                                    sleep(2)
                                    
                                
                                if b_cost4.bought == True and b_cost4.chosen == False:
                                    b_cost4.chosen = True
                                    b_cost1.chosen = False
                                    b_cost2.chosen = False
                                    b_cost3.chosen = False
                                    b_cost5.chosen = False
                                    b_cost6.chosen = False
                                    b_cost4.new_color((150,150,50))
                                    b_cost4.setText('выбрано',35)
                                    b_cost4.draw(5,5)
                                    b_cost4.border((0,0,0), 3)
                                    car_exemple.draw(250, -285)
                                    car_exemple2.draw(250, -220)
                                    car_exemple3.draw(210, -115)
                                    car_exemple4.draw(250, -100)
                                    car_exemple5.draw(250, -53)
                                    car_exemple6.draw(250, 16)
                                    
                                    b_cost1.draw(5,5)
                                    b_cost1.border((0,0,0),3)
                                    b_cost2.draw(5,5)
                                    b_cost2.border((0,0,0),3)
                                    b_cost3.draw(5,5)
                                    b_cost3.border((0,0,0),3)
                                    b_cost4.draw(5,5)
                                    b_cost4.border((0,0,0),3)
                                    b_cost5.draw(5,5)
                                    b_cost5.border((0,0,0),3)
                                    b_cost6.draw(5,5)
                                    b_cost6.border((0,0,0),3)
                                    car_type = 4
                                    car.image = pg.image.load('car7.png')
                                    print_score.setText(f'баланс: {score}',40)
                                    print_score.draw(100, 50)
                                    pg.display.update()
                                    sleep(2)

                            if b_cost5.collide_point(x,y):
                                if b_cost5.bought == False:
                                    if score < 20:
                                        mw.fill(BGCOLOR)
                                        print_score.setText('недостаточно средств',35)
                                        print_score.draw(90,50)
                                        pg.display.update()
                                        sleep(2)
                                        break
                                    else:
                                        score -= 20
                                        mw.fill(BGCOLOR)
                                        b_cost5.bought = True
                                        b_cost5.chosen = True
                                        b_cost1.chosen = False
                                        b_cost2.chosen = False
                                        b_cost3.chosen = False
                                        b_cost4.chosen = False
                                        b_cost6.chosen = False
                                        b_cost5.new_color((150,150,50))
                                        b_cost5.setText('выбрано',35)
                                        b_cost5.draw(5,5)
                                        b_cost5.border((0,0,0), 3)
                                        b_cost1.setText('выбрать',35)
                                        b_cost1.new_color((200,200,50))
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.setText('выбрать',35) if b_cost2.bought == True else None
                                        b_cost2.new_color((200,200,50))
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        b_cost3.setText('выбрать',35) if b_cost3.bought == True else None
                                        b_cost3.new_color((200,200,50))
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0),3)
                                        car_exemple.draw(250, -285)
                                        car_exemple2.draw(250, -220)
                                        car_exemple3.draw(210, -115)
                                        car_exemple4.draw(250, -100)
                                        car_exemple5.draw(250, -53)
                                        car_exemple6.draw(250, 16)
                                        
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0),3)
                                        b_cost4.draw(5,5)
                                        b_cost4.border((0,0,0),3)
                                        b_cost5.draw(5,5)
                                        b_cost5.border((0,0,0),3)
                                        b_cost6.draw(5,5)
                                        b_cost6.border((0,0,0),3)
                                        car_type = 5
                                        car.image = pg.image.load('car8.png')
                                        print_score.setText(f'баланс: {score}',40)
                                        print_score.draw(100, 50)
                                        esc.draw()
                                        esc.border((0,0,0),3)
                                        pg.display.update()
                                    sleep(2)
                                    
                                
                                if b_cost5.bought == True and b_cost4.chosen == False:
                                    b_cost5.chosen = True
                                    b_cost1.chosen = False
                                    b_cost2.chosen = False
                                    b_cost3.chosen = False
                                    b_cost4.chosen = False
                                    b_cost6.chosen = False
                                    b_cost5.new_color((150,150,50))
                                    b_cost5.setText('выбрано',35)
                                    b_cost5.draw(5,5)
                                    b_cost5.border((0,0,0), 3)
                                    car_exemple.draw(250, -285)
                                    car_exemple2.draw(250, -220)
                                    car_exemple3.draw(210, -115)
                                    car_exemple4.draw(250, -100)
                                    car_exemple5.draw(250, -53)
                                    car_exemple6.draw(250, 16)
                                    
                                    b_cost1.draw(5,5)
                                    b_cost1.border((0,0,0),3)
                                    b_cost2.draw(5,5)
                                    b_cost2.border((0,0,0),3)
                                    b_cost3.draw(5,5)
                                    b_cost3.border((0,0,0),3)
                                    b_cost4.draw(5,5)
                                    b_cost4.border((0,0,0),3)
                                    b_cost5.draw(5,5)
                                    b_cost5.border((0,0,0),3)
                                    b_cost6.draw(5,5)
                                    b_cost6.border((0,0,0),3)
                                    car_type = 5
                                    car.image = pg.image.load('car8.png')
                                    print_score.setText(f'баланс: {score}',40)
                                    print_score.draw(100, 50)
                                    pg.display.update()
                                    sleep(2)

                            if b_cost6.collide_point(x,y):
                                if b_cost6.bought == False:
                                    if score < 20:
                                        mw.fill(BGCOLOR)
                                        print_score.setText('недостаточно средств',35)
                                        print_score.draw(90,50)
                                        pg.display.update()
                                        sleep(2)
                                        break
                                    else:
                                        score -= 20
                                        mw.fill(BGCOLOR)
                                        b_cost6.bought = True
                                        b_cost6.chosen = True
                                        b_cost1.chosen = False
                                        b_cost2.chosen = False
                                        b_cost3.chosen = False
                                        b_cost4.chosen = False
                                        b_cost5.chosen = False
                                        b_cost6.new_color((150,150,50))
                                        b_cost6.setText('выбрано',35)
                                        b_cost6.draw(5,5)
                                        b_cost6.border((0,0,0), 3)
                                        b_cost1.setText('выбрать',35)
                                        b_cost1.new_color((200,200,50))
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.setText('выбрать',35) if b_cost2.bought == True else None
                                        b_cost2.new_color((200,200,50))
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        b_cost3.setText('выбрать',35) if b_cost3.bought == True else None
                                        b_cost3.new_color((200,200,50))
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0),3)
                                        car_exemple.draw(250, -285)
                                        car_exemple2.draw(250, -220)
                                        car_exemple3.draw(210, -115)
                                        car_exemple4.draw(250, -100)
                                        car_exemple5.draw(250, -53)
                                        car_exemple6.draw(250, 16)
                                        
                                        b_cost1.draw(5,5)
                                        b_cost1.border((0,0,0),3)
                                        b_cost2.draw(5,5)
                                        b_cost2.border((0,0,0),3)
                                        b_cost3.draw(5,5)
                                        b_cost3.border((0,0,0),3)
                                        b_cost4.draw(5,5)
                                        b_cost4.border((0,0,0),3)
                                        b_cost5.draw(5,5)
                                        b_cost5.border((0,0,0),3)
                                        b_cost6.draw(5,5)
                                        b_cost6.border((0,0,0),3)
                                        car_type = 6
                                        car.image = pg.image.load('car9.png')
                                        print_score.setText(f'баланс: {score}',40)
                                        print_score.draw(100, 50)
                                        esc.draw()
                                        esc.border((0,0,0),3)
                                        pg.display.update()
                                    sleep(2)
                                    
                                
                                if b_cost6.bought == True and b_cost4.chosen == False:
                                    b_cost6.chosen = True
                                    b_cost1.chosen = False
                                    b_cost2.chosen = False
                                    b_cost3.chosen = False
                                    b_cost4.chosen = False
                                    b_cost5.chosen = False
                                    b_cost6.new_color((150,150,50))
                                    b_cost6.setText('выбрано',35)
                                    b_cost6.draw(5,5)
                                    b_cost6.border((0,0,0), 3)
                                    car_exemple.draw(250, -285)
                                    car_exemple2.draw(250, -220)
                                    car_exemple3.draw(210, -115)
                                    car_exemple4.draw(250, -100)
                                    car_exemple5.draw(250, -53)
                                    car_exemple6.draw(250, 16)
                                    
                                    b_cost1.draw(5,5)
                                    b_cost1.border((0,0,0),3)
                                    b_cost2.draw(5,5)
                                    b_cost2.border((0,0,0),3)
                                    b_cost3.draw(5,5)
                                    b_cost3.border((0,0,0),3)
                                    b_cost4.draw(5,5)
                                    b_cost4.border((0,0,0),3)
                                    b_cost5.draw(5,5)
                                    b_cost5.border((0,0,0),3)
                                    b_cost6.draw(5,5)
                                    b_cost6.border((0,0,0),3)
                                    car_type = 6
                                    car.image = pg.image.load('car9.png')
                                    print_score.setText(f'баланс: {score}',40)
                                    print_score.draw(100, 50)
                                    pg.display.update()
                                    sleep(2)
                                    
                            
                    if b_cost1.chosen == False:
                        b_cost1.setText('выбрать',35)
                        b_cost1.new_color((200,200,50))
                    
                    if b_cost2.chosen == False and b_cost2.bought == True:
                        b_cost2.setText('выбрать',35)
                        b_cost2.new_color((200,200,50))

                    if b_cost3.chosen == False and b_cost3.bought == True:
                        b_cost3.setText('выбрать',35)
                        b_cost3.new_color((200,200,50))

                    if b_cost4.chosen == False and b_cost4.bought == True:
                        b_cost4.setText('выбрать',35)
                        b_cost4.new_color((200,200,50))

                    if b_cost5.chosen == False and b_cost5.bought == True:
                        b_cost5.setText('выбрать',35)
                        b_cost5.new_color((200,200,50))

                    if b_cost6.chosen == False and b_cost6.bought == True:
                        b_cost6.setText('выбрать',35)
                        b_cost6.new_color((200,200,50))

                    pg.display.update()
                    clock.tick(40)
            if b_difficult.collide_point(x,y):
                b_difficult.new_color((150,150,50))
                b_difficult.draw(5,5)
                b_difficult.border((0,0,0),3)
                pg.display.update()
                sleep(0.1)
                b_difficult.new_color((250,250,50))
                b_difficult.draw(5,5)
                b_difficult.border((0,0,0),3)
                pg.display.update()
                sleep(0.1)
                Break = True
                while Break:
                    mw.fill(BGCOLOR)
                    b_easy.draw(10,6)
                    b_easy.border((0,0,0),3)
                    b_normal.draw(10,6)
                    b_normal.border((0,0,0),3)
                    b_hard.draw(10,6)
                    b_hard.border((0,0,0),3)
                    for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #!
                            x,y = event.pos
                            if b_easy.collide_point(x,y):
                                b_easy.new_color((50,150,50))
                                b_easy.draw(10,6)
                                b_easy.border((0,0,0), 3)
                                pg.display.update()
                                sleep(0.1)
                                b_easy.new_color((50,255,50))
                                b_easy.draw(10,6) 
                                b_easy.border((0,0,0), 3)
                                pg.display.update()
                                sleep(0.1)

                                speed = 4
                                Break = False
                                break
                            if b_normal.collide_point(x,y):
                                b_normal.new_color((150,150,50))
                                b_normal.draw(10,6)
                                b_normal.border((0,0,0),3)
                                pg.display.update()
                                sleep(0.1)
                                b_normal.new_color((250,250,50))
                                b_normal.draw(10,6)
                                b_normal.border((0,0,0),3)
                                pg.display.update()
                                sleep(0.1)

                                speed = 7
                                Break = False
                                break
                            if b_hard.collide_point(x,y):
                                b_hard.new_color((150,50,50))
                                b_hard.draw(10,6)
                                b_hard.border((0,0,0),3)
                                pg.display.update()
                                sleep(0.1)
                                b_hard.new_color((255,50,50))
                                b_hard.draw(10,6)
                                b_hard.border((0,0,0),3)
                                pg.display.update()
                                sleep(0.1)

                                speed = 10
                                Break = False
                                break
                            


                    pg.display.update()
                    clock.tick(40)
            if b_leave.collide_point(x,y):
                b_leave.new_color((150,50,50))
                b_leave.draw(3,10)
                b_leave.border((0,0,0),3)
                pg.display.update()
                sleep(0.1)
                b_leave.new_color((255,50,50))
                b_leave.draw(3,10)
                b_leave.border((0,0,0),3)
                pg.display.update()
                sleep(0.1)
                run = False
                break
            if b_start.collide_point(x,y):
                b_start.new_color((50,150,50))
                b_start.draw(5,5) if info == 1 else b_start.draw(20, 5)
                b_start.border((0,0,0), 3)
                pg.display.update()
                sleep(0.1)
                b_start.new_color((50,255,50))
                b_start.draw(5,5) if info == 1 else b_start.draw(20, 5)
                b_start.border((0,0,0), 3)
                pg.display.update()
                sleep(0.1)
                
                if car_type == 1:
                    car.image = pg.image.load('pngegg.png')
                    car.image = pg.transform.scale(car.image, (95, 95))
                elif car_type == 2:
                    car.image = pg.image.load('car1.png')
                    car.image = pg.transform.scale(car.image, (115, 100))

                elif car_type == 3:
                    car.image = pg.image.load('car6.png')
                    car.image = pg.transform.scale(car.image, (200, 180))

                elif car_type == 4:
                    car.image = pg.image.load('car7.png')
                    car.image = pg.transform.scale(car.image, (100, 100))

                elif car_type == 5:
                    car.image = pg.image.load('car8.png')
                    car.image = pg.transform.scale(car.image, (100, 100))
                    
                elif car_type == 6:
                    car.image = pg.image.load('car9.png')
                    car.image = pg.transform.scale(car.image, (100, 100))


                car.move_right = False
                car.move_left = False

                bomb1.rect.y = 150-500
                bomb1.rect.x = randrange(5, 155, 50)
                bomb2.rect.y = 150-500
                bomb2.rect.x = randrange(5, 155, 50)
                bomb3.rect.y = 400-500
                bomb3.rect.x = randrange(5, 155, 50)
                bomb4.rect.y = 400-500
                bomb4.rect.x = randrange(5, 155, 50)
                
                luci.image = pg.image.load('luci1.png')
                luci.image = pg.transform.scale(luci.image, (100, 100))
                luci.rect.y = -2000
                info_luci = 2
                fps_amount = 0
                run = True
                while run:
                    mw.fill(BGCOLOR)
                    print_score.setText(f'монетки: {score}', 40, (255, 200, 0))
                    print_score.draw(220,10)
                    car.fill()
                    pg.draw.circle(mw, coin.color,(coin.rect.x+20, coin.rect.y+20), 15)
                    #pg.draw.circle(mw, (255, 150, 0),(coin.rect.x+20, coin.rect.y+20), 22, 15)
                    

                    

                    luci.rect.y += speed
                    luci.draw(200, 0)

                    for line in lines:
                        line.fill()
                    for b in bes:
                        b.draw(-13, -22)
                    pg.draw.line(mw, (255,200,0), (0, 0), (0, 500), 5)
                    pg.draw.line(mw, (255,200,0), (200, 0), (200, 500), 5)
                    if car_type == 1:
                        car.draw(-26)
                    elif car_type == 2:
                        car.draw(-35,-5)
                    elif car_type == 4:
                        car.draw(-32, -5)
                    elif car_type == 5:
                        car.draw(-16, -5)
                    elif car_type == 6:
                        car.draw(-28,-5)
                    else:
                        car.draw(-80,-55)
                    

                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_LEFT:
                                car.move_left = True
                            if event.key == pg.K_RIGHT:
                                car.move_right = True
                            # if event.key == pg.K_2:
                            #     score += 20
                        
                        if event.type == pg.KEYUP:
                            if event.key == pg.K_LEFT:
                                car.move_left = False
                            if event.key == pg.K_RIGHT:
                                car.move_right = False

                    if car.rect.colliderect(bomb1.rect) or car.rect.colliderect(bomb2.rect) or car.rect.colliderect(bomb3.rect) or car.rect.colliderect(bomb4.rect):
                        car.image = pg.image.load('pngburst.png')
                        car.image = pg.transform.scale(car.image, (70,70))

                        mw.fill(BGCOLOR)
                        for line in lines:
                            line.fill()
                        for b in bes:
                            if not b.rect.colliderect(car.rect):
                                b.draw(-5, -12)
                        pg.draw.circle(mw, coin.color,(coin.rect.x+20, coin.rect.y+20), 15)
                        pg.draw.line(mw, (255,200,0), (0, 0), (0, 500), 5)
                        pg.draw.line(mw, (255,200,0), (200, 0), (200, 500), 5)
                        car.draw(-26)
                        pg.display.update()
                        sleep(2)
                        break

                    line1.rect.y += speed
                    line2.rect.y += speed
                    line3.rect.y += speed
                    line4.rect.y += speed
                    line5.rect.y += speed
                    line6.rect.y += speed

                    bomb1.rect.y += speed
                    bomb2.rect.y += speed
                    bomb3.rect.y += speed
                    bomb4.rect.y += speed

                    coin.rect.y += speed

                    if coin.rect.y >= 600:
                        coin.rect.y = -200
                        coin.rect.x = randrange(5, 205, 50)
                        coin.new_color((255,220,0))

                    if car.rect.colliderect(coin.rect):
                        score = score + 1 if coin.color != BGCOLOR else score + 0
                        coin.new_color(BGCOLOR)


                    if bomb3.rect.y >= 480:
                        bomb3.rect.y, bomb4.rect.y = -20, -20
                        bomb3.rect.x, bomb4.rect.x = randrange(10, 210, 50), randrange(10, 210, 50)
                    if bomb1.rect.y >= 480:
                        bomb1.rect.y, bomb2.rect.y = -20, -20
                        bomb1.rect.x, bomb2.rect.x = randrange(10, 210, 50), randrange(10, 210, 50)

                    if line2.rect.y >= 450:
                        line2.rect.y, line4.rect.y, line6.rect.y = -50, -50, -50

                    if line1.rect.y >= 450:
                        line1.rect.y, line3.rect.y, line5.rect.y = -50, -50, -50

                    if car.rect.x >= 155:
                        car.move_right = False
                    if car.rect.x <= 0:
                        car.move_left = False

                    if car.move_right:
                        car.rect.x += speed 
                    if car.move_left:
                        car.rect.x -= speed 
                    
                    if luci.rect.y >= 600:
                        luci.rect.y = -5000
                        info_luci *= -1
                        if info_luci > 0:
                            luci.image = pg.image.load('luci2.png')
                        else:
                            luci.image = pg.image.load('luci1.png')

                        luci.image = pg.transform.scale(luci.image, (100, 100))

                    pg.display.update()
                    clock.tick(60)
                mw.fill(BGCOLOR)
                luci.image = pg.image.load('luci2.png')
                luci.image = pg.transform.scale(luci.image, (100, 100))
                luci.rect.y = 100
                luci.draw(250)
                print_game_over.setText('игра окончена',60, (255, 180, 50))
                print_score.setText(f'собрано монеток: {score}',50, (255, 180, 50))
                print_game_over.draw(100, 200)
                print_score.draw(100, 250)
                b_start.setText('заново', 40)
                pg.display.update()
                sleep(3)
                info = 2
    pg.display.update()
    clock.tick(40)


pg.quit()
