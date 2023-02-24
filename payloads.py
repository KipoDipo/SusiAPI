class Payload:

    def login(username, password, view_state, event_validation):
        return {
            '__EVENTTARGET' : '',
            '__EVENTARGUMENT' : '',
            '__VSTATE': view_state,
            '__VIEWSTATE' : '',
            '__EVENTVALIDATION': event_validation,
            'txtUserName' : username,
            'txtPassword' : password,
            'btnSubmit' : 'Влез',
        }
    
    def report(view_state, event_validation):
        return {
            '__EVENTTARGET' : f'Report_Exams1$btnReportExams',
            '__EVENTARGUMENT' : f'',
            '__VSTATE' : view_state,
            '__VIEWSTATE' : f'',
            '__EVENTVALIDATION' : event_validation,
            'Report_Exams1:chkTaken' : 'on',
            'Report_Exams1:chkNotTaken' : 'on'
        }