import random
count = 0
kisekitaiken = "奇跡体験"
unbeliavable = "アンビリバボー"
kiseki_list = list(kisekitaiken)
unbeli_list = list(unbeliavable)
while True:
    # カウンターを増加
    count += 1
    kiseki_temp = ""
    unbeli_temp = ""
    # 奇跡体験
    for i in range(0, len(kiseki_list)):
        kiseki_temp += random.choice(kiseki_list)
    # アンビリバボー
    for i in range(0, len(unbeli_list)):
        unbeli_temp += random.choice(unbeli_list)
    # 連結
    constructed = kiseki_temp + "！" + unbeli_temp
    message = "[" + str(count) + "]: " + constructed
    # 一致しなければそのまま出力し次
    # 一致しなかった時点でcountが1000の倍数だったら出力
    # 一致すればその時点で終了
    if constructed == "奇跡体験！アンビリバボー":
        print("成功！")
        print(message)
        break
    elif count % 100 == 0:
        print(message)
        continue
    else:
        continue
