from random import randint


my_list = []
for i in range(3):
    num = int(input("Podaj liczbę: "))
    while True:
        if num > 9:
            print("Podałeś za dużą liczbę.")
        elif num < 1:
            print("Podałeś za małą liczbę.")
        else:
            my_list.append(num)
        break

my_list.sort()
print(my_list)

comp_list = []
for item in range(3):
    num_comp = comp_list.append(randint(1, 9))

comp_list.sort()
print(comp_list)

shots_num = []
for i in my_list:
    for u in comp_list:
        if i == u:
            shots_num.append(1)

if len(shots_num) == 0:
    print("Nie udało Ci się trafić żadnej liczby.")
elif len(shots_num) == 1:
    print("Brawo! Udało ci się trafić 1 liczbę.")
else:
    print(f"Brawo! Udało Ci się trafić {len(shots_num)} liczby.")
