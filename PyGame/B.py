import pygame as pyg

#инициализируем размер окна
pyg.init()
w, h = 300, 200
size = (w, h)

#размер квадрата
x, y, sz = 0, 0, 75

#экран на котром будет происзодить отрисовка
scr = pyg.display.set_mode(size)

#отрисовка квадрата
pyg.draw.rect(scr, (0, 0, 255), (x, y, sz, sz))
pyg.display.flip()

running = True
can_move = False
while running:
    for event in pyg.event.get():
        #нормальное закрытие окна если нажать на крестик или alt+f4
        if event.type == pyg.QUIT:
            running = False
        
        #если мы нажили левую кнопку мышии и у нас позиция изменилась ставим can_move = true, потому что сделали движение
        if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
            if x < event.pos[0] < x + sz and y < event.pos[1] < y + sz:
                can_move = True
        
        #если мы двигаем мышь и при этом удерживаем левую клавишу мыши, то изменяем положение координат
        if event.type == pyg.MOUSEMOTION and event.buttons[0] and can_move:
            dx, dy = event.rel[0], event.rel[1]
            x += dx
            y += dy
        
        #если мы если мы подняли палец с левой клавиши мыши, то куб не двигается
        if event.type == pyg.MOUSEBUTTONUP and event.button == 1:
            can_move = False
    
    #темный экран (задний фон)
    scr.fill((0, 0, 0))
    #нарисовали квадрат на новом месте, теперь уже с этого места начнется стартовая точка
    pyg.draw.rect(scr, (0, 0, 255), (x, y, sz, sz))
    pyg.display.flip()
# завершение работы
pyg.quit()