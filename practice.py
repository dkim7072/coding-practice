# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
# print('풍선')
# print("나비")
# print("ㅋ"*9)
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not ( 5>10))

#애완 동물을 소개해주세요
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# '''
# 이렇게 하면 주석
# 처리가 됨

# '''
# print('우리집 ' +animal+" 의 이름은 " + name + "입니다. ")
# hobby = "공놀이"
# print(name +"는 "+ str(age) + "살이며, " + hobby + "을 좋아합니다")
# print(name +"는 어른일까요" + str(is_adult))

# station1= "사당"
# station2 = "신도림"
# station3 = "인천공항"

# print(station1+ "행 열차가 들어오고 있습니다")
# print(station2+ "행 열차가 들어오고 있습니다")
# print(station3+ "행 열차가 들어오고 있습니다")

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3) #2의 3승 즉 2*2*2
# print(5%3) #5 나누기 3을 하고 남은 나머지 값
# print(10%3)
# print(5//3)#5를 3으로 나누었을때 몫
# print( 10 > 3)
# print( 10 >= 30)

# print(3 == 3) #앞과 뒤의 값이 똑같은지 확인
# print(4 == 3)
# print(3 +4 == 7)
# print(1 != 3) # !+는 앞뒤가 같지 않다
# print(not(1 != 3))

# print((3 > 0) and (3<5))
# print((3 > 0) & (3<5))
# print()
# print((3 > 0) or (3>5))
# print((3 > 0) | (3<5))
# print( 5 > 4> 3)
# print( 5 > 4> 7)

# print( 2 + 3 * 4)
# print((2 + 3) *4)
# number = 2 + 3 *4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *=2 
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)

# number %= 5
# print(number)
# print(abs(-5)) # -5에 대한 절대값 즉 5가나옴
# print(pow(4,2)) # 4의 2승 즉 4^2, 4 *4  = 16
# print(max(5, 12)) #최대값 반환 즉 12 가 나옴
# print(min(5, 12))
# print(round(3.14))
# print(round(4.99))

# from math import *
# print(floor(4.99)) #4.99에서 뒤에 부분을 다 버림 즉 4 가 됨
# print(ceil(3.14))#올림값 즉 4가 나옴
# print(sqrt(16)) #제곱근 나옴. 즉 4의 제곱근 16임.

#랜덤함수
# from random import *
# print(random()) #0.0 이상 1.0이하에서 임의의 값을 생성
# print(random()*10)#0.0 이상 10.0이하에서 임의의 값을 생성
# print(int(random()*10))#0.0 이상 10.0이하에서 임의의 값을 생성 인데 뒷에 소숫점은 뺴고보고 싶을때 int로 감싸주면 됨
# print(int(random()* 10) +1)#0을 보기 싫고 1부터 보고 싶다. 즉 1부터 10까지의 임의의 숫자인데 소숫점뺴고
# print()
# print(int(random()*45)+1) #로또값 즉 1 에서 45까지에서 임의의 숫자
# print(randrange(1, 46)) # 1 -45 미만의 임의의 값 생성
# print(randint(1,45))# 1 -45 미만의 임의의 값 생성

# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월" +str(date)+"일 로 선정 되었습니다")

# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이선은 쉬워요"
# print(sentence2)
# sentence3 ="""
# 나는 소년이고
# 파이선은 쉬워요
# """
# print(sentence3)

# jumin = '990120-1234567'

# print('성별 : ' + jumin[7])
# print('연 : ' + jumin[0:2]) # 0부터 2 직전까지 즉 0,1 값
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])#처음부터 6직전
# print("둬7자리 : " + jumin[7:])#7부터 끝까지
# print("둬7자리 (뒤에서부터) : " + jumin[-7:-1])#맨뒤에서 7까지

# python ="Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace('Python', 'Java'))

# index = python.index('n')
# print(index)
# print()
# index=python.index('n', index + 1)
# print(index)
# print(python.find('java'))
# #print(python.index('java'))
# print('hi')
# print(python.count('n'))

# print('a' + 'b')
# print('a','b')

# #방법 1
# print("나는 %d살입니다." % 20)
# print('나는 %s을 좋아해요.' %"파이선")
# print('Apple 은 %c로 시작해요.' %"A")
# #%s를 사용하면
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법2

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format('파란', "빨간") )
# print("나는 {0}색과 {1}색을 좋아해요.".format('파란', "빨간") )
# print("나는 {1}색과 {0}색을 좋아해요.".format('파란', "빨간") )

#방법 3

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color=20, age="빨간"))

#방법 4
# age = 20
# color ="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# print("백문이 불여일견 \n백견이 불여일타") #\n은 문장내에서 줄바꿈
# #저는 "나도 코딩"입니다
# print("저는 '나도 코딩' 입니다")
# print('저는 "나도 코딩" 입니다')
# print("저는 \"나도 코딩\" 입니다")
# print('저는 \'나도 코딩\' 입니다')

# #역슬러쉬를 두번쓰면 \\ 문장내에서는 하나의 역슬러쉬롤 바뀜\
# print("C:\\Users\\Acer\\Desktop\\pythonworkspace")

# # \r 커서를 맨 앞으로 이동
# print("red Apple\rPine")

# # \b 백스페이스 역할 즉 한글자 삭제
# print("Redd\bApple")

# # \t 탭역할
# print("Red\tApple")

# #url = "http://naver.com"
# url = "http://daum.com"
# my_str = url.replace("http://","") #규칙1
# print(my_str)
# my_str = my_str[:my_str.index(".")] #my_str[0:5] -> 0.1.2.3.4
# print(my_str)
# password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
# print("{0}의 비밀번호는 {1}".format(url, password))
# #print("비밀번호: ", password[7:12])

#리스트 []
#지하철 칸별로 10명, 20명, 30명
# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호" ,"박명수"]
# #조세호는 몇번쨰 타고 있는가
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)
# #정형돈씨를 유재석 과 조세호 사이에 태워봄

# subway.insert(1,"정형돈")
# print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
#같은 이름의 사람이 몇명있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#정렬로 가능
# num_list = [5,2,1,3,4]
# print(num_list)

# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)
#다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# #list 가 두개 있는데 합쳐 보겠슴
# num_list = [5,2,1,3,4]
# num_list.sort()
# num_list.reverse()
# mix_list = ["조세호", 20, True]
# num_list.extend(mix_list)
# print(num_list)

#cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# #print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능"))
# print('hi')

# print(3 in cabinet) # ture
# print(5 in cabinet) #false
# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새로운 손님
# print(cabinet)
# cabinet["A-3"] = "김종국" # 키 A-3가 있으므로, 새로운값으로 대체 할것. 즉 김종국이 유재석을 덮어씀
# cabinet["C-20"] = "조세호" # 새로운 키 C-20을 추가 하는것
# print(cabinet)

# #손님이 집에 감
# del cabinet["A-3"]  #A-3에 해당하는 손님이 집에 갔으므로 키를 지워줌
# print(cabinet)


# # key 만 출력
# print(cabinet.keys())
# #value만 출력
# print(cabinet.values())

# #key. value를 쌍으로 출력
# print(cabinet.items())

# #목욕탕 영업끝
# cabinet.clear() # 모든값을 싹지움
# print(cabinet)

# menu = ("돈가스", "치즈가즈") #튜플은 내용변경 안됨. 
# print(menu[0])
# print(menu[1])
# print(menu)

#menu.add("생선가스") 에러발생. 튜플은 추가 불가능

# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name, age, hobby)
#튜플을 이용하면 한번에 선언 할 수 있음
# (name, age, hobby) = ("김종국", 20, " 코딩")
# print(name, age, hobby)

#set 집합
#중복 안되고 순서가 없음
# my_set = [1,2,3,3,3]
# print(my_set)

# jave  = {"유재석", "김태호", "양세형"}
# paython = set(["유재석", "박명수"]) #유재석은 자바에도 있고 , 파이썬에도 있음

# #교집합 즉 자바, 파이썬  다 할 수 있은 사람.

# print(jave & paython) # 유재석이 나옴.
# print(type(jave))
# print(type(paython))
# print(jave.intersection(paython))

# #합집합 (java나 파이썬 둘중 하나라도할 수 있는 사람)
# print(jave | paython)
# print(jave.union(paython))

# #차집합 (jave는 할 수 있지만파이선 못하는 사람)
# print(jave - paython)
# print(jave.difference(paython))

# #파이선을 할 줄 아는 사람이 늘어남. 
# paython.add("김태호")
# print(paython)


# #자바를 까먹었어요. 
# jave.remove("김태호")
# print(jave)a

#자료구조의 변경
# menu = {"커피", "주스", "우유"}
# print(menu, type(menu))
# print()
# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# from random import  *
# users = range(1, 21) # 1부터 20까지
# print(users, type(users))
# users = list(users)
# print(users, type(users))
# shuffle(users)
# print(users)

# winners = sample(users, 4) #  user에서 4명을 일단 뽑고 나서 1명은 치킨, 3명은 커피를 주는걸루

# print(" -- 당첨자 발료 --")
# print("치킨 당첨자 : {}".format(winners[0]))
# print("커피 당첨자 : {}".format(winners[1:]))
# print(" -- 축하합니다--")

# weather = "비"
# # if 조건: 
# #     실행 명령문
# if weather == "비":
#     print("우산 준비해")

# weather = "미세먼지"
# if 조건: 
#     실행 명령문
# elif 조건:
#     실행 명령문

# if weather == "비":
#     print("우산 준비해")
# elif weather == "미세먼지":
#     print("마스크 챙겨라")

# print()
# print()

# weather = "미세먼지"
# if 조건: 
#     실행 명령문
# elif 조건:
#     실행 명령문

# if weather == "비":
#     print("우산 준비해")
# elif weather == "미세먼지":
#     print("마스크 챙겨라")


# weather = "맑아요"
# # if 조건: 
#     실행 명령문
# elif 조건:
#     실행 명령문
# else:
#     실행 명령문

# if weather == "비":
#     print("우산 준비해")
# elif weather == "미세먼지":
#     print("마스크 챙겨라")
# else:
#     print("준비물 필요없다")

# print()

# weather = input("오늘 날씨 어떄요 ")
# if 조건: 
#     실행 명령문
# elif 조건:
#     실행 명령문
# else:
#     실행 명령문

# if weather == "비":
#     print("우산 준비해")
# elif weather == "미세먼지":
#     print("마스크 챙겨라")
# else:
#     print("준비물 필요없다")

# print()
# weather = input("오늘 날씨 어떄요 ")
# # if 조건: 
# #     실행 명령문
# # elif 조건:
# #     실행 명령문
# # else:
# #     실행 명령문

# if weather == "비" or weather == "눈":
#     print("우산 준비해")
# elif weather == "미세먼지":
#     print("마스크 챙겨라")
# else:
#     print("준비물 필요없다")

# temp = int(input('기온은 어때요? '))
# if 30 <= temp: 
#     print("너무 덥다, 집에 있어라")
# elif 10 <= temp and temp < 30:
#     print("괘안타 나가라")
# elif 0 <= temp  < 10: 
#     print("너무춥다 파카 챙겨라")
# else:
#     print("너무 춥다, 집에 있어라")
print()
print()
# print("대기번호 : 1 ")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))
# print()
# for waiting_no in range(1, 6):# 6미만까지
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]

# for customer in starbucks:
#     print("{}, 커피가 준비 되었습니다.".format(customer))

#while
#손님 다섯번 불러서 대답없음 커피 버림
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index)) #여기서 실행하면 좃됨
#     index -= 1
#     if index == 0:
#         print("커피 버렸다")
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index +=1 #요렇게 하면 무한 루프됨. ctrl+ C로 정지 시킴

# customer = "토르"
# person = "unknown"
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요 ")    
#

#선생님이 책 읽기 시킴 그런데
# absent = [2, 5] # 2번 5번은 결석
# no_book = [7] # 7번 학생은 책을 안가져옴
# for student in range(1,11): # 1부터 10번까지 한명씩 반복하면서 책읽어야 하는데
#     if student in absent: 
#         continue #만약 결석한 학생 번호에 오면 밑으로 가지 않고 위로 올라가서 다시 계속 함
#     elif student in no_book:
#         print("오늘 수업 끝이야. {0}번은 고무실로 와".format(student))
#         break #선생이 성질 드러워서 책안가져오면 수업중단하고 학생 교무실로 불러서 마구패버림
#     print("{0},번 책을 읽어봐".format(student))

#출석 번호가 1,2,3,4가 있는데 출석 번호를 101,102,103,104이런식으로 바꾸었음
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students] #student에 있는 값을 하나씩 돌리는데 거기에 100을 더해서 students에 넣어라 
# print(students)


#학생 이름을 길이로 변화
# students = ["iron man", "Thor", " I am groot"]
# students =[len(i) for i in students] # students안에 있는 내용을 하나씩 반복하면서 그 추출한 값을 길이로 변경해주는거임
# print(students)

#학생이름을 대문자로 변화

# students = ["iron man", "Thor", " I am groot"]
# students = [i.upper() for i in students]
# print(students)


# from random import *
# cnt = 0 #총 탑승 승객수
# for i in range(1, 51): # 1에서 50까지 수 . 즉 승객수
#     time = randrange(5, 51) #랜덤으로 시간이 5분에서 50사이의 시간이 소요
#     if 5 <= time <= 15: #5분에서 15분 이내의 손님, 탑승 승객 수 증가 처리 (매칭 성공)
#         print("[0] {0}번 손님 (소요시간 : {1}분)". format(i,time))
#         cnt +=1
#     else: #매칭 실패 
#         print("[] {0}번쨰 손님 (소요시간: {1}분)".format(i, time))

# print("총 탑승 승객: {0} 분".format(cnt))


#함수
#def 함수이름(): 이런식으로 함수 시작
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# #여기서 실행시키면 아무것도 안나옴
# open_account() #요렇게 함수를 실행시켜주면 프린터가 나옴

# #값을 전달하고 결과값을 받는것

# def deposit(balance, money): # 입금 -> 잔액과 지금 입금하는 함수
#     print("입금이 완료, 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money: # 잔액이 머니보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money

#     else: #잔액이 머니보다 적으면
#         print("잔액부족, 출금안됨 잔액은 {0}원 입니다".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 #수수료
#     return commission, balance-money-commission
# balance = 0 #잔액부족
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# #print(balance)
# commission, balance = withdraw_night(balance, 500)
# print("수수료{0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

#기본값 설정
# def profile(name, age, main_lang): # 프로파일 이라는 함수
#     print("이름 : {0} \t나이 : {1}\t주 사용언어: {2}" \
#         .format(name, age, main_lang))

# profile("유재석", 25, "파이선")
# profile("김태호", 30, "자바")

#만약 같은 학교, 같은 학년, 같은 반에서 같은 수업을 듣는 경우라면, 나이랑 파이선 자바 이런건 동일한것이 됨
#그래서 기본값 설정을 아래와 같이 함
# def profile(name, age= 17, main_lang="파이썬"): # 프로파일 이라는 함수
#     print("이름 : {0} \t나이 : {1}\t주 사용언어: {2}" \
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")


# #키워드 값으로 함수를 호출하는 방법
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# #보통의 경우 함수를 호출할때
# profile("유재석", 25, "파이선")
# #하지만 함수를 호출할때 순서를 바꾸어서 호출할 수 있음
# profile(name="유재석", main_lang="파이선", age= 25)
# profile(main_lang="파이선", name="김태호",  age= 25)
# #그래도 결과는 위의 초기 함수 정의한 순서대로 호출이 됨

#가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 {0}\t나이 : {1}\t".format(name, age), end=" ") #마지막에 end = " "를 사용하면 줄바꿈하지 않고 그다음 문장을 붙여씀
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# #이경우는 유재석이 5개 언어 가능
# profile("김태호", 25, "Kotlin", "Swift", "","","")
#이경우는 김태호가 2개 언어만 가능
#그런데 여기서 만약 유재석이 언어를 더 할 줄아는게 생기는 경우 즉 언어가 6개 가능한경우는 위에 함수를 수정해줘야 하는데
#이런 경우에 가변 함수를 사용함

# def profile(name, age, *language): #lang1, lang2, lang3, lang4, lang5 대신에 *language를 넣어줌
#     print("이름 {0}\t나이 : {1}\t".format(name, age), end=" ") #마지막에 end = " "를 사용하면 줄바꿈하지 않고 그다음 문장을 붙여씀
#     #print(lang1, lang2, lang3, lang4, lang5) #이것도 이렇게 할 필요가 없음 왜냐면 *language떄문에
#     for lang in language: 
#         print(lang, end = " ") #줄바꿈을 하지 않기 위해 end = ""를 넣어줌
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")#이경우는 유재석이 개 언어 가능

# profile("김태호", 25, "Kotlin", "Swift")#김태호는 2개만 가능함 그리고 뒤에 "","",""이런거 필요없음

#지역변수와 전역 변수 local , global
#군대을 예를 들어서 
# gun = 10 #총이 10개 있음 이게 global 변수

# def checkpoint(soldiers): #군바리들 경계근무나갈떄 총이 몇개 남았는지 확인 하는 함수 설정
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 :  {0}".foramt(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) #군바리 두명이 근무나감
# print("남은총 : {0}".format(gun))

#이렇게 하면 에러가 남, 왜냐면 gun 이라는 함수는 checkpoint라는 함수의 바깥에 존재하는 global 변수인데
#checkpoint라는 함수내부에 정의가 되지 않았음.그래서 gun이 몇개인지 모름.그래서 에러가 발생함
#만약에 아래와 같이 함수내에 local 변수를 설정하면
# gun = 10 #총이 10개 있음 이게 global 변수

# def checkpoint(soldiers): #군바리들 경계근무나갈떄 총이 몇개 남았는지 확인 하는 함수 설정
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 :  {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) #군바리 두명이 근무나감
# print("남은총 : {0}".format(gun))
#이게 또 많이 안되는게 처음에 print구문은 global 변수 를 땡겨옴
#그리고 checkpoint함수를 불러오면 local 변수를 이용해서 결과값은 내노움.
#마기막 남은총은 또 globla 변수를 불러와서 보여줌 그래서 이게 말이 안되서 
#아래와 같이 변경함
# gun = 10 #총이 10개 있음 이게 global 변수

# def checkpoint(soldiers): #군바리들 경계근무나갈떄 총이 몇개 남았는지 확인 하는 함수 설정
#     global gun #이렇게해서 global 변수를 불러옴
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 :  {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) #군바리 두명이 근무나감
# print("남은총 : {0}".format(gun))

# gun = 10 #총이 10개 있음 이게 global 변수

# def checkpoint(soldiers): #군바리들 경계근무나갈떄 총이 몇개 남았는지 확인 하는 함수 설정
#     global gun #이렇게해서 global 변수를 불러옴
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 :  {0}".format(gun))

# def checkpoint_ret(gun, soldiers): #함수를 하나 더 만들어군인과 총의 갯수를 확인함.
#     gun = gun - soldiers #이렇게 로커 변수를 설정해봐야 이것만 하면 에러가 남
#     print("[함수 내] 남은 총 :  {0}".format(gun))#여기서도 그냥 실행하면 에러가남 대신 밑에 gun = checkpint_rest 함수 불러오는걸 잘 봐야함
#     return gun # 이건 gun의 숫자를 받아서 global 변수에 리턴해준다 이렇게 생각하면됨
# print("전체 총 : {0}".format(gun)) #이건 global 변수를 불러오니까 10개임
# #checkpoint(2) #군바리 두명이 근무나감
# gun = checkpoint_ret(gun, 2) #함수를 실행시키는데 여기서 gun의 숫자가 계싼이 됨
# print("남은총 : {0}".format(gun))

# print()
# def std_weight(height, gender): #키는 m 단위, 성별은 "남자"/ "여자"
#     if gender == "남자":
#         return height * height *22
#     else:
#         return height * height *21


# height = 175 #cm 단위
# gender = "남자"
# weight = round(std_weight(height /100 , gender), 2) #키단위가 cm 이므로 100을 나눠서 m로 바꾸어주어야 함
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# import sys
# print("Python", "Java")
# print("Python", "Java", sep=" vs ")
# print("Python", "Java", sep=",", end="?") #문장의 끝부분을 ?로 바꿔달라
# print("무엇이 더 잼나니?")
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)


# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

#은행 대기 순번표
# #001, 002, 003,....
# for num in range(1, 21):
#     print("대기번호 :" + str(num).zfill(3))

# answer = input("아무거나 써라 : ")
# print(type(answer))
#10
# print("입력하신 값은 : " + answer + "입니다")

# #빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) #오른쪽으로 10자리 공간 확보하고 500울 출력하라는 소리

# print("{0: <10}".format(500))
# #양수일떄는 +로 표시, 음수일떄는 -로 표시
# print("{0: <+10}".format(500))
# print("{0: >+10}".format(-500))

# #.왼쪽 정렬을 하고 빈칸을 밑줄로 채움
# print("{0:_<+10}".format(500))
# #3자리 마다 콤마 찍어 주기
# print("{0:,}".format(1000000000))
# #3자리 마다 콤마 찍어 주기 + - 부호도 붙이기
# print("{0:+,}".format(1000000000))
# print("{0:+,}".format(-1000000000))
# #3자리 마다 콤마 찍어주고 부호도 붙이고 자릿수 확보
# #eㄷ 돈이 많으면 행복하니 빈자리는 ^로 채워줌
# print("{0:^<+30,}".format(100000000000))
# #소숫점 출력
# print("{0:f}".format(5/3))
# #소숫점을 특정 자리수 까지만 표시 (소숫점 3자리에서 반올림)
# print("{0:.2f}".format(5/3))

# score_file = open("score.txt", "w", encoding="utf8") # w 는 덮어쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a는 이어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #r 읽어 오기
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #한줄씩 읽어오고 커서는 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#파일에 내용이 얼마나 있는지 모를경우 while을 이용해서 하나씩 불러 올수 있음.
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline() #라인을 "하나"씩 가져오는거
#     if not line:
#         break
#     print(line)
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()#list 형태로 저장 즉 스코어 파일에 있는 모든 라인을 가져와서 lines라는 변수에 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

#피클 pickle

# from ctypes.wintypes import HPALETTE
# import pickle
# profile_file = open("profile.pickle", "wb") #피클에서는 인코딩을 표현안해도 됨. wb는 쓰기 랑 바이너리.
# profile = {"이름" : "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

#파일을 읽어오기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile로 불러 오기
# print(profile)
# profile_file.close()

# import pickle
# with open("profile.pickle", 'rb') as profile_file:  #profile.pickle이라는 파일을 열어서 profile_file이라는 변수로 저장함
#     print(pickle.load(profile_file)) #파일의 내용을 피클의 load를 통해서 불러와서 출력을 해주는것임


# with open("study.txt", "w", encoding="utf8") as study_file : #study.txt라는 파일을 생성해서 study_file이라는 변수에저장
#     study_file.write("파이선을 열라 공부하고 있음") #study_file이라는 변수에 write라는 함수를 이용해서 내용을 적어주면됨

#위의 파일을 읽어 오는 방법
# with open("study.txt", "r", encoding="utf8") as study_file: #study.txt에 있는 내용을 읽어와서 study_file이라는 변수에 저장
#     print(study_file.read()) #study_file에 있는 내용을 read라는 함수를이용해서 읽어오는것

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")


# #마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" #유닛의 이름
# hp = 40 #유닛의 체력
# damage = 5  #유닛의 공격력

# print("{0} 유닛이 생성 되었습니다." .format(name))
# print("체력 {0}, 공격력 {1} \n".format(hp, damage))


# #탱크: 공격 유닛, 탱크, 포를 쏠 수 있는데 , 일반 모드  /시즈 모드
# tank_name  = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성 되었습니다." .format(tank_name))
# print("체력 {0}, 공격력 {1} \n".format(tank_hp, tank_damage))

# tank2_name  = "탱크2"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성 되었습니다." .format(tank2_name))
# print("체력 {0}, 공격력 {1} \n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" .format( \
#         name, location, damage))
# #함수 호출
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)


#위와 같이 할 수 있지만 만약에 tank가 하나 더 생기면 계속 해서 추가 해줘야함. 이런경우에 class를 사용하면 
#쉽게 할 수 있음.

# class Unit: #class라고 쓰고  class 이름을 써줌
#     def __init__(self, name, hp, damage): # class 안에 함수를 만드는데 __init__ 을 기본으로 self가 들어가 나머지 변수들
#         self.name = name # 앞에 self쓰고 점찍고 변수 이름
#         self.hp = hp 
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린1", 40, 5) # 마린이라는 변수를 만들고 클라스 이름 쓰고 안에 self를 제외한 내용을 넣어줌
# marine2 = Unit("마린2222", 40, 5)
# tank= Unit("탱크", 150, 35)
# print()
# print()
#__init__ 생성자 클래스로 부터 만들어지는건 객체. 마린, 탱크는 유닛 클래스이 인스턴스
#멤버 변수는 클래스네애서 정의된 변수

# #레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스1", 80, 5) #이렇게 하면 클래스에 정의 된 내용을 출력함 
# print("유닛 이름 :  {0},  공격력 : {1}" .format(wraith1.name, wraith1.damage) )
# #위의 내용은 클래스 바깥에서 출력을 하지만 클래스에서 정의된 변수를 불러와서 출력을 해줌.
# print()
# print()
# #마인트 컨트롤: 상대방 유닛을 내것으로 만드는것 (뺴앗음)
# wraith2 = Unit("레이스2222", 80, 5)
# wraith2.clocking = True
# #clocking이라는 변수는 클래스에 없으나 외부에서 변수를 만들어서 쓸 수 있음. 그 변수는 정의한 변수에만 사용. 기존의 변수에는 사용 못함

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다. " .format(wraith2.name))
# #일반 유닛
# class Unit: #class라고 쓰고  class 이름을 써줌
#     def __init__(self, name, hp, damage): # class 안에 함수를 만드는데 __init__ 을 기본으로 self가 들어가 나머지 변수들
#         self.name = name # 앞에 self쓰고 점찍고 변수 이름
#         self.hp = hp 
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# #공격유닛

# class Attackunit:
#     def __init__(self, name, hp, damage): # class 안에 함수를 만드는데 __init__ 을 기본으로 self가 들어가 나머지 변수들
#         self.name = name # 앞에 self쓰고 점찍고 변수 이름
#         self.hp = hp 
#         self.damage = damage

#     def attack(self, location): #클래스 안의 매소드에는 항상 self를 적어 줘야 함.
#         print("{0} : {1} 방향으로 적군을 공격 합니다 . [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다. ".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다. ".format(self.name))

# #메딕: 의무병 즉 공격 능력이 없음


# #파이어뱃, 공격유닉, 화염방사기
# firebat1 = Attackunit("파이어뱃", 50, 16)  
# firebat1.attack("5시")  
# #공격을 두번 ㅏㄷ음
# firebat1.damaged(25)
# firebat1.damaged(25)

#상속에 대해서 알아보자
#일반 유닛 즉 공격력(damage)가 필요 없는 경우가 있음. 의무병같은경우
# class unit: 
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
# #공격유닛을 만들떄 위의 일반 유닛을 상속 받아서 사용가능
# class attackUnit(unit): #공격유닛을 만드는데 위의 일반 유닛의 이름과 hp를 상속을 받음
#     def __init__(self, name, hp, damage):
#         unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location): #클래스 안의 매소드에는 항상 self를 적어 줘야 함.
#         print("{0} : {1} 방향으로 적군을 공격 합니다 . [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다. ".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다. ".format(self.name))

# #메딕: 의무병 즉 공격 능력이 없음


# #파이어뱃, 공격유닉, 화염방사기
# firebat1 = Attackunit("파이어뱃", 50, 16)  
# firebat1.attack("5시")  
# #공격을 두번 ㅏㄷ음
# firebat1.damaged(25)
# firebat1.damaged(25)

# #상속에 대해서 알아보자

# from random import *

# #일반 유닛 즉 공격력(damage)가 필요 없는 경우가 있음. 의무병같은경우
# class Unit: 
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         #print("[지상 유닛 출동]")
#         print("{0} : {1} 방향으로 이동 합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다. ".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다. ".format(self.name))

# #공격유닛을 만들떄 위의 일반 유닛을 상속 받아서 사용가능
# class AttackUnit(Unit): #공격유닛을 만드는데 위의 일반 유닛의 이름과 hp를 상속을 받음
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location): #클래스 안의 매소드에는 항상 self를 적어 줘야 함.
#         print("{0} : {1} 방향으로 적군을 공격 합니다 . [공격력 {2}]"\
#             .format(self.name, location, self.damage))

# #마린 클래스
# class Marin(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

# #스팀팩: 일정시간 동인, 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} :스팀팩을 사용 합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족해서 스팀팩을 사용 못합니다. (HP 10 감소)".format(self.name))

# #탱크 글래스
# class Tank(AttackUnit):
#     #시즈 모드: 탱크를 지ㅣ상에 고정시켜  공격력 향상
#     seize_developed = False #시즈 모드 개발 여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False: 
#             return
#         #현재 시즈모드가 아닐떄는 시즈모드로 만들어줌
#         if self.seize_mode == False:
#             print("{0}  : 시즈모드로 전환 합니다. ".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
            
#         else:  #시즈 모드일떄는 시즈 모드 해제
#             print("{0}  : 시즈모드 해제 합니다. ".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# #공중공격 유닛 클래스



# #메딕: 의무병 즉 공격 능력이 없음


# # #파이어뱃, 공격유닉, 화염방사기
# # firebat1 = attackUnit("파이어뱃", 50, 16)  
# # firebat1.attack("5시")  
# # #공격을 두번 ㅏㄷ음
# # firebat1.damaged(25)
# # firebat1.damaged(25)


#  #다중 상속


# #날수 있는 기능 가진 클래스

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable): #다중상속 받음. 두 클래스에서 제공하는 모든것을 사용가능
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)#지상 스피드는 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         #print("[공중 이동 유닛]")
#         self.fly(self.name, location)


# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,"레이스", 80, 20, 5)
#         self.clocked = False #클로킹모드(해제 상태)

#     def clocking(self):
#         if self.clocked == True: #클로킹 모드 이므로 모드 해제
#             print("{0}  : 클로킹 모드 해제합니다. ".format(self.name))
#             self.clocked = False
#         else: # 클로킹 모드 해제 이므로 클로킹 모드로 전환
#             print("{0}  : 클로킹 모드 설정합니다. ".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임 시작합니다")

# def game_over():
#     print("Player : gg") # good game
#     print("[Player] 님 퇴장하셨습니다")

# #실제게임 진해
# game_start()

# #마린 3개 생성

# m1 = Marin()
# m2 = Marin()
# m3 = Marin()

# #탱크 생성
# t1 = Tank()
# t2 = Tank()

# #레이스 생성
# w1 = Wraith()

# #유닛 일괄 관리(생성된 모든 유닛을 append 처리)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)


# #전군 이동
# for unit in attack_units:
#     unit.move("1시")

# #탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")


# #공격 모드 준비 (마리: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marin):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit,Wraith):
#         unit.clocking()

# #전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# #전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21))#공격은 랜덤으로 5 에서 20 사이에 받음

# #게임 종료
# game_over()

# #발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# # valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# # valkyrie.fly(valkyrie.name, "3시")

# # #벌쳐 : 지상 유닛, 기동성이 좋음
# # vulture = AttackUnit("벌쳐", 80, 10, 20)

# # #베틀 크루저: 공중 유닛, 체력도 굉장히 좋ㅇㅁ. 공격력도 좋음

# # battlecruiser = FlyableAttackUnit("베틀크루저", 500, 25,3)
# # vulture.move("11시")
# # #battlecruiser.fly(battlecruiser.name, "9시")
# # battlecruiser.move("9시")

# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):

#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def  show_detail(self):     
            
#             print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# houses = [ ]
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2010년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house2)


# print("총 {0}대의 매물이 있습니다".format(len(houses)))
# for house in houses:
#     house.show_detail()

# try:
#     print("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("첫번쨰 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번쨰 숫자를 입력하세요: ")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다. ")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알수없는 에러가 발생하였습니다.")
#     print(err)
    
# try:
#     print("한자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫번쨰 숫자를 입력하세요"))
#     num2 = int(input("두번쨰 숫자를 입력하세요"))
#     if num1 >=10 or num2 >=10:
#         raise ValueError
#     print("{0} / {1} = {2} ".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")

#사용자 정의 에러

# class BigNumberError(Exception):
#     pass

# try:
#     print("한자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫번쨰 숫자를 입력하세요"))
#     num2 = int(input("두번쨰 숫자를 입력하세요"))
#     if num1 >=10 or num2 >=10:
#         raise BigNumberError
#     print("{0} / {1} = {2} ".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
# except BigNumberError:
#     print("잘못된 값을 입력하였습니다!!. 한 자리 숫자만 입력하세요")



# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫번쨰 숫자를 입력하세요"))
#     num2 = int(input("두번쨰 숫자를 입력하세요"))
#     if num1 >=10 or num2 >=10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2} ".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("잘못된 값을 입력하였습니다!!. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")


# class SoldOutError(Exception):
#     pass
# chicken = 10
# waiting = 1

# while(True):
#     try:
#         print("[남은 치킨 : {0}".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까 ?"))
#         if order > chicken: #남은 치킨보다 주문이 많을 경우
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0} ] {1} 마리 주문이 완료되었습니다." \
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError

#     except ValueError:
#         print("잘못된 값을 입력하셨습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다. ")
#         break

# import Theather_moudle
# Theather_moudle.price(3) #3명이 영화 보러 갔을떄
# Theather_moudle.price_solider(3)
# Theather_moudle.price_morning(3)

# import Theather_moudle as mv
# mv.price(3)
# mv.price_morning(3)
# mv.price_solider(3)

# from Theather_moudle import *
# #from randm import 
# price(3)
# price_morning(3)
# price_solider(3)

# from Theather_moudle import price, price_morning
# price(2)
# price_morning(2)

# from Theather_moudle import price_solider as price
# price(3)

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.details()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.details()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.details()

# from random import *
# from travel import *
# # # #trip_to = vietnam.VietnamPackage()
# # trip_to = thailand.ThailandPackage()
# # trip_to.details()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())
#,내장 함수
# language = input("무슨 언어를 좋아 하세요")
# print("{0}은 아주 좋은 언어 입니다.".format(language))

#dir 어떤 객체를 넘겨줬을떄 그 객체가 어떤 변수와 함수를 가지고 있는 푯
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# list = [1,2,3]
# # print(dir(list))

# name = "Jim"
# print(dir(name))

#외장 함수
#glob :경로 내의 폴더 / 파일 목록 조회(원도우dir)
# import glob
# print(glob.glob("*.py"))#확장자가 py 인 모드 파일

# os 운영체계에서 제공하는 기본 기능
# import os
# # print(os.getcwd) #현재디렉토리

# # folder = "sampe_dir"
# # if os.path.exists(folder):
# #     print("이미 존재하는 폴더 입니다")
# #     os.rmdir(folder)
# #     print(folder, "폴더를 삭제 하였습니다.")
# # else:
# #     os.makedirs(folder) #폴더 생성
# #     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())#
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는", datetime.date.today())

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)

import byme
byme.sign()




