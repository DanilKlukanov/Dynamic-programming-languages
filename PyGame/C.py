import pygame as pyg

pyg.init()

scr = pyg.display.set_mode((1000, 1000))
x1, y1, w, h = 0, 0, 0, 0

pyg.display.flip()

drawing_ren_tan = []
running = True
drawing = False 
first_click = False

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        
        if event.type == pyg.MOUSEBUTTONDOWN and event.button == True and first_click:
            drawing = True  # включаем режим рисования
            #запоминаем координаты одного угла
            x1, y1 = event.pos
            w, h = 0, 0
            first_click = False
        
        if event.type == pyg.MOUSEBUTTONUP and event.button == True:
            #сохраняем нарисованное (на втором холсте)
            drawing_ren_tan.append((x1, y1, w, h))
            drawing = False
            first_click = True
        
        if event.type == pyg.MOUSEMOTION:
            #запоминаем текущие размеры
            w, h = event.pos[0] - x1, event.pos[1] - y1

        if event.type == pyg.KEYDOWN and event.mod == pyg.KMOD_LCTRL:
            if len(drawing_ren_tan):
                del drawing_ren_tan[len(drawing_ren_tan)-1]

    # рисуем на экране сохранённое на втором холсте
    scr.fill(pyg.Color('black'))
    
    if drawing:  # и, если надо, текущий прямоугольник
        pyg.draw.rect(scr, (0, 0, 255), ((x1, y1), (w, h)), 1)
    for coords in drawing_ren_tan:
        pyg.draw.rect(scr, (0, 0, 255), coords, 1)
    
    pyg.display.flip()