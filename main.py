workers, plays = map(int, input().split(" "))
mas=[0]*workers #массив с разницами
for i in range(plays):
    Agoals, Bgoals = map(int, input().split(" ")) # 6 15, голы
    # дальше workers чисел
    teams=list(map(int, input().split(" ")))
    for j in range(0,5):
        mas[teams[j]] += Agoals - Bgoals
    for j in range(5,10):
        mas[teams[j]] += Bgoals - Agoals
    ans = 0
    for i in range(1, workers):
        if mas[i] > mas[0]:
            ans += 1
    print(ans)