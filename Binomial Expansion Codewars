import math

def expand(expr):
    n = int(expr.split("^")[1])
    if not n:
        return "1"
    elif n == 1:
        return expr.split("(")[1].split(")")[0]
    if "-" in expr[2:]:
        ind = expr[2:].index("-")
        ind += 2
        exprab = expr.split("-")
        exprab = [expr[:ind], expr[ind:]]
        b = int(exprab[1].split(")")[0])
    else:
        exprab = expr.split("+")
        b = int(exprab[1].split(")")[0])
    a = exprab[0].split("(")[1]
    if not b:
        return f"{int(a[:-1])**n}{a[-1]}^{n}"
    answer = []
    acoeff = a[:-1]
    if acoeff == '':
        acoeff = 1
    try:
        acoeff = int(acoeff)
    except:
        acoeff = int(acoeff+"1")
    term = a[-1]
    for r in range(n+1):
        front = math.factorial(n)//(math.factorial(r) * math.factorial(n-r)) * b**r * acoeff**(n-r)
        if n-r == 1:
            degree = ""
        elif not n-r:
            degree = ""
            term = ""
        else:
            degree = f"^{n-r}"
            
        if front > 1:
            sign = "+"
        elif abs(front) == 1 and r != n:
            print(str(front))
            print(f"{str(front)[0]}")
            sign = f"{str(front)[0]}"
            front = ""
        elif front < 0:
            sign = ""
        elif not front:
            continue
        elif front == 1 and r == n:
            sign = "+"
            
        if not r:
            sign = ""
        
        answer.append(f"{sign}{front}{term}{degree}")
                          
    return ''.join(answer)
