import pygame as pyg
import math

# инициализация 
pyg.init()

# размеры окна
w, h = 1000, 1000
size = (w, h)
rad = 200

# scr — холст, на котором мы делаем отрисовку
scr = pyg.display.set_mode(size)

# отрисовка круга
points_multi = []
for i in range(1,361):
    x = int(math.cos(math.radians(i)) * rad) + h//2
    y = int(math.sin(math.radians(i)) * rad) + h//2
    points_multi.append((x,y))

#переменные для основного куска программы
mult = 2 #значение на которое мы будем каждый раз умножать, чтобы получить тапблицу
draw = True
running = True
push = False
color = pyg.Color(100, 200, 100)
hcolor = color.hsva

# ожидание закрытия окна
while running:
    for event in pyg.event.get():
        #изначально наше состояние кнопки = false, так как мы на нее даже не нажимали
        push = False
        
        #когда выходим прекращаем работу программы
        if event.type == pyg.QUIT:
            running = False
        
        #если мы нажали на пробел, то мы останавливаем отрисовку(ставим ена паузу), данным занчением у нас выступает перменная print
        if event.type == pyg.KEYDOWN and event.key == pyg.K_SPACE and draw and not push:
            push = True
            draw = False
        
        #если мы опять нажмем на пробел, то мы уберем паузу и возобновим работу нашей программы
        if event.type == pyg.KEYDOWN and event.key == pyg.K_SPACE and not draw and not push:
            push = True
            draw = True
    
    #изначально у нас значение равно = true, так как мы не надималь на пробел
    if draw:
        hcolor = ((hcolor[0] + 0.3) % 256,  hcolor[1],  hcolor[2],  hcolor[3])
        scr.fill((0, 0, 0))
        
        #рисуем линью от одной точки в другую
        for i in range(360):
            pyg.draw.aaline(scr, hcolor, points_multi[i], points_multi[(round(i * mult)) % 360])
        
        pyg.draw.circle(scr, hcolor, (w // 2, h // 2), rad, 1)
        pyg.display.flip()
        mult += 0.01
pyg.quit()