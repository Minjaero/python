#a = input()
#a = float(a)
#print(a)
#print(a)
#print(a)    #-3/24

#a , b = input().split()
#print(a)
#print(b)    # - 3/25

#a , b = input().split()
#print(b , a)    

#a = input()
#print(a, a, a) #0326
# 버블 정렬의 범용성을 높이기 위해 함수로 만듬
#def bubbleSort(arr):
#    n = len(arr) # 배열의 크기를 측정

    # 배열의 크기만큼 반복
#    for i in range(n):
        
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
#        for j in range(0, n - i - 1):
            
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
#            if arr[j] > arr[j + 1]: 
 #               arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환

# 예시 배열
#arr = [64, 34, 25, 12, 57, 93, 1, 123]

#bubbleSort(arr)

#print("[Sorted array is]")
#for i in range(len(arr)):
#    print("%d " %arr[i], end = "") 3/31

#a,b = input().split(':')
#print(a,b,sep=':')      # 4/2

#y,m,d = input().split('.')
#print(d,m,y,sep = '-')   #4/4

#num = input()
#print(num.replace("-",""))  #4/7

#word = input()
#for i in word:  
#    print(i)       #4/8

#YMD = input()
#Y = YMD[:2]   # [A:B] -> A이상 B미만 [A,B)
#M = YMD[2:4]  # YMD[2:4] -> YMD의 2번째부터 3번째 원소
#D = YMD[4:]

#print(Y, M, D)     # 4/9

#H, M, S = input().split(":")
#print(M)                        # 4/11

#word1, word2 = input().split()
#print(word1 + word2)            #4/14

#num1, num2 = input().split()
#num1 = int(num1)
#num2 = int(num2)
#print(num1 + num2)                  #4/15

#num1 = input()
#num2 = input()

#result = float(num1) + float(num2)
#print(result)                      #4/16

#dec = int(input())
#print("%x" %dec)                    #4/17

#dec = int(input())
#print("%X" %dec)                     #4/18

#print('I said "Hello" to you')
#print("Let's go")

#w = int(input("삼각형의 밑변 길이:"))
#h = int(input("삼각형의 높이:"))
#area = w * h /2
#print("삼각형의 면적" , area)

#h = int(input("현재 시:"))
#m = int(input("현재 분:"))
#m = m + 20
#h = (h+m // 60) % 24
#m = m % 60
#print("20분 뒤에는 %d시 %d분 입니다." %(h,m))

#num = int(input("숫자입력:"))
#if num < 0:
#    num = -1 * num
#print(num)

#id = input("아이디를 입력하세요:")
#level = int(input("레벨을 입력하세요:"))
#if id == 'admin' or level == 1:
#    print("관리자 입니다.")
#else :
#    print('관리자가 아닙니다.')

#a = int(input("첫번째 수:"))
#b = int(input("두번째 수:"))
#c = int(input("세번째 수:"))

#max = a
#if max < b:
#    max = b
#if max < c:
#    max = c
#    print('가장 큰 수는', max, "입니다.")

#age = int(input("나이입력:")) 
#if age <= 7:
#    print("어린이")
#elif age <= 13:
#    print("초등학생")
#elif age <= 16:
#    print("중학생")
#elif age <= 19:
#    print("고등학생")
#else:
#    print("성인")

#num = int(input("숫자입력:"))
#while num != 0:
#    print(num % 10, end = ' ')
#    num = num //10

#import random

#cnt = 0
#guess = 0
#answer = random.randint(1,100)
#print('정답:', answer)
#print('1부터 100까지의  숫자를 맞히기')

#while answer != guess:
#    guess = int(input("숫자를 맞혀보세요:"))
#    cnt += 1
#    if guess > answer:
#        print("높음")
#    elif guess < answer:
#        print("낮음")
        
#print("축하합니다. 시도횟수 =" , cnt)

#n = input()
#hex = int(n, 16)

#print("%o" %hex)            # 4/20

#c = ord(input())
#print(c)                    #4/21

#n = int(input())
#print(chr(n))                #4/22

#n = int(input())
#print(-n)                      #4/23  

#s = ord(input())
#print(chr(s+1))               #4/24