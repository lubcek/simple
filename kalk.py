#Financial Maths
from time import sleep

def calc_expenses(nom,inte,per):
    inte = inte/100
    intres = nom*inte*per
    result = nom+intres
    return(result)


def calc_interest():
    pass

def calc_payment():
    pass

def calc_loan():
    pass

def warning():
    print("You have not entered enough data!")

params = []

try:
    loan = int(input("Enter the nominal amount: "))
    params.append(loan)
except ValueError:
    loan = 0

try:
    intrest = int(input("Enter the interest rate in %: "))
    params.append(intrest)
except ValueError:
    intrest = 0

try:
    length = int(input("Enter the loan period: "))
    params.append(length)
except ValueError:
    length = 0

try:
    onepay = int(input("Enter the single payment: "))
    params.append(onepay)
except ValueError:
    onepay = 0

try:
    exp = int(input("Enter all expenses: "))
    params.append(exp)
except ValueError:
    exp = 0    


print("So, let's start ...")
sleep(1)
    
if exp == 0:
    if (loan*intrest*length) != 0:
        result = calc_expenses(loan,intrest,length)
        print("You will pay {}".format(result))
    else:
        warning()



##def compound_interest():
##  print ' '
##  P = input('  The starting value: ')
##  i = input('  Interest rate:      ')
##  r = input('  Compounded:         1: Monthly\n                      2: Yearly\n                   => ')  
##  if r in (1,2):
##    n = input('  Number of years:    ')
##    if i >= 1:
##      i = i/100.00
##    if r == 1:
##      i = i/12.00
##      n = n*12
##      return P*(1+i)**n
##    elif r == 2:
##      return P*(1+i)**n
##  else:
##    print'\n  [E]\n  Please insert 1 or 2'
##    return
