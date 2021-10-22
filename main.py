import sys
from enum import Enum

randomList = ['a', 0, 2]


class WithdrawStatus(Enum):
    Ok = 1,
    CantWithdrawMoreThan4000PerTime=2,
    MustBeLargerThan0=3,
    NotEnoughSaldo=4    


# ska dra och returnera nya saldot
class Account:
    def __init__(self, kontonummer:str):
        self._saldo = 0
        self._kontonummer = kontonummer
    def getKontonummer(self) -> str:
        return self._kontonummer
    def setKontonummer(self, kontonummer:str):
        self._kontonummer = kontonummer

    def getSaldo(self) -> int:
        return self._saldo

    def anotherwithdraw(self, belopp:int)->WithdrawStatus:
        if belopp > 4000:
            return WithdrawStatus.CantWithdrawMoreThan4000PerTime
        if belopp <= 0:
            return WithdrawStatus.MustBeLargerThan0
        if belopp > self._saldo:
            return WithdrawStatus.NotEnoughSaldo
        self._saldo = self._saldo - belopp
        
        return WithdrawStatus.Ok


    def withdraw(self, belopp:int)->int:

        if belopp > 4000:
            raise ValueError("Cant withdraw more than 4000 each time")
        if belopp <= 0:
            raise ValueError("Most be larger than 0")
        if belopp > self._saldo:
            raise ValueError("Not enough saldo")


        # canConnectToBank = False
        # if canConnectToBank == False: 
        #     raise ConnectionError("Bankomat offline right now. come back later")

        self._saldo = self._saldo - belopp
        return self._saldo


acc = Account("121221-12")
while True:
    x = int(input("Hur mycket vill du ta ut"))
    status = acc.anotherwithdraw(x)
    if status == WithdrawStatus.CantWithdrawMoreThan4000PerTime:
        print("Cant 4000")
    elif status == WithdrawStatus.MustBeLargerThan0:
        print("Larger than 0 tack")
    elif status == WithdrawStatus.NotEnoughSaldo:
        print("inte tillr saldo")
    elif status == WithdrawStatus.Ok:
        nyaSaldot =  acc.getSaldo()
        print("Nya saldot:", nyaSaldot)
    break
        




acc = Account("121221-12")
while True:
    try:
        x = int(input("Hur mycket vill du ta ut"))
        nyaSaldot =  acc.withdraw(x)
        print("Nya saldot:", nyaSaldot)
        break
    except ValueError as ex:    
        print(ex.args[0])
        





try:
    acc.withdraw(200)
except Exception as ex:
    print(ex.args[0])    




for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
    except Exception:
        print("Ngt gick fel")


for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
    except (ValueError, TypeError):
        print("Det är nog inte ett numeriskt värde verkar det som")
        print()
    except ZeroDivisionError:
        print("Men idiot en 0:a går ju inte att dela med")
        print()



print("The reciprocal of", entry, "is", r)




# mata in fem tal i en lista
# får inte krascha...


tal = []
while(len(tal) < 5):
    try:
        x=int(input("Ange tal:"))
        tal.append(x)
    except:
        print("Fel")



      

        