from random import randint

my_list = []
while not len(my_list) == 6:
    try:
        num = int(input("Choose number from 1 to 49: "))
        if num in my_list:
            print("You've already chosen this number. Choose another number.")
        else:
            while True:
                if num > 49:
                    print("Chosen number is too big.")
                elif num < 1:
                    print("Chosen number is too small.")
                else:
                    my_list.append(num)
                break
    except ValueError:
        print("You can only choose numbers.")

my_list.sort()
print(my_list)

comp_list = []
while not len(comp_list) == 6:
    num_comp = randint(1, 49)
    if num_comp in comp_list:
        pass
    else:
        comp_list.append(num_comp)


comp_list.sort()
print(comp_list)

hits = 0
for number in my_list:
    if number in comp_list:
        hits += 1

print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")

# shots_num = []
# for i in my_list:
#     for u in comp_list:
#         if i == u:
#             shots_num.append(1)
#
# if len(shots_num) == 0:
#     print("Przykro mi. Nie udało Ci się trafić żadnej liczby.")
# elif len(shots_num) == 1:
#     print("Brawo! Udało Ci się trafić 1 liczbę.")
# elif len(shots_num) == 5:
#     print("Brawo! Udało Ci się trafić 5 liczb.")
# elif len(shots_num) == 6:
#     print("Brawo! Trafiłeś wszystkie liczby!")
# else:
#     print(f"Brawo! Udało Ci się trafić {len(shots_num)} liczby.")
