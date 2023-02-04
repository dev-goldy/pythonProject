def on():
    try:
        file = input("[2] enter file name > ")
        open(file, 'w')
    except Exception:
        print("< done >")

    again = input("[+] start again (y/n)> ")
    if again == "y":
        pass
    else:
        print(" bye ")
