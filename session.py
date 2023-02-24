from colorama import Fore, Style
from colorama import init as colorama_init

def beautiful_str(str_array):
    str = ""
    for i in str_array:
        str += f"\t{i},\n" if i != str_array[-1] else f"\t{i}\n"
    return str

class Session:

    def __init__(self) -> None:
        self.Passed = 0
        self.Failed = 0
        self.Undecided = 0
        self.Passed_Subjects = []
        self.Failed_Subjects = []
        self.Undecided_Subjects = []
        self.ECTS_All = 0
        self.ECTS_Mandatory = 0
        self.ECTS_Optional= 0
        self.Grade = 0

    def print(self) -> str:
        colorama_init()
        subject_count = len(self.Passed_Subjects) + len(self.Failed_Subjects) + len(self.Undecided_Subjects)
        if self.Passed != 0:
            print(f"Passed: {Fore.LIGHTGREEN_EX}{self.Passed}{Fore.WHITE}/{Fore.GREEN}{subject_count}{Style.RESET_ALL}")
        if self.Failed != 0:
            print(f"Failed: {Fore.LIGHTRED_EX}{self.Failed}{Fore.WHITE}/{Fore.RED}{subject_count}{Style.RESET_ALL}")
        if self.Undecided != 0:
            print(f"Undecided: {Fore.LIGHTYELLOW_EX}{self.Undecided}{Fore.WHITE}/{Fore.YELLOW}{subject_count}{Style.RESET_ALL}")
        if self.Passed_Subjects != []:
            print(f"Passed Subjects: {Fore.GREEN}[\n{beautiful_str(self.Passed_Subjects)}{Fore.GREEN}]{Style.RESET_ALL}")
        if self.Failed_Subjects != []:
            print(f"Failed Subjects: {Fore.RED}[\n{beautiful_str(self.Failed_Subjects)}{Fore.RED}]{Style.RESET_ALL}")
        if self.Undecided_Subjects != []:
            print(f"Undecided Subjects: {Fore.YELLOW}[\n{beautiful_str(self.Undecided_Subjects)}{Fore.YELLOW}]{Style.RESET_ALL}")
        if self.ECTS_All != 0:
            print(f"{Fore.CYAN}Total ECTS           {Fore.LIGHTCYAN_EX}{self.ECTS_All:>12}")
        if self.ECTS_Mandatory != 0:
            print(f"{Fore.CYAN}Total ECTS Mandatory {Fore.LIGHTCYAN_EX}{self.ECTS_Mandatory:>12}")
        if self.ECTS_Optional != 0:
            print(f"{Fore.CYAN}Total ECTS Optional  {Fore.LIGHTCYAN_EX}{self.ECTS_Optional:>12}")
        if self.Grade != 0:
            print(f"{Fore.MAGENTA}Grade                {Fore.LIGHTMAGENTA_EX}{self.Grade:>12.2f}")
            
        return str
