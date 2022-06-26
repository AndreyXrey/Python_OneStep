# "ab" is a reduction of 'a'ddress 'b'ook
ab = { 'Swaroop' : 'swaroop@swaroopch.com',
       'Larry': 'larry@wall.org',
       'Matsumoto': 'matz@ruby-land.org',
       'Spammer': 'sammer@hotmail.com'
       }

print("Swaroop's address is:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print("\n There are {0} contacts in address book\n".format(len(ab)))
# {0}_______.format()


for name, address in ab.items():
    print("Contact {0} with address {1}".format(name,address))

# Добавление пары ключ-значение
ab['Guido'] = "guido@python.org"

if 'Guido' in ab:
    print("\n Адпес Guido:", ab['Guido'])