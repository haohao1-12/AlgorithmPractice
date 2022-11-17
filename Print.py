# 流程： 
# 按照概率生成打印作业，加入打印队列
# 如果打印机空闲，且队列不空，则取出对手作业打印，记录次作业的等待时间
# 如果打印机忙，则按照打印速度进行1秒打印
# 如果当前作业打印完成，则打印机进入空闲

# 作业等待时间：
# 生成作业时，记录生成的时间戳
# 开始打印时，当前时间减去生成时间即可

# 作业打印时间：
# 生成作业时，记录作业的页数
# 开始打印时，页数除以打印速度即可

from pythonds.basic.queue import Queue

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm # print speed
        self.currentTask = None # print task
        self.timeRemaining = 0 # time countdown

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self): # busy or not
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time) -> None:
        self.timestamp = time
        self.pages = random.randrange(1,21) # How mang pages will it print

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds, pagesPerMinute): # 打印多长时间，打印机设定的模式

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait, printQueue.size()))

for i in range(10):
    simulation(3600, 10)









