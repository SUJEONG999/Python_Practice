print("*입력한 숫자만큼 데코문자를 출력하는 프로그램입니다.*")
for i in range(3):  # 3번 반복하고 싶다.
    deco = input("데코문자를 입력하세요 : ")
    number = int(input("출력횟수를 입력하세요 : "))
    for i in range(number):
        print(deco, end="")
    print()
print("\n*수행 종료됩니다.*")