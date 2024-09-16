#eltelt hónapok (1.hónap - megnő a nyúl pár, 2.hónap - párosodnak, 3.hónap - születik k új nyúl pár)
n = 5
#születő nyúlpárok száma
k = 3

def rabbitpop(n,k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return rabbitpop(n-2,k) * k + rabbitpop(n-1,k)
print (rabbitpop(5,3))

#bottom up módszer, kevesebbet kell számolnia a gépnek
def bottomup_rabbitpop(n,k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    bottomup_list = [None] * (n+1)
    bottomup_list[0] = 0
    bottomup_list[1] = 1
    for i in range(2, n+1):
        bottomup_list[i] = bottomup_list[i-1] + bottomup_list[i-2]*k
    return bottomup_list[n]
print(bottomup_rabbitpop(5,3))