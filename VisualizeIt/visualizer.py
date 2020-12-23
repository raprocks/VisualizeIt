import time
import os
import sys
from typing import Union
from colorama import init, Fore, Style, deinit, Cursor
from VisualizeIt_implementations.BinarySearch import BinarySearch
from VisualizeIt_implementations.BubbleSort import BubbleSort
init()

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
        self.array = self.algo.data['array']
        self.name = self.initdata['name']
        self.mainlabel = f'''{Fore.CYAN + Style.BRIGHT}{
        "VisualizeIt - Algorithms Visualized".center(winwidth)}
{Style.RESET_ALL}Currently performing {Fore.RED + Style.BRIGHT +
self.type + Style.RESET_ALL} using
{Style.BRIGHT + Fore.GREEN + self.name + Style.RESET_ALL} on
[ {Style.BRIGHT + " ".join(map(str, self.array)) + Style.RESET_ALL} ] \n
'''


class SearchVisualizer(Visualizer):
    def __init__(self, algoimpl: BinarySearch) -> None:
        super().__init__(algoimpl)
        self.algo = algoimpl
        self.speeds = {
            'slow': 4,
            'mid': 2,
            'fast': 1
        }
        self.data = self.algo.data

    def run(self, element: int, speed='mid'):
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

{"Array : " + ("[" + " ".join([
    (Style.DIM + str(val) + Style.RESET_ALL) if idx < start
    else (Fore.RED + Style.BRIGHT + str(val) + Style.RESET_ALL) if idx==start
    else (Fore.GREEN + Style.BRIGHT + str(val) + Style.RESET_ALL) if idx == mid
    else (Fore.CYAN + Style.BRIGHT + str(val) + Style.RESET_ALL) if idx == end
    else (Style.BRIGHT + str(val) + Style.RESET_ALL)
    for idx,val in enumerate(self.algo.arr)])+"]" + Style.RESET_ALL)}

{Style.BRIGHT + Fore.LIGHTRED_EX
+ self.data['msg'].center(winwidth) + Style.RESET_ALL}
'''
            print(POS + self.mainlabel + label)
            time.sleep(1*self.speeds[speed])
            try:
                self.data = runner.__next__()
            except StopIteration:
                pass
        deinit()


class SortVisualizer(Visualizer):
    def __init__(self, algoimpl: BubbleSort) -> None:
        super().__init__(algoimpl)
        self.algo = algoimpl
        self.speeds = {
            'ultra': 0.3,
            'slow': 4,
            'mid': 2,
            'fast': 1
        }
        self.data = self.algo.data

    def run(self, speed='mid'):
        clrscr()
        runner = self.algo.sort()
        self.data = runner.__next__()
        sorted_arr = False
        arr_len = len(self.data['array'])
        while not sorted_arr:
            if self.data['sorted'] is True:
                sorted_arr = True

            winwidth = os.get_terminal_size()[0]
            clrscr()
            comparing_idx = self.data['comparing_data'].values()
            swapping_idx = self.data['swapping_data'].values()
            pass_number = self.data['pass']
            fixed = arr_len - 1-pass_number
            label = f'''{Style.BRIGHT}{
                    Fore.GREEN if self.data["comparing"]
                    else Fore.RED}\tComparing{Style.RESET_ALL}

{"Array : " + ("[" + " ".join([
    (Style.DIM + str(val) + Style.RESET_ALL) if (idx not in comparing_idx) and (idx not in swapping_idx)
    else (Fore.RED + Style.BRIGHT + str(val) + Style.RESET_ALL)
    if self.data['comparing'] and (idx in comparing_idx)
    else (Fore.GREEN + Style.BRIGHT + str(val) + Style.RESET_ALL)
    if self.data['swapping'] and (idx in swapping_idx)
    else (Style.BRIGHT + str(val) + Style.RESET_ALL)
    if idx>= fixed
    else (str(val) + Style.RESET_ALL)
    for idx,val in enumerate(self.data['arr'])])+"]" + Style.RESET_ALL)}

{Style.BRIGHT + Fore.LIGHTRED_EX
+ self.data['msg'].center(winwidth) + Style.RESET_ALL}
'''
            print(POS + self.mainlabel + label)
            time.sleep(1*self.speeds[speed])
            try:
                self.data = runner.__next__()
            except StopIteration:
                pass
        deinit()
