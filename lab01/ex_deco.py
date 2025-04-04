
def outer_fuc(msg):
    def inner_func():
        print(f"메시지: {msg}")
    return inner_func

closure = outer_fuc("안녕하세요")
closure()