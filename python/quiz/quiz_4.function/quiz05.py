def CheckPass(p):
    if len(p)<8:
        return "비밀번호는 8자 이상이어야 합니다."
    if p.isalpha() or p.isdigit():
        return "비밀번호는 영문자와 숫자를 혼합해야 합니다."
    if p.islower() or p.isupper():
        return "비밀번호는 대문자와 소문자를 혼합해야 합니다."
    return "비밀번호가 안전합니다."

password = input("비밀번호를 입력하세요: ")
print(CheckPass(password))

while CheckPass(password) !="비밀번호가 안전합니다.":
    password = input("비밀번호를 다시 입력하세요: ")
    print(CheckPass(password))
