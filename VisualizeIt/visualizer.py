import os
from colorama import init, Fore, Back, Style, deinit
winwidth = os.get_terminal_size()[0]


class Visualizer:
    def __init__(self, algoimpl) -> None:
        self.algo = algoimpl
        self.initdata = self.algo.data['algorithm']
        self.type = self.initdata['type']
        self.name = self.initdata['name']
        self.mainlabel = f'''{Fore.CYAN + Style.BRIGHT}{"VisualizeIt - Algorithms Visualized".center(winwidth)}
{Style.RESET_ALL}Currently performing {Fore.RED + Style.BRIGHT + self.type.title()+Style.RESET_ALL} using
{Style.BRIGHT+Fore.GREEN+self.name.title()+Style.RESET_ALL} on
[ {Style.BRIGHT+" ".join(map(str, self.algo.arr))+Style.RESET_ALL} ]
'''


class SearchVisualizer(Visualizer):
    def __init__(self):
        super()


class SortVisualizer(Visualizer):
    def __init__(self):
        super()
