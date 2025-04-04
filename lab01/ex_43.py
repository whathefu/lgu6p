def print_all(*args, **kwargs) :
    print(args)
    print(kwargs)

#묶어서 위치에 맞게 코딩해야 출력 가능함.
print_all(1,2,3,4,5,6, x=100, y=300, z=400)