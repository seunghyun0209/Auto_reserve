class privateValue:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)
        return cls._instance

    def setSite(self, site):
        self.__site = site;

    def setId(self,id):
        self.__id = id;

    def setPw(self, pw):
        self.__pw = pw;

    def setBirthday(self,bd):
        self.__bd = bd;

    def setConcert(self,concert):
        self.__concert = concert;

    def getSite(self):
        return self.__site;

    def getId(self):
        return self.__id;

    def getPw(self):
        return self.__pw;

    def getBirthday(self):
        return self.__bd;

    def getConcert(self):
        return self.__concert;