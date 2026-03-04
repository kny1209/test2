class Phone:
    def __init__(self, factory, year, color):
        self.factory = factory
        self.year = year
        self.color = color

    def info(self):
        print("제조사 :",self.factory,"\n출고년도 :",self.year,"\n색상 :",self.color)

    def setinfo(self,factory, year, color ):
        self.factory = factory
        self.year = year
        self.color = color

my_phone = Phone('A',2015,'green')
my_phone.info()
my_phone.setinfo('B', 2022, 'red')
my_phone.info()