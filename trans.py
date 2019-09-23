from dataclasses import dataclass
import datetime as dt
from string import digits


cred_types = set(('Wire DepositDomestic','ACH Deposit', 'IB Transfer Deposit'))
deb_types = set(('IB Transfer W/D','ACH Payment','POS Payment'))

transactions = []


fd = open('testpdf2.txt', 'r')

data = [line.strip('\n') for line in fd]

tmp_data = []
for i in data:
    if i == '':
        continue
    else:
        tmp_data.append(i)
data = tmp_data


amount_count = 0
credits_dates = []
credits_description = []
credits_amount = []
Credits = False
at_deposits = False
in_deposit_dates = False
deposit_dates = []
deposit_amounts = []
for i in range(len(data)):
    if data[i] == "Deposits" and data[i+1] == 'Date':
        in_deposit_dates = True
    if data[i] == 'Deposit':
        at_deposits = True
        in_deposit_dates = False
    if data[i] == ('Electronic Credits'):
        Credits = True
        at_deposits = False
    if data[i] == ('Electronic Debits'):
        Credits = False
        Debits = True
    if data[i].startswith('02/') and in_deposit_dates == True:
        deposit_dates.append(data[i])
    if data[i].startswith('$') and at_deposits:
        deposit_amounts.append(data[i])
    if data[i] == 'Amount' and Credits == True:
        amount_count += 1
    if data[i].startswith('02/') and Credits == True:
        credits_dates.append(data[i])
    if data[i] in cred_types and Credits == True:
        credits_description.append(data[i+1])
    if data[i].startswith('$') and Credits == True and amount_count > 1:
        credits_amount.append(data[i])
    if data[i] in deb_types and Credits == True:
        credits_description.append(data[i+1])
    if data[i].startswith('$') and Credits == True and amount_count > 1:
        credits_amount.append(data[i])


for i in range(len(credits_amount)):
    print(credits_dates[i], end=" ")
    print(credits_description[i],end=" ")
    print(credits_amount[i])

print(deposit_dates)
print(deposit_amounts)
