import random
# Создаем доску с кораблями
horizon = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
vertical = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
counter = 10
places = []
while counter > 0:  # раскидываем корабли по игровой зоне
    counter -= 1
    if ([horizon[random.randint(0, 8)], vertical[random.randint(0, 8)]]) in places:
        counter += 1
    else:
        places.append([horizon[random.randint(0, 8)], vertical[random.randint(0, 8)]])
print(places)  # Убираем, чтобы не было подсказки где расположенны корабли


def game(): #начинает игру
    while len(places) > 0:
        dot = input("Введите точку") #Вводим точку B1
        if list(dot.upper()) in places:
            print(f"корабль потоплен на {list(dot)}")
            places.remove(list(dot.upper()))
            print(places)
        else:
            print("мимо")


game()

if __name__ == "__main__":
    game()