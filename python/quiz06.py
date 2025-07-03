cost = int(input("음식의 가격"))
tip_rate = 0.1
tip = cost * tip_rate
total_cost = cost + tip
message = "음식 전체 가격은 %d원입니다. 팁은 %d입니다."
print(message % (total_cost, tip))