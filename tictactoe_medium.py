import tkinter
from random import choice
from tkinter import ttk

class Choice(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.result = None # 1 - крестики, 0 - нолики
        self.btn1 = ttk.Button(text='noughts', command=self.command1).place(x=15, y=50)
        self.btn2 = ttk.Button(text='crosses', command=self.command2).place(x=110, y=50)

    def command1(self):
        self.result = 0
        self.destroy()

    def command2(self):
        self.result = 1
        self.destroy()



class TicTacToe(tkinter.Canvas):
    def __init__(self, window, result):
        self.window = window
        self.result = result
        self.flag = 1 # флаг: 1 - игра идет, 0 - игра завершена
        self.canvas = super().__init__(window, width = 300, height = 300)
        self.state = [None] * 9 # массив ноликов
        self.bind('<Button-1>', self.click) # обрабатываем событие клика - вызываем функцию click()
        
        self.window.title('TicTacToe GAME')

    def player_1_move(self, x, y):
        if self.result == 1:
            self.add_x(x, y)
        else:
            self.add_o(x, y)
    
    def player_2_move(self, x, y):
        if self.result == 0:
            self.add_x(x, y)
        else:
            self.add_o(x, y)

    def click(self, event):
        x = event.x
        y = event.y
        if self.flag: # проверяем, закончилась ли игра
            if 0 < x < 100:
                if 0 < y < 100 and self.state[0] == None:
                    self.state[0] = self.result
                    self.player_1_move(0, 0)    
                    if self.get_winner() != None:
                        self.end()
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
                if 100 < y < 200 and self.state[3] == None:
                    self.state[3] = self.result
                    self.player_1_move(0, 1)
                    if self.get_winner() != None:
                        self.end()   
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
                if 200 < y < 300 and self.state[6] == None:
                    self.state[6] = self.result
                    self.player_1_move(0, 2)
                    if self.get_winner() != None:
                        self.end()   
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
            if 100 < x < 200:
                if 0 < y < 100 and self.state[1] == None:
                    self.state[1] = self.result
                    self.player_1_move(1, 0)
                    if self.get_winner() != None:
                        self.end()   
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
                if 100 < y < 200 and self.state[4] == None:
                    self.state[4] = self.result
                    self.player_1_move(1, 1)
                    if self.get_winner() != None:
                        self.end()   
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
                if 200 < y < 300 and self.state[7] == None:
                    self.state[7] = self.result
                    self.player_1_move(1, 2)
                    if self.get_winner() != None:
                        self.end()   
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
            if 200 < x < 300:
                if 0 < y < 100 and self.state[2] == None:
                    self.state[2] = self.result
                    self.player_1_move(2, 0)
                    if self.get_winner() != None:
                        self.end()   
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
                if 100 < y < 200 and self.state[5] == None:
                    self.state[5] = self.result
                    self.player_1_move(2, 1)
                    if self.get_winner() != None:
                        self.end()   
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
                if 200 < y < 300 and self.state[8] == None:
                    self.state[8] = self.result
                    self.player_1_move(2, 2)
                    if self.get_winner() != None:
                        self.end()   
                    else:   
                        self.bot_move()
                    if self.get_winner() != None:
                        self.end() 
                    
        else:
            # обработка окончания игры
            self.flag = 1
            self.delete("all")
            self.state = [None] * 9 
            self.draw_mesh()   
                                 

    def add_x(self, x, y):
        offset = 20
        self.create_line(offset + x * 100, offset + y * 100, 100 - offset + x * 100, 100 - offset + y * 100, fill='blue', width=7)
        self.create_line(offset + x * 100, 100 - offset + y * 100, 100 - offset + x * 100, offset + y * 100, fill='blue', width=7)

    def add_o(self, x, y):
        r = 35
        self.create_oval(100 * x + 50 - r, 100 * y + 50 - r, 100 * x + 50 + r, 100 * y + 50 + r, outline='green', width=7)

    def draw_mesh(self):
        self.create_line(0, 100, 300, 100, fill='purple', dash=(10,5), width=2)
        self.create_line(0, 200, 300, 200, fill='purple', dash=(10,5), width=2)

        self.create_line(100, 0, 100, 300, fill='purple', dash=(10,5), width=2)
        self.create_line(200, 0, 200, 300, fill='purple', dash=(10,5), width=2)
    
    def bot_move(self):
        
        free_cells = [] # массив свободных ячеек для ноликов
        attack = None
        protect = None
        
        h = self.result
        b = (self.result + 1) % 2

        # 0 1 2
        # 3 4 5
        # 6 7 8
        
        for i in range(len(self.state)):
            if self.state[i] == None:
                free_cells.append(i)
        
        # выбираем наиболее подходящий индекс k массива self.state 
        # т.е. первостепенно - атакуем, если можем победить, иначе - защищаемся, если грозит проигрыш, иначе если свободна центральная ячейка - занимаем ее, иначе выбираем любую ячейку из free_cells
        
        for j in range(0, 7, 3): # смотрим горизонталь на предмет необходимости атаки/защиты
            bot_cnt = 0
            human_cnt = 0
            spare = None
            for i in range(3):
                #print(i + j)
                if self.state[i + j] == h:
                    human_cnt += 1
                elif self.state[i + j] == b:
                    bot_cnt += 1 
                else:
                    spare = i + j

            if bot_cnt == 2 and spare != None:
                attack = spare
                break
            elif human_cnt == 2 and spare != None:
                protect = spare

        for i in range(3):  # смотрим вертикаль
            bot_cnt = 0
            human_cnt = 0
            spare = None
            for j in range(0, 7, 3):
                if self.state[i + j] == h:
                    human_cnt += 1
                elif self.state[i + j] == b:
                    bot_cnt += 1 
                else:
                    spare = i + j
            if bot_cnt == 2 and spare != None:
                attack = spare
                break
            elif human_cnt == 2 and spare != None:
                protect = spare
           
        bot_cnt = 0
        human_cnt = 0
        spare = None

        for i in range(0, 9, 4):  # смотрим главную диагональ
            if self.state[i] == h:
                human_cnt += 1
            elif self.state[i] == b:
                bot_cnt += 1 
            else:
                spare = i
        if bot_cnt == 2 and spare != None:
            attack = spare
        elif human_cnt == 2 and spare != None:
            protect = spare
            
        bot_cnt = 0
        human_cnt = 0
        spare = None

        for i in range(2, 7, 2): # смотрим побочную диагональ
            if self.state[i] == h:
                human_cnt += 1
            elif self.state[i] == b:
                bot_cnt += 1 
            else:
                spare = i
        if bot_cnt == 2 and spare != None:
            attack = spare
        elif human_cnt == 2 and spare != None:
            protect = spare
                
        if attack != None:
            k = attack
            print('attack')
        elif protect != None:
            k = protect
            print('protection')
        else:
            if self.state[4] == None:
                k = 4
                print('middle occupation')
            else:
                k = choice(free_cells)
                print('random')


        self.state[k] = (self.result + 1) % 2 # result: 0 -> 1; 1 -> 0
        
        if k == 0:
            self.player_2_move(0, 0)
        elif k == 1:
            self.player_2_move(1, 0)
        elif k == 2:
            self.player_2_move(2, 0)
        elif k == 3:
            self.player_2_move(0, 1)
        elif k == 4:
            self.player_2_move(1, 1)
        elif k == 5:
            self.player_2_move(2, 1)
        elif k == 6:
            self.player_2_move(0, 2)
        elif k == 7:
            self.player_2_move(1, 2)
        elif k == 8:
            self.player_2_move(2, 2)
    def get_winner(self):
        # 0 1 2  /   0 1 2
        # 3 4 5  /   1
        # 6 7 8  /   2
        # проверяем на победную комбинацию

        # вертикальные
        if (self.state[0] == 1 and self.state[1] == 1 and self.state[2] == 1) or (self.state[0] == 0 and self.state[1] == 0 and self.state[2] == 0):
            return [0, 50, 300, 50, self.state[0]] # координаты начала и конца прямой + крестик/нолик
        if (self.state[3] == 1 and self.state[4] == 1 and self.state[5] == 1) or (self.state[3] == 0 and self.state[4] == 0 and self.state[5] == 0):
            return [0, 150, 300, 150, self.state[3]]
        if (self.state[6] == 1 and self.state[7] == 1 and self.state[8] == 1) or (self.state[6] == 0 and self.state[7] == 0 and self.state[8] == 0):
            return [0, 250, 300, 250, self.state[6]]
        
        # горизонтальные
        if (self.state[0] == 1 and self.state[3] == 1 and self.state[6] == 1) or (self.state[0] == 0 and self.state[3] == 0 and self.state[6] == 0):
            return [50, 0, 50, 300, self.state[0]] # координаты начала и конца прямой + крестик/нолик
        if (self.state[1] == 1 and self.state[4] == 1 and self.state[7] == 1) or (self.state[1] == 0 and self.state[4] == 0 and self.state[7] == 0):
            return [150, 0, 150, 300, self.state[1]]  
        if (self.state[2] == 1 and self.state[5] == 1 and self.state[8] == 1) or (self.state[2] == 0 and self.state[5] == 0 and self.state[8] == 0):
            return [250, 0, 250, 300, self.state[2]]
        # диагональные
        if (self.state[0] == 1 and self.state[4] == 1 and self.state[8] == 1) or (self.state[0] == 0 and self.state[4] == 0 and self.state[8] == 0):
            return [0, 0, 300, 300, self.state[0]]
        if (self.state[2] == 1 and self.state[4] == 1 and self.state[6] == 1) or (self.state[2] == 0 and self.state[4] == 0 and self.state[6] == 0):
            return [300, 0, 0, 300, self.state[2]]
        
        # проверка на то, что больше не осталось пустых клеток(= ничья)
        cur_flag = 1
    
        for i in range(9):
            if self.state[i] == None:
                cur_flag = 0
                break
        if cur_flag == 1:
            return 'draw'
            
        return None
    
    def end(self):  # окончание игры 
        var = self.get_winner()
        if var != 'draw':
            x1, y1, x2, y2, winner = self.get_winner()
            # winner - 0 = bot, 1 = human
            # self.result - 0 = human choosed noughts, 1 = human choosed crosses
            self.create_line(x1, y1, x2, y2, fill='red', width=7)
            listt = ['NOUGHTS', 'CROSSES']
            win_str = listt[winner] + ' WON!!!'
            self.create_text(150, 150, text=win_str,fill="red",font=('Helvetica 25 bold'))

        else:   
            self.create_text(150, 150, text= "DRAW",fill="red",font=('Helvetica 50 bold'))
        self.flag = 0   # опускаем флаг = игра закончена




def main():
    # инициализируем окно выбора
    choice = Choice()
    choice.title('X or O')
    choice.geometry("200x200")
    l = ttk.Label(text='CHOOSE SIDE', font=('Arial', 14), foreground="#B71C1C")
    l.place(x = 27, y = 15)
    choice.mainloop()   
    
    
    

    game = TicTacToe(tkinter.Tk(), choice.result) # создаем объект класса TicTacToe
    game.pack()
    

    game.draw_mesh() # рисуем клетки поля
    game.window.mainloop()


if __name__ == '__main__':
    main()
