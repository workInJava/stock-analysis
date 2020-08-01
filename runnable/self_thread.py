
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, param ,fun):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.param = param
        self.fun = fun

    def run(self):
        print ("开始线程：" + self.name)
        self.fun(self.param)
        print ("退出线程：" + self.name)

def print_time(test):
    print("============="+test)

# 创建新线程
thread1 = myThread(1, "Thread-1","wewew", print_time)
thread2 = myThread(2, "Thread-2","dsds" ,print_time)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")