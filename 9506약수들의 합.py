while True:
    result = []
    n = int(input())
    if n == -1:
        break
    for _ in range(1, n):
        if n % (_) == 0:
            result.append(_)
    if sum(result) == n:
        print(n, " = ", " + ".join(str(_) for _ in result), sep = "")
    else:
        print(f"{n} is NOT perfect.")
