import random

n = int(input('Number of double rolls: '))
ats = []
for i in range(n):
    dice1 = random.randint(1,6)
    #print(f"The first dice shows {dice1}.")
    dice2 = random.randint(1,6)
    #print(f"The second dice shows {dice2}.")


    sumn = dice1 + dice2
    #print(f"The sum of the dices is {sumn}.")
    ats.append(sumn)

mean = sum(ats)/n
print(mean)
print('*' * 80)

# (*^-^*)

