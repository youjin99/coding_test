#피보나치 함수를 재귀 함수로 표현
def fibonacci(n):
    if n == 1 or n == 2: 
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4)) #3

#한 번 계산된 결과를 메모제이션하기 위한 리스트 초기화 
d = [0] * 100
#피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(n): 
    #종료 조건(1혹은 2일 때 1을 반환)
    if n == 1 or n == 2:
        return 1 
    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[n] != 0:
        return d[n]
    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환 
    else: 
        d[n] = fibo(n-2)+fibo(n-1)
        return d[n]
    
print(fibo(99)) #218922995834555169026

#호출되는 함수 확인 
d = [0] * 100
def pibo(n): 
    print('f('+str(n)+')',end=' ')
    if n == 1 or n == 2:
        return 1 
    if d[n] != 0:
        return d[n]
    d[n] = pibo(n-2)+pibo(n-1)
    return d[n]
    
pibo(6) #f(6) f(4) f(2) f(3) f(1) f(2) f(5) f(3) f(4)

#피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍)
d = [0] * 100
#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
