class Alarmclock:

    def __init__(self):
        self.time_now = ''
        self.alarm_time =''
        self.alarm_on = False
        

    def set_time(self):  
        current_time = input('Current time is 1000 do yo want to change it? Enter y/n:  ')  
      
        if current_time == 'y':
            self.time_now = input ('What time is it? ')
        else:
            self.time_now = 1000    

    def set_alarm_time(self):
        wakeup_time = input('What time do you want to wake up? ')
        self.alarm_time = wakeup_time   
          

    def alarm_set(self):
        if self.alarm_on == False:
         print('Alarm is off! ')
         response=input('Do you want to turm it on? Enter y/n: ')
         if response == 'y':
             self.alarm_om = True
             print ("Alarm is on!")
         else:
             self.alarm_on = False  