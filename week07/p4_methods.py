class Phone:
    __password = "0805"

    @classmethod 
    def getPasswd(cls):
        print(cls.__password)
        return cls.__password

    @staticmethod
    def sayHello():
        print('Hello')

    def printPasswd(self):
        print(self.__password)


huawei = Phone()
huawei.printPasswd()
Phone.getPasswd()

class MobilePhone(Phone):
    def output(self):
        self.getPasswd()

apple = MobilePhone()
apple.output()
