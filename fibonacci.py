from sys import argv


def fib(n):
    if n > 2:
        return fib(n - 2) + fib(n - 1)
    elif n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        raise ValueError("n should be in range [0: +inf]")


if __name__ == "__main__":
    user_input = argv[1]
    if int(user_input):
    	print(fib(int(user_input)))
    else:
        print("fibonacci <n> - calculates the member of sequence on n position")
        
