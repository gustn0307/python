def solution(queue1, queue2):
    answer = -2
    allSum = int(sum(queue1) + sum(queue2))/2
    n=len(queue1)
    temp=list()
    e=0
    cnt=0

    if (sum(queue1) + sum(queue2))%2==1:
        answer=-1
        return answer

    for i in range(2*n):          
        if sum(queue1) > sum(queue2):
            temp=list(reversed(queue1))
            e=temp.pop()  # pop
            queue1=list(reversed(temp))
            queue2.append(e) # insert
            cnt+=1     
        elif sum(queue1) < sum(queue2):
            temp=list(reversed(queue2))
            e=temp.pop()  # pop
            queue2=list(reversed(temp))
            queue1.append(e) # insert 
            cnt+=1

        if i == (2*n - 1) and sum(queue1) == sum(queue2):
            answer=-1
            return answer
    answer=cnt

    return answer
    
q1=[3, 2, 7, 2]
q2=[4, 6, 5, 1]
print(solution(q1,q2))