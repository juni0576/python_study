num = input("100,000에서 999,999사이의 숫자를 입력하시오")
ln=list(num)
ln.insert(-3, ',')
num2 = ''.join(ln)
print("원하신 그 숫자가 이게 맞나요?",num2)

# gpt가 알려준 겁나 간단한 답
# print(f"입력받은 값은 {int(num):,}")

#12번 문제풀이. 2가지가 핵심. if, print문 조합
# num = int(input("숫자를 입력하시오 : "))
# if num >=100000 and num<1000000:
#     moreT = num//1000
#     lessT = num%1000
#     print(moreT,",",lessT)
#     print(f"{moreT},{lessT}")
#     print(str(moreT)+","+str(lessT))
#     print("%d,%d" %(moreT,lessT))
# else:
#     print("숫자가 범위 밖에 있습니다.")