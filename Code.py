import random
n = input('Enter the number of friends joining (including you):')
print()
try:
    assert int(n) > 0
except AssertionError:
    print("No one is joining for the party")

names = []
name_dict = {}
val = 0

if int(n) > 0:
    for x in range(int(n)):
        names.append(input('Enter the name of every friend (including you), each on a new line:'))

    print()
    b = int(input('Enter the total bill value:'))
    print()

    feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    print()
    try:
        assert feature == 'Yes'
        lucky = random.choice(names)
        print(f'{lucky} is the lucky one!')
        print()
        val = round((b / (int(n) - 1)), 2)
        name_dict = dict.fromkeys(names, val)
        name_dict[lucky] = 0
        print(name_dict)

    except AssertionError:
        print('No one is going to be lucky')
        val = round(b / int(n), 2)
        name_dict = dict.fromkeys(names, val)
        print()
        print(name_dict)
