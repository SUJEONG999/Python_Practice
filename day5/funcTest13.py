salerate = 0.9  # 함수 밖에서 만들어진 변수 : 전역변수, 한번 만들어지면 프로그램 끝날 때까지 계속 사용.(여러함수에서 공통적 으로 사용하는 경우)
                # 처음 만들어지는 것라서 초기화 한다 표현
def kim():
    print("오늘의 할인율 :", salerate) # r-value(값) --> 지역변수가 없으면 전역변수를 찾아서 사용
                                    # 전역 변수도 없으면 error.
def lee():
    price = 1000   # 함수안에서 만들어진 변수 : 지역변수, 함수를 벗어나면 더이상 쓸수 없음. 함수 내에서만
    print("가격 :", price * salerate)  # r-value(값)

kim()  # 함수는 호출이라는 과정을 거쳐야만 수행이되는 것임.
salerate = 1.1   # salerate 에 1.1을 할당함(대입함)  --- 처음x 라서 초기화 x
lee()   # 1000*1.1
################
price = 1000    # 전역변수

def sale():
    price = 500     # l-value(값) --> 지역변수를 새로 만들게 된다.
    print(price)    # r-value(값) --> 지역변수가 있으므로 지역변수 사용

sale()   # 지역변수를 가져와서 수행됨.
print(price)   # 지정함수가 아니라서 전역변수를 가져와서 수행됨.