from colorama import init, Fore, Back, Style

init()


class Visualizer:
    def __init__(self, algoimpl) -> None:
        self.algo = algoimpl
        self.initdata = self.algo.data['algorithm']
        self.type = self.initdata['type']
        self.name = self.initdata['name']
        self.label = f'''{Fore.CYAN + Style.BRIGHT}VisualizeIt - Algorithms Visualized 
{Style.RESET_ALL}Currently performing {self.type.title()} using
{self.name.title()} on
[ {" ".join(map(str, self.algo.arr))} ]
'''

    def run(self):
        print(self.label)
