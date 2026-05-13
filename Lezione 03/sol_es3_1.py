def farfallino_encode1(s: str) -> str:
    ris = ''
    i = 0    
    while i < len(s):
        if s[i] == 'a':
            ris += 'afa'
        elif s[i] == 'e':
            ris += 'efe'
        elif s[i] == 'i':
            ris += 'ifi'
        elif s[i] == 'o':
            ris += 'ofo'
        elif s[i] == 'u':
            ris += 'ufu'
        else: 
            ris += s[i]
        i = i + 1
    return ris

def farfallino_encode2(s: str) -> str:
    ris = ''
    for c in s:
        if c == 'a':
            ris += 'afa'
        elif c == 'e':
            ris += 'efe'
        elif c == 'i':
            ris += 'ifi'
        elif c == 'o':
            ris += 'ofo'
        elif c == 'u':
            ris += 'ufu'
        else: 
            ris += c
    return ris

def farfallino_encode3(s: str) -> str:
    ris = ''
    for c in s:
        if c in 'aeiou':
            ris += c + 'f' + c
        else: 
            ris += c
    return ris

def farfallino_encode4(s: str) -> str:
    ris = ''
    for c in s:
        ris += c
        if c in 'aeiou':
            ris += 'f' + c
    return ris

def farfallino_encode5(s: str) -> str:
    s = s.replace('a', 'afa')
    s = s.replace('e', 'efe')
    s = s.replace('i', 'ifi')
    s = s.replace('o', 'ofo')
    s = s.replace('u', 'ufu')
    return s

def farfallino_encode6(s: str) -> str:
    return (s.replace('a', 'afa').replace('e', 'efe').replace('i', 'ifi')
             .replace('o', 'ofo').replace('u', 'ufu'))

def farfallino_encode(s: str) -> str:
    ris = ''
    i = 0
    while i < len(s):
        ris = ris + s[i]
        i = i + 1
    return ris

print(farfallino_encode('ciao'))
print(farfallino_encode('aiuola'))
print(farfallino_encode('Costantino'))
