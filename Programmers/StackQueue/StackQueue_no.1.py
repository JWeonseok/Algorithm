# 210118 월 주식가격

"""
푸는 데 문제 없음
특이사항도 없음
"""

def solution(prices):
    answer=[]    
    
    for i in range(len(prices)):
        cnt=0
        curt = prices[i]
        for j in range(i+1,len(prices)):
            cnt+=1
            if curt > prices[j]:
                break
        answer.append(cnt)
    
    return answer

print(solution([1,2,3,2,3]))