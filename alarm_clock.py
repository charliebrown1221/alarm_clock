class Alarm_clock:

    def __init__(self):
        self.time_now = ''
        self.alarm_time =''
        self.alarm_on = True
        

def set_time(self):  
    current_time = input('Current time is 1000 do yo want to change it? Enter y/n:  ')  
    self.time_now= current_time
    if current_time == 'y':
        current_time = input ('What time is it? ')
    else:
        current_time = 1000    

def set_alarm_time(self):
    wakeup_time = input('What time do you want to wake up? ')
    self.alarm_time = wakeup_time   
    if alarm_set == False:
        print('Alarm is off! ')
        response=input('Do you want to turm it on? Enter y/n: ')
    if response == 'y':
        self.alarm_om = True
    else:
        self.alarm_on = False    




def alarm_set(self):
    if self.alarm_on == True:
        print('Alarm is already on! ') 
    else :
        self.alarm_on == False            