print("나 이제 말해주고싶어")

def fact(n : int) -> int:
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans
# print(fact(5))
