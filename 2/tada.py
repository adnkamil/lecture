import threading
import time

class RacingCar:
    def __init__(self,name) :
        self.carName = name + 1
        self.result = 0

    def runCar(self) :
        for i in range (self.carName) :
            self.result = self.result + i     
        # print(self.result)
        # print('1+2+3+....+', self.carName, '=', self.result)
        print('template disini', self.result)


#program start from 1
#insert parameter 
car1 = RacingCar(1000)              # 1+2+3+....+1000 = ...
car2 = RacingCar(100000)            # 1+2+3+....+100000 = ...
car3 = RacingCar(10000000)          # 1+2+3+....+10000000 = ...

th1 = threading.Thread(target=car1.runCar)
th2 = threading.Thread(target=car2.runCar)
th3 = threading.Thread(target=car3.runCar)

th1.start()
th2.start()
th3.start()
