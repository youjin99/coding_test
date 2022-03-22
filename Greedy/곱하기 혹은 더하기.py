#문자열 S 
s = input() 

#문자열 리스트로 만들기
string = []
for i in range(len(s)):
    string.append(int(s[i]))

cal = [] #계산값 
result = 0 #계산값 업데이트 

for i in string: 
    if len(cal) <= 1: #cal이 두 개 이상 전까지
        cal.append(i) #cal에 string 추가 
    else: #cal이 두 개 이상부터 
        if cal[-2] == 0 or cal[-1] == 0 or cal[-2] == 1 or cal[-1] == 1: #계산할 숫자가 0이나 1이라면 
            result = cal[-2] + cal[-1] #더하는게 더 큰 숫자가 나온다
            cal.append(result) #계산값 cal에 저장
            cal.append(i) #다음 계산할 숫자 cal에 저장 
        else: #계산할 숫자에 0이나 1이 없다면
            result = cal[-2] * cal[-1] #곱하는게 더 큰 숫자가 나온다
            cal.append(result) #계산값 cal에 저장
            cal.append(i) #다음 계산할 숫자 cal에 저장 

#마지막 값 계산 
if cal[-2] == 0 or cal[-1] == 0 or cal[-2] == 1 or cal[-1] == 1: #계산할 숫자가 0이나 1이라면 
    result = cal[-2] + cal[-1] #더하는게 더 큰 숫자가 나온다
else: #계산할 숫자에 0이나 1이 없다면
    result = cal[-2] * cal[-1] #곱하는게 더 큰 숫자가 나온다
    
print(result)
    

"""입력 예시
02984
출력 예시
576

입력 예시2
567
출력 예시2
210
"""