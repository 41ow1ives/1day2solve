# 이진수로 만드는 함수
def to_bin(n,num):
    ans = ''
    for i in range(n):
        ans = str(num%2)+ans
        num //= 2
    return ans

def solution(n, arr1, arr2):
    
    # 이진수로 바꾸기
    arr1 = [to_bin(n,i) for i in arr1]
    arr2 = [to_bin(n,i) for i in arr2]
    answer = []
    
    for i in range(n):
        pw=''
        for j in range(n):
            if arr1[i][j]=="1" or arr2[i][j]=="1":
                pw += "#"
            else :
                pw +=" "
        answer.append(pw)
    return answer

# 참고 - 비트연산 사용
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

