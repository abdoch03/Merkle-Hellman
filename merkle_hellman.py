import random
from math import gcd

def seq() :
    seq = []

    seq.append(2)
    max=2
    for i in range( 1, 8):
        next = random.randint(max+1,max+10)
        max = max + next
        seq.append(next)
    max = max + random.randint(0,10)
    return seq,max

def find_n(m):
    for i in range(int(m/2),m):
        if gcd(i , m )==1:
            return i

def mod_inverse(a, m) :
    if gcd(a,m)==1 :
       i=1
       while ((a*i)%m)!=1:
           i=i+1
       return i
    else:
        return "impossible"

def clé_publique(seq,m,n):
    key=[]
    for i in range(len(seq)):
        key.append((seq[i]*n)%m)
    return key

def encrypt(message, w):
    cipher = []
    for i in range(len(message)):
        num = 0
        binary_char = format(ord(message[i]), '08b')
        for j in range(8):
            if binary_char[j] == '1':
                num += w[j]
        cipher.append(num)
    return cipher



def decrypt(cipher , seq , m ,n):
    n_inverse = mod_inverse(n,m)
    res=''
    for i in cipher:
        char = []
        C= ( i * n_inverse ) % m
        for j in range(len(seq)):
            if C >= seq[len(seq)-1-j]:
                char.append('1')
                C=C-seq[len(seq)-1-j]
            else:
                char.append('0')
        char.reverse()
        res= res + to_char(char)
    return res


def to_char(tab):
    binary_str = ''.join(tab)
    ascii_value = int(binary_str, 2)
    return chr(ascii_value)

mes = "SALUT"
print(mod_inverse(17,3120))





