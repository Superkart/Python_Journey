"""
📘 Exercise: Array Data Structure
Source: CodeWithHarry Python Tutorial - Video 3

Part 1: Monthly Expenses
You have a list of monthly expenses:
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

Using this list, perform the following tasks:
1. In February, how many dollars did you spend extra compared to January?
2. Find out your total expense in the first quarter (first three months) of the year.
3. Check if exactly $2000 was spent in any month.
4. Add June's expense of $1980 to the list.
5. You received a refund of $200 for an April purchase. Update the list to reflect this refund.
"""

monthlyExpenses = [2200, 2350, 2600, 2130, 2190]
febToJan = monthlyExpenses[1] - monthlyExpenses[0]
print(febToJan)
firstQuarter = monthlyExpenses[0] + monthlyExpenses[1] + monthlyExpenses[2]
print(firstQuarter)

for i in range(len(monthlyExpenses)):
    if(monthlyExpenses[i] == 2000):
        print(f'yes in month {i - 1} 2000 was spent')

else:
    print('nope')

monthlyExpenses.insert(len(monthlyExpenses), 1980)
print(monthlyExpenses)

monthlyExpenses[3] = monthlyExpenses[3] + 200
print(monthlyExpenses)


"""""
Part 2: Marvel Heroes List
You have a list of Marvel superheroes:
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

Tasks:
1. Find the length of the list.
2. Add 'black panther' at the end of the list.
3. Move 'black panther' to appear after 'hulk'.
4. Replace 'thor' and 'hulk' with 'doctor strange' in a single line.
5. Sort the list alphabetically.
"""
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(heros))
heros.insert(len(heros), 'black panther')
print(heros)
heros.insert(heros.index('hulk') + 1, heros[len(heros) - 1])
heros.pop(len(heros) - 1)
print(heros)

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()
print(heros)

""""
Part 3: Odd Numbers Generator
- Take a max number as input from the user.
- Generate a list of all odd numbers from 1 to that max number.
"""
try:
    maxNumber = int(input('Enter a number : '))
except:
    print('Invalid input bro!')

odd_Numbers = []
for i in range(maxNumber):
    if(i%2 != 0):
        odd_Numbers.append(i)
    else:
        continue

print(odd_Numbers)