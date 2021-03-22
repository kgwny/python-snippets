def generate_nums():
    for num in range(15):
        yield num 

nums = generate_nums()

for x in nums:
    print("first loop: %d" % x)

    if x > 9:
        break

for x in nums:
    print("second loop: %d" % x)

    if x > 19: 
        break
