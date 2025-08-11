pencil_case = ["ペン", "消しゴム", "ものさし"]
print(pencil_case)

#配列に情報を追加(配列.append(追加する要素))
pencil_case.append("えんぴつ")
print(pencil_case)

print(pencil_case[0])

pencil_case[1] = "修正ペン"
print(pencil_case)

pencil_case.append("筆箱")
print(pencil_case)
print(len(pencil_case))

ride_count = 0
friends = []

friend = {}
print("お友達のお名前は？")
friend["name"] = input()
print("お友達の身長は？")
friend["height"] = int(input())
friends.append(friend)
ride_count += 1

friend = {}
print("お友達のお名前は？")
friend["name"] = input()
print("お友達の身長は？")
friend["height"] = int(input())
friends.append(friend)
ride_count += 1

friend = {}
print("お友達のお名前は？")
friend["name"] = input()
print("お友達の身長は？")
friend["height"] = int(input())
friends.append(friend)
ride_count += 1

print(f"乗車するのは{ride_count}人です")