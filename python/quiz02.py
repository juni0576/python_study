chi_leg=2
cow_leg=4
pig_leg=4

num_chi=int(input("닭의 수를 입력하세요"))
num_cow=int(input("소의 수를 입력하세요")) 
num_pig=int(input("돼지의 수를 입력하세요"))
total_legs = (num_chi * chi_leg) + (num_cow * cow_leg) + (num_pig * pig_leg)
print(f"총 다리의 수는 {total_legs}개 입니다.")