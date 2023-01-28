##############################################
#                                            #
#  git ->                                    #
#  made by ->  sirGOLDU                      #
#  on   january, 29, 2023                    #
#                                            #
##############################################

from threading import *  # importing thread i dont know why
from time import sleep  # for loading


def notsuper():
    cyan = "\033[0;36m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    print(cyan, "[1] open read new file ")
    print(green, "[2] open new file in write mode ")
    print(red, "[3] open file in notepad ")
    sleep(1)


class Superclasss(Thread):

    def supermethodd(self):
        # I forgot how can I use class variables so i do that
        # both methods have their own clr codes
        green = "\033[0;32m"

        x = input(" Enter file number please >> ")
        y = input(" Please enter new file name >> ")

        if x and y:
            print(green, " Loading...")
            sleep(1)
            print("***...................")
            sleep(1)
            print("****..................")
            sleep(1)
            print("*******...............")
            sleep(1)
            print("**********............")
            sleep(1)
            print("************..........")
            sleep(1)
            print("***************.......")
            sleep(1)
            print("********************..")
            sleep(1)
            print("**********************")

        try:
            i = int(input(" please enter any number kind sir > "))
        except ValueError as e:
            print(" please enter number kind sir/madam not strings >> ")
            print("real error is > ", e)
        print(" script ended  ")


obj = Superclasss()
notsuper()
obj.supermethodd()
