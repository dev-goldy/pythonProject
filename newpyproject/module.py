from filemkr import on
from sorting import sort

def Allinone():
    print("[1] make file")
    print("[2] sort list")
    srtlist = "here's your sorted list >"

    S = input("enter > ")
    if S == "1":
        on()
    elif S == "2":
        list = int(input("enter your numbers > "))
        num_list = [int(x) for x in str(list)]
        sort(num_list)
        show = input(" print list (y/n)> ")
        if show == "y":
            print(num_list)
        elif show == "n":
            pass


if __name__ == "__main__":
    Allinone()