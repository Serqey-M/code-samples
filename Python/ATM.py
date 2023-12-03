# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import datetime

class ATM():
    _MULTIPLICITY = 50
    _PERCENTAGE_FOR_WITHDRAWAL = 0.015
    _MIN_PERCENTAGE_FOR_WITHDRAWAL = 30
    _MFX_PERCENTAGE_FOR_WITHDRAWAL = 600
    _MAX_COUNT_OPERATION = 3
    _ACCRUAL_PERCENTAGE = 0.03
    _WEALTH_TAX = 0.1
    _BORDER_WEALTH_TAX = 5_000_000
        
    def __init__(self, name: str, balance: float = 0) -> None:
        self.name = name
        self.balance = balance
        with open(f'D:\code-samples\Python\\balance-{self.name}.txt', 'w', encoding='utf-8') as f1, \
            open(f'D:\code-samples\Python\count_operation-{self.name}.txt', 'w', encoding='utf-8') as f2:
            f1.write(str(self.balance))
            f2.write(str(0))
            

    def replenish(self):
        with open(f'D:\code-samples\Python\\balance-{self.name}.txt', 'r', encoding='utf-8') as f1, \
            open(f'D:\code-samples\Python\count_operation-{self.name}.txt', 'r', encoding='utf-8') as f2:
            balance = float(f1.read())
            count_operation = int(f2.read())
        if balance > self._BORDER_WEALTH_TAX:
           balance = balance - balance * self._WEALTH_TAX
        summa = int(
            input("Введите сумму пополнения кратную 50 или 0 для отмены операции: ")
        )
        while summa % self._MULTIPLICITY != 0:
            summa = int(
                input("Введите сумму пополнения кратную 50 или 0 для отмены операции: ")
            )
        if summa != 0:
            balance += summa
            count_operation += 1
            if count_operation == self._MAX_COUNT_OPERATION:
                count_operation = 0
                balance *= 1 + self._ACCRUAL_PERCENTAGE
        data = [str(datetime.datetime.now()), f'Сумма пополнения: {summa}', f'Баланс: {balance}']
        with open(f'D:\code-samples\Python\\balance-{self.name}.txt', 'w', encoding='utf-8') as f1, \
            open(f'D:\code-samples\Python\count_operation-{self.name}.txt', 'w', encoding='utf-8') as f2, \
            open(f'D:\code-samples\Python\information.txt', 'a', encoding='utf-8') as f3:
            f1.write(str(balance))
            f2.write(str(count_operation))
            f3.write(f'{str(data)} \n')
        print (f'Баланс: {balance}')


    def withdraw(self):
        with open(f'D:\code-samples\Python\\balance-{self.name}.txt', "r", encoding='utf-8') as f1, \
            open(f'D:\code-samples\Python\count_operation-{self.name}.txt', "r", encoding='utf-8') as f2:
            balance = float(f1.read())
            count_operation = int(f2.read())
        if balance > self._BORDER_WEALTH_TAX:
           balance = balance - balance * self._WEALTH_TAX
        summa = int(input("Введите сумму снятия кратную 50 или 0 для отмены операции: "))
        while summa % self._MULTIPLICITY != 0:
            summa = int(
                input("Введите сумму снятия кратную 50 или 0 для отмены операции: ")
            )
        if summa != 0:
            summa_percentage_for_withdrawal = summa * self._PERCENTAGE_FOR_WITHDRAWAL
            if summa_percentage_for_withdrawal > self._MFX_PERCENTAGE_FOR_WITHDRAWAL:
                summa_percentage_for_withdrawal = self._MFX_PERCENTAGE_FOR_WITHDRAWAL
            elif summa_percentage_for_withdrawal < self._MIN_PERCENTAGE_FOR_WITHDRAWAL:
                summa_percentage_for_withdrawal = self._MIN_PERCENTAGE_FOR_WITHDRAWAL
            summa_withdrawals = summa + summa_percentage_for_withdrawal
            if summa_withdrawals <= balance:
                balance = balance - summa_withdrawals
            else:
                print("на счете не достаточно средств")
            count_operation += 1
            if count_operation == self._MAX_COUNT_OPERATION:
                count_operation = 0
                balance *= 1 + self._ACCRUAL_PERCENTAGE
        data = [str(datetime.datetime.now()), f'Сумма снятия: {summa}', f'Баланс: {balance}']
        with open(f'D:\code-samples\Python\\balance-{self.name}.txt', 'w', encoding='utf-8') as f1, \
            open(f'D:\code-samples\Python\count_operation-{self.name}.txt', 'w', encoding='utf-8') as f2,\
            open(f'D:\code-samples\Python\information.txt', 'a', encoding='utf-8') as f3:
            f1.write(str(balance))
            f2.write(str(count_operation))
            f3.write(f'{str(data)} \n')
        print (f'Баланс: {balance}')


    def operation_selection(self):
        operation = -1
        while operation != 0:
            operation = int(
                input("Выберите операцию: 1 - пополнение; 2 - снятие; 3 - информация; 0 - выход ")
            )
            match operation:
                case 1:
                    self.replenish()
                case 2:
                    self.withdraw()
                case 3:
                    with open(f'D:\code-samples\Python\information.txt', "r", encoding='utf-8') as f:
                        print(list(f))
                case 0:
                    break
                case _:
                    print("Не коректный выбор операции")


if __name__ == '__main__':
    user1 = ATM('zxc')
    user1.operation_selection()