import time
import os
import sys
from colorama import init, Fore, Back, Style, deinit, Cursor
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
        self.mainlabel = f'''{Fore.CYAN + Style.BRIGHT}{"VisualizeIt - Algorithms Visualized".center(winwidth)}
{Style.RESET_ALL}Currently performing {Fore.RED + Style.BRIGHT + self.type.title()+Style.RESET_ALL} using
{Style.BRIGHT+Fore.GREEN+self.name.title()+Style.RESET_ALL} on
[ {Style.BRIGHT+" ".join(map(str, self.algo.arr))+Style.RESET_ALL} ] \n
'''


class SearchVisualizer(Visualizer):
    def __init__(self, algoimpl) -> None:
        super().__init__(algoimpl)
        self.data = self.algo.data

    def run(self, element):
        clrscr()
        runner = self.algo.step_search(element)
        self.data = runner.__next__()

        # print(self.locallabel)
        found = False
        while not found:
            if self.data['found'] is True:
                found = True

            winwidth = os.get_terminal_size()[0]
            clrscr()
            label = f'''{Style.BRIGHT}{Fore.GREEN if self.data["searching"] else Fore.RED}\tSearching{Style.RESET_ALL} {element} in {self.algo.arr}

{Fore.RED + Style.BRIGHT + ('Start : '+ str(self.data['process_data']['start'])).ljust(10)}{Fore.GREEN + Style.BRIGHT + ("Mid : "+ str(self.data['process_data']['mid'])).center(winwidth-18)}{Fore.CYAN + Style.BRIGHT + ("End : " + str(self.data['process_data']['end'])).rjust(8) + Style.RESET_ALL}

{("["+" ".join([str(i) for i in self.algo.arr])+"]").center(winwidth)}

{self.data['msg'].center(winwidth)}
'''
            print(POS + self.mainlabel + label)
            time.sleep(1)
            try:
                self.data = runner.__next__()
            except StopIteration:
                pass
        deinit()


class SortVisualizer(Visualizer):
    def __init__(self):
        super()
