#Financial Maths
i = 0.00
def compound_interest():
  print ' '
  P = input('  The starting value: ')
  i = input('  Interest rate:      ')
  r = input('  Compounded:         1: Monthly\n                      2: Yearly\n                   => ')  
  if r in (1,2):
    n = input('  Number of years:    ')
    if i >= 1:
      i = i/100.00
    if r == 1:
      i = i/12.00
      n = n*12
      return P*(1+i)**n
    elif r == 2:
      return P*(1+i)**n
  else:
    print'\n  [E]\n  Please insert 1 or 2'
    return
