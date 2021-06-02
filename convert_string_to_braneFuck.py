def convert(s):
    ascii_code = []
    return_code = []
    is_done = False
    for i in s:
        ascii_code.append(ord(i))
    for j in ascii_code:
        for g in range(2, 10):
            if j % g == 0:
                print(g, j / g)
                return_code.append("+" * g + "[>" + "+" * int(j/g) + "<-]>.>")
                is_done = True
                break
        if is_done:
            is_done = False
        else:
            return_code += "+" * j + ".>"
        print(j)

    return_code = "".join(return_code)
    return return_code


print(convert(input()))
