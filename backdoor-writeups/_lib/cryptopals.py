# coding=UTF-8
'''A set of functions I wrote to solve the CryptoPals Crypto Challenges. Requires Python2.'''
'''Note: You're welcome to use this code for your own purposes, but if you want to learn about cryptography, I would recommend working through the CryptoPals problem set by yourself.'''

def pkcs7(s,nbytes):
    '''Implement PKCS#7 padding'''
    d = nbytes - len(s)
    return s + chr(d) * d



def hex2base64(s):
    '''Converts a series of hex digits into an ASCII string, and Base64-encodes the result'''
    if len(s) % 2 == 1:
        s = '0' + s
    return s.decode('hex').encode('base64')


def fixedXOR(s1, s2):
    '''Combines two strings by XOR-ing the byte values of each character'''
    return ''.join(chr(ord(a) ^ ord(b)) for (a,b) in zip(s1,s2))


def englishness(s, use_digraphs=True):
    '''Returns an integer score indicating how much the input string resembles English (higher is better). Checks letter frequencies, and also digraph frequencies (if use_digraphs=True)'''
    # Character frequencies in War & Peace
    efreq = { ' ':10470, 'e':6363, 't':4460, 'a':4053, 'o':3883, 'n':3671, 'i':3379, 'h':3322,
              's':3254, 'r':2949, 'd':2366, 'l':1949, '\n':1325, 'u':1322, 'c':1205, 'm':1186,
              'w':1146, 'f':1075, 'g':1016, 'y':913, ',':812, 'p':790, 'b':629, '.':626,
              'v':528, 'k':390, '"':366, '-':165, '\'':153, 'I':149, 'T':129, 'A':125, 'P':123,
              'H':81, '!':80, 'x':75, 'B':72, 'N':72, 'M':66, '?':64, 'S':59, 'W':58, 'R':53,
              'q':46, 'z':46, 'j':44, 'D':40, 'F':38, 'E':35, 'C':34, 'O':31, 'Y':25, 'G':24,
              'K':24, ';':23, ':':19, 'V':18, ')':13, '(':13, 'L':13, 'X':7, '1':6, 'J':6,
              '*':5, 'U':4, '8':3, '0':2, '2':2, 'Z':2 }
    digraphs = { 'e ':1855, ' t':1553, 'he':1487, 'th':1401, 'd ':1286, ' a':1208, 't ':977,
                 'in':972, 's ':969, ' h':881, 'er':881, 'an':870, 're':722, ' w':711, ' s':708,
                 'nd':703, ', ':700, 'n ':660, ' o':620, 'ed':582, 'at':565, 'on':547, 'ha':544,
                 'en':536, 'hi':518, 'ng':509, 'to':496, 'o ':479, 'y ':476, 'ou':476, 'r ':472,
                 ' i':455, 'is':441, 'as':420, 'it':415, ' b':405, 'es':398, 'or':397, 'te':368,
                 ' f':363, 'g ':361, 'ar':360, 'st':356, ' c':352, 'se':351, 'f ':345, 'le':344,
                 'of':341, 'nt':324, 'me':306, ' m':305, '. ':303, 'ne':298, 've':293, ' d':282,
                 'ti':279, 'al':275, 'ro':274, '\n\n':273, 'ho':271, 'ri':270, 'ea':270,
                 'll':268, 'de':267, 'ce':266, 'h ':248, 'wa':246, 'a ':244, 'no':242, 'co':242,
                 ' r':238, ' p':238, ' l':236, 'ad':230, 'om':225, 'ut':221, ' n':219, 'ch':218,
                 'be':217, 'el':210, 'wh':208, 'sh':203, 'ly':203, 'ow':202, 'ot':202, 'im':200,
                 'l ':198, 'wi':197, 'ss':196, '.\n':190, ' e':189, 'li':189, 'si':187, 'nc':185,
                 'us':181, 'ta':178, 'ai':178, 'id':175, 'un':174, 'ic':172, 'ie':172, 'm ':170,
                 'sa':170, 'ra':167, 'il':166, 'so':166, 'lo':166, 'rs':164, 'ur':163, 'ee':163,
                 'ma':159, ' g':159, 'fo':158, 'pe':158, 'et':156, 'ol':156, 'di':155, 'e\n':155,
                 'la':153, 'io':149, 'oo':145, 'we':143, 'ac':142, 'ld':141, 'ov':140, 'os':137,
                 'ca':132, 'em':130, 'ul':127, 'w ':124, 'e,':124, 'ns':124, 's,':123, 'gh':121,
                 'ir':120, '\n"':118, '" ':118, 'mo':117, 'ry':116, 'ke':115, 'ge':112, 'tr':112,
                 'ni':111, 'pr':110, 'ay':110, 'ec':107, 'ev':107, 'yo':105, ' y':104, 'rr':100,
                 '\nt':100, ' u':100, 'Th':99, ' I':99, 'd\n':98, 'mi':95, 'rt':93, 'po':93,
                 'am':93, 'fe':92, 'fi':92, 'do':92, ' P':92, 'av':91, 'wo':90, 'vi':90, 'tt':89,
                 'pa':89, '\'s':89, 'rd':88, 'e.':88, 'fr':87, 'ig':87, '--':86, 'd,':85,
                 'ht':85, '\na':83, 'pl':83, 'bu':83, '..':81, 'ct':81, 's\n':80, ' A':79,
                 'I ':78, 'ap':78, 'su':77, 'ts':77, 'fa':76, 'ey':76, 'k ':74, 'bl':73, 'na':73,
                 ' T':72, 'tu':70, 'dr':70, 'ei':70, 't\n':69, 'mp':69, 'if':69, 's.':69,
                 'ep':69, 'ab':69, 'ag':69, 'ga':68, 'ok':68, 'ki':67, 'iv':66, 'ug':66, 't,':65,
                 ' "':64, 'ef':64, 'ew':64, 'ty':63, 'y,':63, '"\n':63, 'sp':63, 'ex':63,
                 'bo':62, 'od':62, 'n,':61, '\ns':61, 'tl':61, 'op':61, 'An':60, 'u ':59,
                 '\nh':59, 'rm':58, 'ia':58, ' v':58, 'r,':57, 'ff':57, 'd.':57, ',\n':57,
                 'up':56, 'ba':55, ' k':54, 'pp':53, '\nw':53, ' M':53, ',"':53, 'ck':53,
                 'gr':52, 'rn':52, 'go':52, ' B':52, 'ak':52, ' H':51, ' N':51, 'ci':51, 't.':50,
                 'by':50, 'gi':50, 'n\n':49, 'my':47, 'lf':47, 'Pr':47, 'da':46, 'He':46,
                 '."':46, 'qu':46, 'ru':45, 'ds':45, 'wn':45, 'pi':45, 'p ':45, 'oi':45, 'au':45,
                 'y.':44, 'sk':44, 'ft':43, ' S':43, 'sc':43, 'eg':43, 'aw':43, 'ye':42, 'r.':42,
                 'nl':42, 'kn':41, 'uc':41, 'ny':41, 'cr':41, '!"':41, 'n.':40, 'Pi':40,
                 'r\n':39, 'nn':39, 'cl':39, 'ms':38, '\no':38, 'br':38, 'ue':38, ' R':38,
                 'Na':38, 'fu':37, 'y\n':37, '\nc':37, 'ui':35, 'n\'':35, 'o\n':35, '?"':34,
                 'Wh':34, 'cu':34, 'm.':33, 'lt':33, 'mu':32, '\nT':32, '\ni':32, '\nb':32,
                 'sm':32, 'eo':32, 'Ma':31, '! ':31, 'ls':31, 'va':31, 'hu':31, 'nk':30,
                 '\nf':30, ' F':30, 'lu':30, 'v ':30, 'rc':29, 'gl':29, 'm,':29, 'pt':29,
                 'g,':29, 'g\n':29, 'vo':29, 'af':29, 'mm':28, 'ud':28, ' D':28, 'l,':28,
                 'oa':28, 'um':27, 'Fr':27, 'xp':27, 'f\n':26, 'ya':26, 'ys':26, 'rg':26,
                 '\nd':26, 'dd':26, 'ik':26, 'ib':26, '"I':26, 'ua':26, '\np':26, 'oc':26,
                 'hr':26, 'rl':25, 'dl':25, ' j':25, ' q':25, ' W':25, 'h,':25, 'fl':24,
                 '\nm':24, 'dy':24, '"W':24, '\'t':24, '? ':24, 'sl':24, '\nA':23, '\nr':23,
                 'pu':23, 'gu':23, 'Ro':23, 'Bu':23, 'tw':22, 'mb':22, 'yi':22, ' E':22,
                 '\ne':21, 'ps':21, 'g.':21, '; ':21, 'lk':21, 'cc':21, '\nP':20, ' C':20,
                 'e\'':20, 'Bo':20, 't\'':19, 'du':19, 'w,':19, 'nu':19, ' K':19, '  ':19,
                 'Mo':19, 'ju':19, 'It':19, 'h\n':19, 'a,':19, 'a\n':19, '\nl':18, 'bi':18,
                 'ub':18, 'nf':18, 'gn':18, ' G':18, 'hy':18, 'gs':17, 'Sh':17, 'So':17, 'Co':17,
                 'o,':17, 'ob':17, 'yt':16, 'rk':16, 'kh':16, 'ip':16, ' O':16, 'Ru':16,
                 'l\n':16, '"T':15, 'nv':15, 'Yo':15, 'og':15, 'No':15, ': ':14, 'rv':14,
                 'Em':14, 'ks':14, '\nn':14, 'ws':14, '"A':14, '"Y':14, 'ze':14, 'Do':14,
                 'We':14, 'oy':14, 'Ni':14, '\ng':13, 'On':13, 'Al':13, ' V':13, 'sw':13,
                 'eh':13, 'e!':13, 'Ku':13, 'Pe':13, 'jo':13, 'Be':13, 'tc':12, 'm\n':12,
                 'r\'':12, '\nH':12, '\nB':12, 'iz':12, 'uz':12, 'zo':12, 'l.':12, 'e-':12,
                 'xc':12, 'De':12, 'Go':11, 'rp':11, 'k,':11, '\nN':11, '\nI':11, ' (':11,
                 'e?':11, 'v,':11, 'In':11, 'h.':11, 'f,':10, '\nS':10, '\nC':10, 'ko':10,
                 'w.':10, 'wr':10, 'Hi':10, 's!':10, '\' ':10, 'vn':10, 'oe':10, 'a.':10, '-t':9,
                 'gg':9, 'rf':9, '\nu':9, '"H':9, 'i ':9, 'bs':9, ' Y':9, 'Ye':9, 'lw':9, 'lr':9,
                 'xt':9, 'Ba':9, '-a':8, 'f.':8, 't?':8, '\nW':8, 'dg':8, 'w\n':8, '"N':8,
                 'Ho':8, ' L':8, 's\'':8, 'sb':8, 'lv':8, 'sn':8, 'je':8, 'c ':8, 'I\n':8,
                 'A ':8, 't!':7, 'v\'':7, 'ER':7, 'k.':7, '\nM':7, 'ka':7, 'd-':7, 'wd':7,
                 ') ':7, 'ph':7, 'CH':7, 'p,':7, '"B':7, '"O':7, 'HA':7, 'To':7, 'TE':7, 'AP':7,
                 '\'l':7, 'Mi':7, 's-':7, 'sy':7, 'lm':7, 'lp':7, 'R ':7, 'PT':7, 'I\'':7,
                 'o.':7, 'hm':7, 'az':7, 'Ge':6, 'y-':6, 'y\'':6, 'r-':6, '\nR':6, '\nD':6,
                 'kl':6, 'd!':6, 'dv':6, 'py':6, 'Va':6, 'Oh':6, 'Ha':6, 'u,':6, 'uf':6, 'n-':6,
                 'At':6, 'sf':6, 'xa':6, 'xe':6, 'Pa':6, 'cy':6, 'a\'':6, '-w':5, '-s':5,
                 't-':5, ':\n':5, 'Se':5, 'vs':5, 'y!':5, 'rw':5, 'r?':5, 'r!':5, '\nO':5,
                 '\nF':5, '\ny':5, 'dn':5, 'p.':5, 'ix':5, '"S':5, 'bt':5, 'uk':5, 'n!':5,
                 'Au':5, ' *':5, 's?':5, 'ek':5, 'xi':5, 'Wi':5, 'v.':5, 'If':5, 'As':5, '-c':4,
                 '-h':4, 'tm':4, 'St':4, 'mn':4, 'y?':4, 'yl':4, 'rb':4, 'Ev':4, 'k\n':4,
                 '\nk':4, 'Ju':4, 'dj':4, 'wl':4, '"D':4, '"M':4, '\n ':4, 'bb':4, 'u\'':4,
                 '\nv':4, 'nq':4, 'Af':4, 'n?':4, ' J':4, ' X':4, ' \'':4, 'zi':4, 'Fo':4,
                 'eb':4, 'eu':4, 'eq':4, '* ':4, 'vl':4, 'II':4, 'h!':4, 'gt':3, '-d':3, '-f':3,
                 '-b':3, '-l':3, '-i':3, 'tn':3, 'tf':3, 'ml':3, 'Le':3, 'Lo':3, 'f-':3, 'fs':3,
                 'ym':3, 'yc':3, 'yb':3, 'rh':3, 'x ':3, '\nK':3, '\nE':3, 'd\'':3, 'd?':3,
                 'd:':3, 'dm':3, '),':3, 'p\n':3, 'Ch':3, 'Ca':3, '"t':3, '"G':3, '"C':3, '"L':3,
                 'i,':3, 'Ve':3, 'Vi':3, 'bj':3, 'u\n':3, 'u.':3, 'uo':3, 'Ti':3, ' 1':3, 's;':3,
                 'sq':3, 'l-':3, 'ez':3, 'e;':3, 'Ka':3, '18':3, 'Du':3, 'Po':3, 'Ne':3, '!.':3,
                 'hs':3, 'hl':3, 'Ah':3, 'ae':3, 'aj':3, 'Ar':3, '-e':2, '-o':2, '-n':2, 'Gu':2,
                 'Gr':2, 'tz':2, 'm!':2, 'm-':2, 'm?':2, 'Sp':2, 'Su':2, 'Si':2, 'Sm':2, 'mf':2,
                 'La':2, 'Li':2, 'g?':2, 'y:':2, 'yf':2, 't;':2, 'VI':2, 'XI':2, '\nj':2, 'ky':2,
                 'd;':2, 'w\'':2, 'pc':2, '"a':2, '"b':2, 'iu':2, '"F':2, '"P':2, 'i\'':2,
                 'Or':2, 'b ':2, 'u!':2, 'Tu':2, '\nq':2, 'Te':2, 'nh':2, 'nj':2, 'nm':2, 'nw':2,
                 '\'v':2, '\'r':2, '\'m':2, ' U':2, 'g!':2, 'g-':2, 'zh':2, 'za':2, 'zu':2,
                 'My':2, 'Fi':2, 's:':2, '?.':2, '?\n':2, 'Re':2, 'ln':2, 'l\'':2, 'l!':2,
                 'e:':2, 'Ki':2, 'Dm':2, 'Da':2, 'Dr':2, 'cq':2, 'Is':2, 'Il':2, 'Br':2, 'o-':2,
                 'o!':2, 'o?':2, 'Un':2, 'oz':2, 'ox':2, 'h?':2, '!\n':2, 'hn':2, 'ah':2, 'a!':2,
                 '-I':1, '-m':1, '-p':1, '-r':1, '-y':1, 'gy':1, 't:':1, '-"':1, 'Zh':1, 'V\n':1,
                 'm;':1, 'Sc':1, 'Sa':1, 'mt':1, 'mr':1, 'f!':1, 'z ':1, 'fy':1, 'y;':1, 'yp':1,
                 'yr':1, 'yu':1, 'yw':1, 'rz':1, 'En':1, 'Eh':1, 'r:':1, 'r;':1, 'Eu':1, 'Er':1,
                 'X\n':1, 'XX':1, 'XV':1, 'v\n':1, 'k!':1, 'k-':1, '\n(':1, 'k?':1, '\nV':1,
                 '\nL':1, '\nG':1, 'kw':1, 'dk':1, 'dh':1, 'df':1, 'w!':1, 'w-':1, 'w?':1,
                 'wk':1, 'pf':1, '"w':1, '"E':1, '"U':1, '"V':1, '"R':1, '"-':1, 'i.':1, 'Vo':1,
                 'Ol':1, 'Of':1, 'Ou':1, 'Ot':1, 'Hu':1, 'bm':1, '.)':1, 'u?':1, '.\'':1, 'uv':1,
                 'Tw':1, 'Ts':1, 'Ta':1, 'nb':1, 'nx':1, 'np':1, 'nr':1, '\'d':1, '\'c':1,
                 'Am':1, 'n:':1, 'n;':1, ' Z':1, 'g:':1, 'zm':1, 'Me':1, 'Mu':1, 'Fa':1, 'Fe':1,
                 ',\'':1, 's)':1, 's"':1, ';\n':1, 'sv':1, 'sd':1, 'Ra':1, 'lg':1, 'lb':1,
                 'lc':1, 'l?':1, 'ej':1, '80':1, 'e)':1, 'e"':1, 'xh':1, 'Ko':1, 'Kr':1, '12':1,
                 'Di':1, 'Wa':1, 'Wo':1, 'Pl':1, 'ja':1, 'cs':1, 'c\n':1, 'vr':1, 'vy':1, 'Iv':1,
                 '(w':1, '(t':1, '(h':1, '(a':1, 'Bi':1, 'By':1, '\'\n':1, 'o\'':1, 'oh':1,
                 '!\'':1, 'h-':1, 'hk':1, 'hb':1, 'hc':1, 'hf':1, 'hd':1, 'Ag':1, '81':1, 'a-':1,
                 'a?':1 }
    score = 0
    for ch in s:
        if ch in efreq:
            score += efreq[ch]
        else:
            score -= 10
            if (ch < ' ' and ch not in '\r\n\t') or ch > '~':
                score -= 200
    if use_digraphs:
        for (ch1,ch2) in zip(s[:-1], s[1:]):
            d = ch1 + ch2
            if d in digraphs:
                score += digraphs[d] * 20
            else:
                score -= 100
    return score


def singleByteXORcrack(s, use_digraphs=True):
    '''Calculates the most likely plaintext for a ciphertext where every character has been XOR-ed with the same value'''
    results = []
    for x in range(256):
        p = ''.join(chr(ord(c)^x) for c in s)
        results.append((p, englishness(p, use_digraphs)))
    results.sort(key=lambda q: -q[1])
    return results[0][0]


def repeatingKeyXOR(s, key):
    '''Encrypts a character string by XOR-ing with a repeating key'''
    r = ''
    p = 0
    for ch in s:
        r += chr(ord(ch) ^ ord(key[p % len(key)]))
        p += 1
    return r


def hammingDistance(str1,str2):
    '''Compute the Hamming distance (number of non-equal bits) between two strings'''
    def nsetbits(x):
        r = 0
        while x:
            r += x & 1
            x >>= 1
        return r
    dist = 0
    for pair in zip(str1,str2):
        dist += nsetbits(ord(pair[0]) ^ ord(pair[1]))
    if len(str2) > len(str1):
        dist += hammingDistance(str2[len(str1):], '\0' * (len(str2)-len(str1)))
    elif len(str1) > len(str2):
        dist += hammingDistance(str1[len(str2):], '\0' * (len(str1)-len(str2)))
    return dist


def getKeySizeCandidates(ct, minSize=2, maxSize=40):
    '''Generate a sorted list of candidate key lengths for a repeating-key XOR cipher. Returns an array of (keylen,d) tuples, where d is the normalized Hamming distance between chunks separated by keylen characters'''
    candidates = []
    maxSize = min(maxSize, len(ct)/2)
    for keylen in range(minSize,maxSize+1):
        n = d = 0
        for keystart in range(0, len(ct), keylen*2):
            str1 = ct[keystart:keystart+keylen]
            str2 = ct[keystart+keylen:keystart+keylen*2]
            d += hammingDistance(str1, str2)
            n += 1
        d /= 1.0 * (n * keylen)
        candidates.append((keylen,d))
    candidates.sort(key=lambda q: q[1])
    return candidates


def sanitize(s):
    '''Converts all non-ASCII characters (including line breaks, etc.) in a string into dots'''
    return ''.join(ch if ' '<=ch<'~' else '.' for ch in s)


def vigenereCrack(ct, minSize=2, maxSize=40, keysize=0):
    '''Cracks an XOR repeating-key Vigenère cipher. If the key size is known, pass this in the keysize parameter. Otherwise specify a range using the minSize and maxSize parameters.'''
    if keysize == 0:
        ks = getKeySizeCandidates(ct, minSize, maxSize)[0][0]
    else:
        ks = keysize
    ctslices = [ct[i::ks] for i in range(ks)]
    ptslices = [singleByteXORcrack(s,False) for s in ctslices]
    pt = ''
    for i in range(len(ptslices[0])):
        for j in range(ks):
            if len(ptslices[j]) > i:
                pt += ptslices[j][i]
    return pt


def aes_ecb_decrypt(ct, key):
    '''AES ECB decryption. The parameters ct and key muct both be 16 bytes exactly'''
    from Crypto.Cipher import AES
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(ct)
    return pt
