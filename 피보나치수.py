def solution(n):
    answer = 0
    dp=[0,1]+[0]*(n-1)
    
    if n==1: return 1
    
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    answer=dp[n]%1234567
    return answer