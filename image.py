from dataclasses import dataclass
import datetime as dt
from string import digits

@dataclass
class deposits:
    deps: list
    def total_deposits(self):
        total = 0
        for deposit in self.deps:
            total += deposit.value
        return total

@dataclass
class deposit:
    value: int
    date: str


def str_to_date(str_date):
    date = list(map(int,str_date.split('/')))
    return dt.date(date[2],date[0],date[1])


def acct_to_int(str_number):
    res = ''
    dig = set(digits)
    for l in str_number:
        if l in dig or l == '.':
            res = res+l
    return float(res)


def get_values(type,data,start,stop):



fd = open('testpdf2.txt', 'r')
data = fd.read().split()

deposit_count = 0
at_deposits = False
deposits = deposits([])

amount_count =

#create deposit objects
for i in range(len(data)):
    if data[i] == 'Deposit':
        deposit_count += 1
        at_deposits = True
    if data[i].startswith('$') and at_deposits:
        deposits.deps.append(deposit(acct_to_int(data[i]),None))
    if data[i] == 'Electronic' and data[i+1] == 'Credits':
        break



#add date values to deposits
for i in range(len(data)):
    if data[i-1] == 'Deposits':
        for j in range(len(deposits.deps)):
            deposits.deps[j].date = str_to_date(data[i+j+1])

for i in deposits.deps:
    print(i.value, i.date)


print("total deposits:",deposits.total_deposits())
