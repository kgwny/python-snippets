import time

start = time.perf_counter()
for x in range(1000):
    pass
end = time.perf_counter()
total = end - start
print(total)
