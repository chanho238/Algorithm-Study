def solution(price, money, count):
    answer = -1
    a = 0
    for i in range(1,count+1):
        a += price*i
    answer = a - money
    if answer < 0:
        return 0
    return answer