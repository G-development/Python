def fattoriale(num):
    #iterativa, forumula n(n-1)/2
    if num == 1:
        return num
    else:
        res = num * fattoriale(num-1)
        return res

def fibonacci(num):
    #iterativa, n1=1, n2=2 -> n3= n1+n2
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)