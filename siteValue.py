class site:
    def __init__(self):
        self.masterValue = 0
        self.m_url = ""
        self.m_login_btn = ""
        self.m_id_text = ""
        self.m_pw_text = ""
        self.m_birth_text =""
        self.m_birth_btn = ""

    def getMasterValue(self):
        return self.masterValue
    def getUrl(self):
        return self.m_url
    def getLoginBtn(self):
        return self.m_login_btn
    def getIdText(self):
        return self.m_id_text
    def getPwText(self):
        return self.m_pw_text
    def getBirthText(self):
        return self.m_birth_text
    def getBirthBtn(self):
        return self.m_birth_btn

    def setSiteValue(self, num):
        if(num == '1'):
            self.masterValue = 1;
            self.m_url = "http://www.ticketlink.co.kr/";
            self.m_login_btn = "loginBtn";
            self.m_id_text = "id"
            self.m_pw_text = "pw";
            self.m_birth_text = "birthday";
            self.m_birth_btn = "confirmBtn";

            print(self.m_url);

        if (num == '2'):
            self.masterValue = 2;
            self.m_url = "http://ticket.interpark.com/"
            self.m_login_btn = "loginBtn";
            self.m_id_text = "id"
            self.m_pw_text = "pw";
            print(self.m_url);

        if(num == '3'):
            self.masterValue = 3;
            self.m_url = "http://ticket.yes24.com/"
            self.m_login_btn = "loginBtn";
            self.m_id_text = "id"
            self.m_pw_text = "pw";
            print(self.m_url);


