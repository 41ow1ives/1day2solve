# 효율성 테스트 3,4 실패
def solution(phone_book):

    phone_book = sorted(phone_book, key = lambda x : len(x))

    for idx, num in enumerate(phone_book):
        if idx == len(phone_book)-1 : return True
    
        else:
            pre = [p[:len(num)] for p in phone_book[idx+1 : ]]
            if num in pre: return False
