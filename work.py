# Number 1
data = [
    {'name': 'tower', 'speed': 0, 'hp': 100}, 
    {'name': 'ork', 'speed': 10, 'hp': 0}, 
    {'name': 'soldier', 'speed': 10, 'hp': 10}, 
    {'name': 'troll', 'speed': 10, 'hp': -1}, 
    {'name': 'ruin', 'speed': 0, 'hp': -100}, 
    {'name': 'rock', 'speed': 0, 'hp': 0}, 
    {'name': 'castle', 'speed': 0, 'hp': 999}, 
    {'name': 'bird', 'speed': 100, 'hp': 0.1}, 
]

# Number 1
output_list = []

for obj in data:
    if obj['hp'] > 0 and obj['speed'] == 0:
        output_list.append(obj)

# Живые но недвигающиеся объекты
print(output_list) # -> [{'name': 'tower', 'speed': 0, 'hp': 100}, {'name': 'castle', 'speed': 0, 'hp': 999}]


# Number 2
# Какие были ошибки в программе?
MAX_NUMBER = 2 ** 32 - 1

def find_slowest_unit(units):
    slowest_unit = None
    # Ошибка 1. Минимальная скорость изначально 
    # должна быть максимально возможной
    minSpeed = MAX_NUMBER

    for currentUnit in units:
        # Ошибка 2. Мы должны найти юнит с минимальной скоростью => 
        # Мы должны делать проверку, 
        # если скорость текущего юнита меньше
        # минимальной скорости, 
        # то будем менять данные минимальной скорости и 
        # самого медленного юнита 
        if currentUnit['speed'] < minSpeed:
            slowest_unit = currentUnit
            minSpeed = currentUnit['speed'] # Ошибка 3. Данные словаря в Python получаются только через квадратные скобки, currentUnit['speed']
        
        # Ошибка 4. Должны возвращать либо None, либо самый медленный юнит
        return slowest_unit


print(find_slowest_unit(data)) # -> {'name': 'tower', 'speed': 0, 'hp': 100} т.к первый элемент с самой минимальной скоростью