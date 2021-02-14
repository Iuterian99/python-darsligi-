def longest_name():
    take_input = input("Input names please! ")
    space = take_input.split(" ")
    long_name = max(space, key=len)
    print(long_name)

longest_name()

