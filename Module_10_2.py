import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        people = 100
        days = 0
        while people > 0:
            time.sleep(1)
            days += 1
            people -= self.power
            if people < 0:
                people = 0
            print(f'{self.name} сражается {days} суток, осталось {people} воинов врага.')
        print(f'{self.name} одержал победу спустя{days}дней(дня)!')

knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight('Sir Galahad', 20)
# Запуск потоков и остановка текущего
knight1.start()
knight2.start()
knight1.join()
knight2.join()
# Вывод строки об окончании сражения
print('Все битвы закончены!')