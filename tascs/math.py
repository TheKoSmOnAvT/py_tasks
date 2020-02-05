from random import randint

class SearchPoint():
    def __init__(self, w, h):
        self.__x = randint(0, w)
        self.__y = randint(0, h)
    def where_is_point(self, x, y):
        pos_x = pos_y = ''
        if x > self.__x:
            pos_x = 'L'
        elif x < self.__x:
            pos_x = 'R'
        if y > self.__y:
            pos_y = 'D'
        elif y < self.__y:
            pos_y = 'U'
        return pos_x + pos_y
    def what_is_point(self):
        print("Рандомная точка:({0},{1})".format(self.__x,self.__y))

if __name__ == '__main__':
    w, h = map(int, input().split())        #ширина и высота сетки
    x, y = map(int, input().split())        #стартовая точка
    SP = SearchPoint(w, h)                  #Создание точки
    position = SP.where_is_point(x, y)      #сравнение текущей точки(x,y) с искомой
    while(position!=''):
        for i in position:
            x = x - 1 if i == 'L' else x
            x = x + 1 if i == 'R' else x
            y = y + 1 if i == 'U' else y
            y = y - 1 if i == 'D' else y
        print(x, y)
        position = SP.where_is_point(x, y)
    print("Искомая точка:({0},{1})".format( x, y))
    SP.what_is_point()