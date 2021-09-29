candles = [3, 2, 1, 3]

tallest = max(candles)
i = 0
n = len(candles)

print(tallest)
print(n)
print()

# while tallest in candles:
#     candles.remove(tallest)
#     i += 1

for num in range(n):
    print(i,candles[num],tallest)
    if candles[num] == tallest:
        i += 1
    print(i)

print()
print(i)

# return len(candles)