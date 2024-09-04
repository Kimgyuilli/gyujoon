lit = input()

stack = []
DepthStack = [0] * 50
depth = 0

for _ in lit:
    if _ != ")":
        if _ == "(":
            depth += 1
            DepthStack[depth] = 0
        stack += [_]
    else:
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == "(":
                num = DepthStack[depth]
                for j in stack[i + 1 :]:
                    num += 1
                depth -= 1
                DepthStack[depth] += num * int(stack[i - 1])
                del stack[i - 1 :]
                break
print(DepthStack[0] + len(stack))