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