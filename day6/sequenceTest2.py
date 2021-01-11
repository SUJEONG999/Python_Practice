list1 = [10, 20, 30, "가나다", "abc", "A", True, 10, 20, 10]
print(list1)
print("---in과 not in 연산자---")
print('30' in list1)   # 30 문자열 존재하는지
print(30 not in list1)   # 존재하니깐 False
print(True in list1)
print(False not in list1)
print("---시퀀스연산---")
list2 = ["파","이","썬"]
print(list1+list2)
print(list1)
print(list2)
print(list2 * 3)
print("---인텍싱과 슬라이싱---")
print(list2[0]); print(list2[1]); print(list2[2]); print(list2[-1])
print(list1[:])
print(list1[::1])
print(list1[::2])
print(list1[::-1])
print(list1[0:4:1])
print("---함수들---")
print(len(list1))  # 데이터의 갯수
#print(max(list1)); print(min(list1))
print(max([10,20, 30])); print(min([10, 20,30]))
print(max(['a', 'b', 'c'])); print(min(['a', 'b', 'c']))
print(max([True, False])); print(min([True, False]))
print(list1.count(10))
print(list1.count(20))
print("---for와 함께 사용하는 시퀀스---")
for data in list2 :
    print("#", data, "#")
print("---리스트는 변경가능---")
list2[0] = "가"
print(list2)
list2[0:1] = "파"
print(list2)
list2[0:0] = "가"  # 맨앞에 삽입
print(list2)
list2[0:2] = "나"  # 1,2번째 대신 나
print(list2)
list2[0:2] = [10, 20, 30, 40, 50, 60, 70]  # 원래 리스트 값 대신에 원소로 들어가게됨.
print(list2)
list2[0] = [10, 20, 30, 40, 50, 60, 70]   # 서브리스트로 들어감
print(list2)
del list2[0]
print(list2)
del list2[0:3]
print(list2)
r1 = list2.remove("썬")  # 있으면 삭제, 없으면 삭제 X
print(list2)
print(r1)
#list2.remove("썬")
#print(list2)
r2 = list2.pop()   #
print(list2)
print(r2)
list2.append("가")
print(list2)
list2.insert(1,"나")
print(list2)
list2.append([1,2,3])
print(list2)
list2.extend([1,2,3,4,5])
print(list2)