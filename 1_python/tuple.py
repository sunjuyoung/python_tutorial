menu = ("돈까스","치즈까스")
print(menu[0])

#menu.add("생선까스") 

#name = "유재석"
#age = 20
#hobby= "코딩"
#print(name,age,hobby)

name,age,hobby = "김종국",20,"코딩"
print(name,age,hobby)


#집합 set
#중복 안됨 ,순서없음

my_set={12,3,4,5,2,2,2,12}
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

#교집합  
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java  - python)
print(java.difference(python))

#추가
python.add("김태호")
print(python)

#
java.remove("김태호")
print(java)


#자료구조의 변경
menu ={"커피","우유","주스"}
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))

###

from random import *
lst = [1,2,3,4,5,6,7]
shuffle(lst)
print(lst)
print(sample(lst,1))


lott = range(1,21)
lott = list(lott)
print(lott)
shuffle(lott)

chicken = sample(lst,1)



coffee = set(lst).difference(set(chicken))


print("coffee: {}".format(list(coffee)))
#print("치킨 당첨자 :"+ chicken)
#print("커피 당첨자 : "+ coffee)