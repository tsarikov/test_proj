def pascal(n):
    line = [1]
    for k in range(n):
        line.append(int(line[k] * (n-k) / (k+1)))
    return line

print(pascal(10))