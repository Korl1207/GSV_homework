s = [81, 120]
for i in range(s[0], s[1] + 1):
    print(f"{i}) ", end="")
    exec(open(f"{i}.py").read())
