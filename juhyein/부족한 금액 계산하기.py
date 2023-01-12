def solution(price, money, count):
    
    answer = sum([i*price for i in range(1,count+1)]) - money
    
    if answer > 0 :
        return answer
    return 0
  
  
  #참고1
  def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
