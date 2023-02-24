import requests
from payloads import Payload
from getpass import getpass
from utils import *
import sys

page_login = 'https://susi.uni-sofia.bg/ISSU/forms/Login.aspx'
page_report = 'https://susi.uni-sofia.bg/ISSU/forms/students/ReportExams.aspx'

username = input('Username: ')
password = getpass('Password: ')

class CLA:
    show_full_report = '-a' #all
    show_semester = '-s'    #session
        
with requests.Session() as s:

    login_content = s.get(page_login).text
    s.post(page_login, Payload.login(username, password, *scrape_keys(login_content)))
    
    report_content = s.get(page_report).text
    response = s.post(page_report, Payload.report(*scrape_keys(report_content))).text
    
    full_report = CLA.show_full_report in sys.argv
    session = CLA.show_semester in sys.argv
    if session:
        session_num = int(sys.argv[sys.argv.index(CLA.show_semester) + 1])
    else:
        session_num = None
        
    print_report(response, show_all=full_report, session=session_num)
