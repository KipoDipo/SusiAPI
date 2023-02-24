from bs4 import BeautifulSoup
from session import Session
from colorama import Fore, Back, Style
from colorama import init as colorama_init

def scrape_keys(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    view_state = soup.find(id='__VSTATE')['value']
    event_validation = soup.find(id='__EVENTVALIDATION')['value']
    return [view_state, event_validation]

def print_report(report_html_text, show_all = False, session = None):
    colorama_init()
    semesters = []
    soup = BeautifulSoup(report_html_text, 'html.parser')
    td_tags = soup.find_all('td')

    semester = Session()
    for i, td in enumerate(td_tags):
        if td.text == 'Предмет' or i == len(td_tags) - 1:
            if semesters != []:
                semester.ECTS_All = semester.ECTS_Mandatory + semester.ECTS_Optional
                semester.Failed = len(semester.Failed_Subjects)
                semester.Passed = len(semester.Passed_Subjects)
                semester.Undecided = len(semester.Undecided_Subjects)
                if (semester.Passed + semester.Failed) != 0:
                    semester.Grade = semester.Grade / (semester.Passed + semester.Failed)
                semester = Session()
            
            if i != len(td_tags) - 1:
                semesters.append(semester)
                continue

        if td.text in ['Задължителни', 'Избираеми', 'Факултативни']:
            passed = td_tags[i + 1].text.strip()
            ects = float(td_tags[i + 3].text.replace(',', '.'))
            if len(td_tags[i + 2].text) > 2:
                grade = float(td_tags[i + 2].text)
                semester.Grade += grade
                subject = [f'{grade:.2f} - {td_tags[i - 2].text.strip()}']
            else:
                grade = None
                subject = [td_tags[i - 2].text.strip()]

            if passed == 'да':
                semester.Passed_Subjects += subject
                if td.text == 'Задължителни':
                    semester.ECTS_Mandatory += ects
                else:
                    semester.ECTS_Optional += ects
            elif grade is not None:
                semester.Failed_Subjects += subject
            else:
                semester.Undecided_Subjects += subject

    allECTS = 0
    allECTS_Mandatory = 0
    allECTS_Optional = 0
    last_semester = 0
    for i, sem in enumerate(semesters):
        if sem.Grade == 0 and not show_all:
            break
        if sem.Grade != 0:
            allECTS += sem.ECTS_All
            allECTS_Mandatory += sem.ECTS_Mandatory
            allECTS_Optional += sem.ECTS_Optional
        
            last_semester = i + 1
        if session is not None and i + 1 != session:
            continue
        print(f'{Fore.LIGHTYELLOW_EX}------------------------------------{Style.RESET_ALL}')
        print(f'{Back.LIGHTYELLOW_EX}{Fore.BLACK}Session {i + 1}:{Style.RESET_ALL}\n')
        sem.print()
    
    print(f'{Fore.LIGHTYELLOW_EX}------------------------------------{Style.RESET_ALL}\n')
    print(f'{Back.LIGHTYELLOW_EX}{Fore.BLACK}Overall:{Style.RESET_ALL}')
    print(f'{Fore.LIGHTYELLOW_EX}o===============================o{Style.RESET_ALL}')

    print(f'{Back.CYAN}{Fore.BLACK}Total ECTS           {Back.LIGHTCYAN_EX}{Fore.BLACK}{allECTS:>12}{Style.RESET_ALL}')
    print(f'{Back.CYAN}{Fore.BLACK}Total ECTS Mandatory {Back.LIGHTCYAN_EX}{Fore.BLACK}{allECTS_Mandatory:>12}{Style.RESET_ALL}')
    print(f'{Back.CYAN}{Fore.BLACK}Total ECTS Optional  {Back.LIGHTCYAN_EX}{Fore.BLACK}{allECTS_Optional:>12}{Style.RESET_ALL}')
    if last_semester - 1 > 1:
        avg = (semesters[last_semester - 1].Grade + semesters[last_semester - 2].Grade) / 2
    elif last_semester - 1 == 0:
        avg = semesters[0].Grade
    else:
        avg = -1

    print(f'{Back.MAGENTA}{Fore.WHITE}Scholarship grade    {Back.LIGHTMAGENTA_EX}{Fore.WHITE}{avg:>12.2f}{Style.RESET_ALL}')
    print(f'{Fore.LIGHTYELLOW_EX}o===============================o{Style.RESET_ALL}')
