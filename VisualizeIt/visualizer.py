import time
import os
import sys
from colorama import init, Fore, Style, deinit, Cursor
init()

UP = Cursor.UP()
DOWN = Cursor.DOWN()
RIGHT = Cursor.FORWARD()
LEFT = Cursor.BACK()
POS = Cursor.POS()


def clrscr():
    if sys.platform != "linux":
        os.system("cls")
    else:
        os.system("clear")


class Visualizer:
    def __init__(self, algoimpl) -> None:
        winwidth = os.get_terminal_size()[0]
        self.algo = algoimpl
        self.initdata = self.algo.data['algorithm']
        self.type = self.initdata['type']
        self.name = self.initdata['name']
        self.mainlabel = f'''{Fore.CYAN + Style.BRIGHT}{
        "VisualizeIt - Algorithms Visualized".center(winwidth)}
{Style.RESET_ALL}Currently performing {Fore.RED + Style.BRIGHT +
self.type.title()+Style.RESET_ALL} using
{Style.BRIGHT+Fore.GREEN+self.name.title()+Style.RESET_ALL} on
[ {Style.BRIGHT+" ".join(map(str, self.algo.arr))+Style.RESET_ALL} ] \n
'''


class SearchVisualizer(Visualizer):
    def __init__(self, algoimpl) -> None:
        super().__init__(algoimpl)
        self.speeds = {
            'slow': 4,
            'mid': 2,
            'fast': 1
        }
        self.data = self.algo.data

    def run(self, element, speed='mid'):
        clrscr()
        runner = self.algo.step_search(element)
        self.data = runner.__next__()

        # print(self.locallabel)
        found = False
        while not found:
            if self.data['found'] is True or self.data['notfound'] is True:
                found = True

            winwidth = os.get_terminal_size()[0]
            clrscr()
            start = self.data['process_data']['start']
            mid = self.data['process_data']['mid']
            end = self.data['process_data']['end']
            label = f'''{Style.BRIGHT}{
                    Fore.GREEN if self.data["searching"]
                    else Fore.RED}\tSearching{Style.RESET_ALL} for {
                    Style.BRIGHT+str(element)} in {self.algo.arr}

{Fore.RED + Style.BRIGHT + ('Start : '+ str(start)).ljust(10)
}{Fore.GREEN + Style.BRIGHT + ("Mid : "+ str(mid)).center(winwidth-18)
}{Fore.CYAN + Style.BRIGHT + ("End : " + str(end)).rjust(8) + Style.RESET_ALL}

{("["+" ".join([(Style.DIM + str(val)) if idx < start
    else (Fore.RED + Style.BRIGHT + str(val) + Style.RESET_ALL) if start==idx
    else (Fore.GREEN + Style.BRIGHT + str(val) + Style.RESET_ALL) if idx == mid
    else (Fore.CYAN + Style.BRIGHT + str(val) + Style.RESET_ALL) if idx == end
    else (Style.BRIGHT + str(val) + Style.RESET_ALL)
    for idx,val in enumerate(self.algo.arr)])+"]").ljust(winwidth//2 -1)}

{self.data['msg'].center(winwidth)}
'''
            print(POS + self.mainlabel + label)
            time.sleep(1*self.speeds[speed])
            try:
                self.data = runner.__next__()
            except StopIteration:
                pass
        deinit()


class SortVisualizer(Visualizer):
    def __init__(self):
        super()
