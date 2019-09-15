class  Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato (self):
        print("Saldo de {} do titular {}".format(self.__saldo,self.__titular))

    def getNumero(self):
        return self.__numero
        
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    def deposita(self,  valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, contadestino, valor):
        if (self.__saldo+self.__limite) - valor >= 0:
            self.saca(valor)
            contadestino.deposita(valor)
            print("Transferência realizada com sucesso!")
        else:
            print("Não é possivel transferir o valor {} da conta {} para a conta {}".format(valor, self.getNumero(), contadestino.getNumero()))
        

    