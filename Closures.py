def make_counter(start=0):
    count = start
    def increment(step=1):
        nonlocal count
        count += step
        return count
    return increment

counter_a = make_counter()
counter_b = make_counter(100)

print(counter_a(), counter_a(), counter_a())
print(counter_b(5), counter_b(5))

