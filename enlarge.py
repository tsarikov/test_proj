def enlarge(mass):
    for line in mass:
        stroka = list(line)
        l = len(stroka)
        i = 0
        while i < l:
            stroka[i] = stroka[i]*2
            i += 1
        doubled_line = ''.join(stroka)
        print(doubled_line)
        print(doubled_line)



enlarge(['@@@','@ @','@@@'])