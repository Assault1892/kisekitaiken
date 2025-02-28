import random

count = 0
kisekitaiken = "奇跡体験"
unbeliavable = "アンビリバボー"
kiseki_list = list(kisekitaiken)
unbeli_list = list(unbeliavable)
kiseki_len = len(kiseki_list)
unbeli_len = len(unbeli_list)

target = "奇跡体験！アンビリバボー"

while True:
    count += 1
    kiseki_temp = ''.join(random.choices(kiseki_list, k=kiseki_len))
    unbeli_temp = ''.join(random.choices(unbeli_list, k=unbeli_len))
    constructed = f"{kiseki_temp}！{unbeli_temp}"
    if constructed == target:
        print(f"成功！[{count}]: {constructed}")
        break
    elif count % 100 == 0:
        print(f"[{count}]: {constructed}")
