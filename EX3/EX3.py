

##EX3_1
def EX3_1(n):
    m=n
    print(m,end=' ')
    while m != 1:
        if m % 2 == 0:
            m /= 2
        else:
            m = 3 * m+ 1
        print(int(m),end=' ')
print("##EX3_1")
print("请输入数字：")
EX3_1(int(input()))

print()
##EX3_2
def EX3_2(p, str):
    for m in range(0,len(str)):
        ord_c=ord(str[m])+p
        print(chr(ord_c),end='')
print("##EX3_2")
print("请输入偏移量：")
p=int(input())
print("请输入字符串：")
str=input()
EX3_2(p, str)
print()

##EX3_3

def EX3_3():
    nums = {25, 18, 91, 365, 12, 78, 59}
    a = []
    print("multiplier_of_3:")
    for n in nums:
        if n % 3 == 0:
            a.append(n)
    print(a)
    print()
    
    print("square_of_odds:")
    b = set()
    for n in nums:
        if n % 2 == 1:
            b.add(n*n)
    print(b)
    print()
    
    print("sr:")
    s = [25, 18, 91, 365, 12, 78, 59, 18, 91]
    sr = dict()
    for n in s:
        sr[n] = n % 3
    print(sr)
    print()
    
    print("tr:")
    tr = dict()
    for (n,r) in sr.items():
        if r == 0 :
            tr[n] = r
    print(tr)
        
print("##EX3_3")     
EX3_3()
            
        
    
    
    
    
        