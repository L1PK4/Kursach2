import pygame ## Подключение пакета пайгейм

## Функция сигнума ##
def sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0
######################

## Инициализация пакетов пайгейм и объявление окна ##
pygame.init()
ui = pygame.display.set_mode( (1000, 1000))
######################################################


## Рекурсивная функция, задающая код кривой ##
def code(code_):
    if int(code_) == 0:
        return [1]
    else:
        c = code(int(code_) - 1)
        c += [1] + c
        c[ len(c) - len(c) // 4 - 1] = 0
        return c
##############################################

## Класс кривой ##
class curve(object):

    ## Массив точек и задержка рисования ##
    points = []
    delay = 10
    ########################################

    ## Инициализация кривой ##
    def __init__(self, points_):
        self.points = points_
    ##########################

    ## Функция меняющая задержку ##
    def change_delay(self, d):
        if self.delay + d > 0:
            self.delay += d
        else:
            self.delay = 0
    ################################


    ## Функция рисования до номера поворота ##
    def draw_n(self, a):
        pygame.time.delay(self.delay)
        pygame.draw.line(ui,(0,0,0),self.points[a],self.points[a+1])
    ##########################################

    ## Функция кодировки координат из кода поворотов ##
    def encode(self, n):
        i = 1
        for c in code(n - 1):
            dx = self.points[i][0] - self.points[i - 1][0]
            dy = self.points[i][1] - self.points[i - 1][1]
            if c == 1:
                self.points.append((self.points[i][0] + 3 * sign(dy), self.points[i][1] + 3 * sign(dx)))
            else:
                self.points.append((self.points[i][0] - 3 * sign(dy), self.points[i][1] - 3 * sign(dx)))
            i += 1
    ####################################################


    ## Функция рисования до порядка ##
    def draw_p(self,n):
        self.points = []
        self.encode(n)
        pygame.time.delay(self.delay)
        for i in len(points):
            pygame.draw.line(ui,(0,0,0),self.points[i],self.points[i+1])
    ##################################

## Основная функция ##
def main():
    dSpeed = 0                                                                      ## Изменение задержки
    running = True                                                                  ## Проверка работы программы
    i = 1                                                                           ## Номер
    cu = curve([(500,500), (500,495)])                                              ## Инициализация кривой
    cu.encode(17)                                                                   ## Кодировка
    ui.fill((255,255,255))                                                          ## Заливка
    font=pygame.font.SysFont("arial",16)                                            ## Объявление шрифта


    while running:                                                                  ## Цикл работы программы
        for event in pygame.event.get():                                            ##Обработка событий
            if event.type == pygame.QUIT:                                           ##Если закрывается окно - выкл программа
                running = False
            ## Функции рестарта и ускорения ##
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = 1
                    ui.fill((255,255,255))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dSpeed = +2
                elif event.key == pygame.K_RIGHT:
                    dSpeed = -2
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                    dSpeed = 0
            ####################################


        text = font.render("Delay = %d"%cu.delay,1,(10,10,10),(255,255,255))        ## Инициализация текста
        ui.blit(text,(0,0))                                                         ## Наложение текста
        cu.change_delay(dSpeed)                                                     ## Смена задержки
        cu.draw_n(i)                                                                ## рисование отрезка
        pygame.display.update()                                                     ## обновление экрана
        i += 1                                                                      ## следующий шаг

## Запуск программы если запускается только сам скрипт ##
if __name__ == "__main__":
    main()
#########################################################
