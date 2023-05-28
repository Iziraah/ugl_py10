# Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра. 



class Bankomat():
    def __init__(self, bank = 0):
        self.__bank = bank
        
    def get_bank(self):
        return self.__bank
    

    def add_bank(self):
        cash = int(input("Введите сумму, кратную 50: "))
        self.__bank += cash
        return print('Your balance: ', self.get_bank())
    

    def take_bank(self):
        cash = int(input("Введите сумму, кратную 50: "))
        if cash > self.__bank:
            print('Нет денег!')
            exit()        
        if cash <=2000:
            cash -=30
        elif 2001 <= cash <= 40000:
            cash *= 0.0985
        else:
            cash -= 600
        self.__bank -= cash
        
        print('Your balance: ', self.get_bank())

b = Bankomat(0)

def wellcome():
        dict = {}
        id = 1
        while True:
            action = int(input('1 - Снять\n2 - Пополнить\n3 - Выйти\n'))
            if b.get_bank() >= 5000000:
                b.__bank *= 0.9
            match action:
                case 1:
                    b.take_bank()                                    
                        
                case 2:
                    b.add_bank()
                case 3:
                    exit()

wellcome()