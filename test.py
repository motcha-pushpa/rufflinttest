def make_three_adders(x):
    result = []
    for i in [10, 20, 30]:
        p = x + i
        result.append(p)
    return result

for adder in make_three_adders():
    print(adder(7))  # noqa