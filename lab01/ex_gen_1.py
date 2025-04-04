
# def get_number_generator(n):
#     for i in range(n):
#         print("before yield")
#         yield i
#         print("after yield")

# number = get_number_generator(3)
# next(number, 'end')
# print()

# next(number,'end')
# print()

# next(number, 'end')
# print()


def inf_number_gen():
    i = 1
    while True :
        yield i
        i += 1

g = inf_number_gen()
print(next(g))
print(next(g))
