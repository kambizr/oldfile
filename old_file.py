# Version 0.1
# jsut shows files older than entry
#developed by Kambiz Rahmani
#!/usr/bin/env python3.6
# coding: utf-8
import time, os ,shutil
from datetime import datetime
from termcolor import colored

start=time.time()
today=datetime.now()

# print(bcolors.WARNING + "Warning: No active frommets remain. Continue?"+ bcolors.ENDC)
def main():
    while True:
        i=0
        j=0
        e=0
        stars="*"*40
        ans=int(input("""Please choose one of the following options:(just enter option number)
        1.By create datetime
        2.By modification datetime
        3. Exit
        >"""))
        old=int(input(colored("Enter days old you want to monitor: ",'cyan')))
        d=input(colored("Please enter your complete path: ",'cyan'))
        os.chdir(d)
        lst=os.listdir(d)


        for item in lst:
            try:
                if ans == 1:
                    utime=os.stat(item).st_ctime
                    mtime=datetime.fromtimestamp(utime)
                    age=today-mtime
                    #print(item," has ",age.days," days old")
                elif ans == 2:
                    utime=os.stat(item).st_mtime
                    mtime=datetime.fromtimestamp(utime)
                    age=today-mtime
                elif ans == 3:
                    exit(0)

                if int(age.days) > old :
                    fage="{} days old".format(age.days)
                    print(colored(item,'red'),colored('<----->','green'),colored(fage,'yellow',attrs=['underline']))
                    print('-'*47)
                    j=j+1
                i=i+1
            except:
                e +=1
            #end of for loop
        if j > 0:
            w="You have {}  out of  {} Items in this folder are older than {} days old, task complete with {} Errors in path:".format(j,i,old,e)
            print(colored(stars,'red'))
            print(colored(w,'yellow'))
            print(colored(os.getcwd(),'yellow',attrs=['underline']))

            #colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
            print(colored(stars,'red'))
            print("\n\n")
        else:
            print(colored(stars,'blue'))
            w2="You dont have any {} days old file in this path:".format(old)
            print(colored(w2,'green'))
            print(colored(os.getcwd(),'green',attrs=['underline']))
            print(colored(stars,'blue'))
            print("\n\n")


print("""File  manupilation program V 0.2
Developed by: Kambiz Rahmani 2018""")
main()
