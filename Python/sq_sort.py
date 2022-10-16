def SortedSquares(nums):
    neg_s=[]
    pos_s=[]
    neg=True
    for i in nums:
        if neg:
            neg_s.append(i*i)
            if i>=0:
                neg= False
        else:
            pos_s.append(i*i)
    i,j=0,len(neg_s)-1
    n=len(pos_s)
    ans=[]
    while i<n and j>=0:
        if pos_s[i]<neg_s[j]:
            ans.append(pos_s[i])
            i+=1
        else:
            ans.append(neg_s[j])
            j-=1
    while i<n:
        ans.append(pos_s[i])
        i+=1
    while j>=0:
        ans.append(neg_s[j])
        j-=1
    return ans

print(SortedSquares([-7,-3,2,3,11]))