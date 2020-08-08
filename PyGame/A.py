import pygame as pyg
#инициализация pygame
pyg.init()

w, n = map(int, input().split())
size_p = int(w / n)
size = (w, w)
#инициализруем окно
screen = pyg.display.set_mode(size)
cnt = 0
color_black = (0, 0, 0)
color_white = (255, 255, 255)
#главный кусок программы где мы из отрисовываем, и задаем им цвет
for i in range(n):
    for j in range(n):
        if cnt % 2 == 0:
           pyg.draw.rect(screen, color_white, [i * size_p, j * size_p, size_p, size_p])
        else:
            pyg.draw.rect(screen, color_black, [i * size_p, j * size_p, size_p, size_p])
        cnt += 1
    cnt -= 1

#отрисовка кадра
pyg.display.flip()
#ожидание закрытия окна
while pyg.event.wait().type != pyg.QUIT:
    pass
# завершение работы
pyg.quit()