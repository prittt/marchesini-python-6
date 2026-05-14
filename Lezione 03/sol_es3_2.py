def translate0(s: str, from_lst: str, to_lst: str) -> str:
    n = len(from_lst)
    if len(to_lst) != n:
        return s
    i = 0
    while i < n:
        s = s.replace(from_lst[i], to_lst[i])
        i = i + 1
    return s

def translate1(s: str, from_lst: str, to_lst: str) -> str:
    n = len(from_lst)
    if len(to_lst) != n:
        return s
    ris = ''
    for c in s:
        i = 0
        while i < n:
            if c == from_lst[i]:
                break
            i = i + 1
        if i < n:
            ris += to_lst[i]
        else:
            ris += c
    return ris            

def translate2(s: str, from_lst: str, to_lst: str) -> str:
    n = len(from_lst)
    if len(to_lst) != n:
        return s
    ris = ''
    for c in s:
        i = 0
        while i < n:
            if c == from_lst[i]:
                ris += to_lst[i]    
                break
            i = i + 1
        else:
            ris += c
    return ris            

def translate3(s: str, from_lst: str, to_lst: str) -> str:
    n = len(from_lst)
    if len(to_lst) != n:
        return s
    ris = ''
    for c in s:
        for i in range(n):
            if c == from_lst[i]:
                ris += to_lst[i]    
                break
        else:
            ris += c
    return ris            

def translate4(s: str, from_lst: str, to_lst: str) -> str:
    n = len(from_lst)
    if len(to_lst) != n:
        return s
    ris = ''
    for c in s:
        i = from_lst.find(c)
        if i >= 0:
            ris += to_lst[i]
        else:
            ris += c
    return ris            

def translate5(s: str, from_lst: str, to_lst: str) -> str:
    if len(to_lst) != len(from_lst):
        return s
    tbl = str.maketrans(from_lst, to_lst)
    return s.translate(tbl)

translate = translate0
print(translate("ciao", "abcd", "wxzy")) # "yiwo"
print(translate("abcdefghi", "abcdefghi", "ihgfedcba")) # "ihgfedcba"