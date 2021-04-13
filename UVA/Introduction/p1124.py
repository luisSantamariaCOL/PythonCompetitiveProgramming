def Main():
    while True:
        try:
            mssg =  str(input())
        except EOFError:
            break
        print(mssg)
Main()
