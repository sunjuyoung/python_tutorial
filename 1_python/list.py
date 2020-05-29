subway = ['유재석','케이']

print(subway)

num_list = [1,5,6,7,4]
num_list.sort()

print(num_list)
# reverse
num_list.reverse()
print(num_list)

#clear

#리스트 확장
subway.extend(num_list)
print(subway)


cabinet ={3:'유재석',99:'김연아'}
print(cabinet[3])
print(cabinet[99])
print(cabinet.get(99))

# print(cabinet[4]) 오류 프로그램종료
print(cabinet.get(4))  # none
print(cabinet.get(5,'사용가능'))
print('hi')
print(cabinet)

# in 사전 값 확인
print(3 in cabinet) # true
print(4 in cabinet) # false

cabinet1 = {'A-3':"유재석",'B-1':"김연아"}
print(cabinet1['A-3'])

cabinet1["C-2"] = "손흥민"
print(cabinet1)
cabinet1["C-2"] = "케이"
print(cabinet1)

#삭제
del cabinet1["C-2"]
print(cabinet1)

#key 출력
print(cabinet1.keys())

#value 출력
print(cabinet1.values())

#쌍으로 출력
print(cabinet1.items())

cabinet1.clear()
print(cabinet1)