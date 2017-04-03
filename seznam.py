l = []
a = ''
print('Welcome to Shopping List Creator, 1.0\n')

print('Pro konec zadávání napište k')
while a!='k':
    a = input('Zadej položku na nákup do seznamu: ')
    if a in l:
        print('Tuto položku jsi již zadal.')
    else:
        l.append(a)
l.pop(-1)
print('')
print('Musíš nakoupit:')
print('---------------')
for item in l:
    print(item)
