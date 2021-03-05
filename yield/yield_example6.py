def func3():
    print("He said:")
    yield "How are you?"

    print("She replied and asked:")
    yield "I'm fine. How are you?"

    print("He replied:")
    yield "I'm fine too."

generator = func3()
print(next(generator))
print(next(generator))
print(next(generator))

# He said:
# How are you?
# She replied and asked:
# I'm fine. How are you?
# He replied:
# I'm fine too.
