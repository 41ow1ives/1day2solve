# 10:08
numbers = {"zero":"0",
          "one":"1",
          "two":"2",
          "three":"3",
          "four":"4",
          "five":"5",
          "six":"6",
          "seven":"7",
          "eight":"8",
          "nine":"9"}

def solution(s):
    answer = ""
    num = ""
    
    for i in range(len(s)):
        num += s[i]
        if num in numbers.keys() : 
            answer += numbers[num]
            num = ""
        elif num in numbers.values() :
            answer += num
            num = ""
    answer = int(answer)
    return answer
