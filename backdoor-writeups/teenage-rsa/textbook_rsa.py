'''Textbook RSA calculations
Requires Python2'''

def egcd(a,b):
    '''Extended Euclidean algorithm'''
    x,y,u,v = 0,1,1,0
    while a != 0:
        q,r = b//a,b%a
        m,n = x-u*q,y-v*q
        b,a,x,y,u,v = a,r,u,v,m,n
    return b,x,y

def modinv(a,m):
    '''Modular multiplicative inverse'''
    g,x,y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x%m

def rsa_decrypt(p,q,c,e,text_out=True):
    '''Calculate plaintext m from ciphertext c based on e, p and q'''
    n = p * q
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    m = pow(c,d,n)
    if text_out:
        plaintext = hex(m)[2:].rstrip('L')
        if len(plaintext) % 2 == 1:
            plaintext = '0' + plaintext
        return plaintext.decode('hex')
    else:
        return m
