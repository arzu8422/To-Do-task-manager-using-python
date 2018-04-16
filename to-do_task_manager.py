import time,os
from time import localtime, strftime

class to_do_task_manager:
    completed_task=[]
    def __init__(self):
        self.app_menu()

    def app_menu(self):
        user_response1=input("""Welcome to To-Do task manager!!!
1. Enter 1 to register
2. Enter 2 to login
3. Enter anything else to exit \n""")

        if user_response1=='1' :
            self.register()
        elif user_response1=='2' :
            self.login()
        else :
            self.goodbye()

    def user_menu(self, log_in_file):
        # if self.is_logged_in=='1' :
            print("Select what do you want to do: ")
            user_response2 = input("""1. Enter 1 to add new task
2. Enter 2 to delete any task
3. Enter 3 to view all remaining tasks
4. Enter 4 to view all completed tasks
5. Enter 5 for account settings
6. Enter 6 to logout\n """)

            if user_response2 == '1':
                self.add_task(log_in_file)
            elif user_response2 == '2':
                self.delete_task(log_in_file)
            elif user_response2 == '3':
                self.view_task(log_in_file)
            elif user_response2 == '4':
                self.completed_task(log_in_file)
            elif user_response2 == '5':
                self.settings(log_in_file)
            elif user_response2=='6':
                self.logout()
            else :
                print("Invalid input")
                self.user_menu(log_in_file)
        # else :
            # print("Please login or register")
            # self.app_menu()

    def register(self):
        print("Enter the following credentials:")
        user=input("Enter your username: ")
        email=input("Enter your email: ")
        if os.path.isfile(email+'.save')==0 :
            password=input("Enter your password: ")
            filename=email+".save"
            savedata=open(filename,"w")
            savedata.write(user+"`"+email+"`"+password+"`")
            savedata.close()
            print("Saving data....")
            time.sleep(1)
            print("Registration Successfull!!!")
            time.sleep(1)
            print("Welcome "+user+" Select what do you want to do : ")
            #self.is_logged_in=1
            self.user_menu(filename)
        else :
            print("That email is already registered....please choose another email")
            time.sleep(1)
            self.app_menu()

    def login(self):
        print("Enter the following credentials to login :")
        email_for_login=input("Email: ")
        password_for_login=input("Password: ")
        log_in_file=email_for_login+".save"
        try :
            try_login_file=open(log_in_file,"r")
            credentials=[]
            for line in try_login_file :
                parts=line.split('`')
                credentials.append(parts)
            try_login_file.close()
            if (credentials[0][1] == email_for_login and credentials[0][2] == password_for_login) :
                print("Successfully logged in")
                time.sleep(1)
                print("Welcome " + credentials[0][0] )
                self.is_logged_in = 1
                self.user_menu(log_in_file)
            else :
                print("Incorrect username or password")
                self.app_menu()
        except FileNotFoundError :
            print("Incorrect username or password")
            self.app_menu()

    def add_task(self,log_in_file):
       # if self.is_logged_in=='1' :
            task=input("Please Tell what do you want to do : ")
            print("Please Enter the due date and time of the task :")
            year = int(input("Year in YYYY : "))
            month = int(input("Month in MM: "))
            day = int(input("Day in DD: "))
            hour = int(input("Hour in 24hr HH: "))
            min = int(input("Minute in MM: "))

            try :
                time_tuple = time.strptime('%d-%d-%d %d:%d:00' % (year, month, day, hour, min), '%Y-%m-%d %H:%M:%S')
                time_epoch = int(time.mktime(time_tuple))
            except ValueError:
                print("Incorrect date or time...please enter date and time properly and try again")
                self.add_task(log_in_file)


            filename2=open(log_in_file,'a')
            filename2.write(task+'`%d`'%(time_epoch))
            filename2.close()
            print("Adding task....")
            time.sleep(1)
            print("task added succesfully\n")
            time.sleep(1)
            self.user_menu(log_in_file)
        #else :
            #print("Please login or register")
            #self.app_menu()

    def view_task(self,log_in_file):
        #if self.is_logged_in == '1':
            filename3=open(log_in_file,'r')
            view_task_list=[]
            for line in filename3:
                parts = line.split('`')
                view_task_list.append(parts)
            filename3.close()
            count = len(view_task_list[0])
            if (count > 4) :
                print("Showing pending tasks: ")
                time.sleep(1)
                j=3
                current_time = int(time.time())
                print("Sl.no.|     Task     |    Due date    |    Time left")
                if int(view_task_list[0][4]) > current_time:
                    rem_time = int(view_task_list[0][4]) - current_time
                    print("1.    |"+view_task_list[0][3]+"|"+time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(int(view_task_list[0][4])))+"|"+"Days:%d  Hours:%d  Minutes:%d "%(rem_time/86400,(rem_time/3600)%24,(rem_time/60)%60))
                else:
                    print("1.    |" + view_task_list[0][3] + "|" + time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(int(view_task_list[0][4]))) + "|"+"Expired")
                for i in range(4,count-1) :
                    if (i % 2 == 1):
                        if int(view_task_list[0][i+1])>current_time:
                            rem_time = int(view_task_list[0][i+1]) - current_time
                            print("%d.    |"%(i-j)+view_task_list[0][i]+"|"+time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(int(view_task_list[0][i+1])))+"|"+"Days:%d  Hours:%d  Minutes:%d "%(rem_time/86400,(rem_time/3600)%24,(rem_time/60)%60))
                            j=j+1
                        else :
                            print("%d.    |" % (i - j) + view_task_list[0][i] + "|" + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(int(view_task_list[0][i + 1]))) +"|"+"Expired")
                            j=j+1
                print()
            else :
                print("You have no pending tasks")
                time.sleep(1)
            self.user_menu(log_in_file)
        #else :
           # print("Please login or register")
            #self.app_menu()
    def delete_task(self,log_in_file):
        filename4 = open(log_in_file, 'r')
        view_task_list = []
        for line in filename4:
            parts = line.split('`')
            view_task_list.append(parts)
        filename4.close()
        count = len(view_task_list[0])
        current_time = int(time.time())
        if (count > 4):
            print("Showing pending tasks: ")
            print("Sl.no.|     Task     |    Due date    |    Time left")
            time.sleep(1)
            j=3
            if int(view_task_list[0][4]) > current_time:
                rem_time = int(view_task_list[0][4]) - current_time
                print("1.    |" + view_task_list[0][3] + "|" + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(int(view_task_list[0][4]))) + "|" + "Days:%d  Hours:%d  Minutes:%d " % (rem_time / 86400, (rem_time / 3600) % 24, (rem_time / 60) % 60))
            else:
                print("1.    |" + view_task_list[0][3] + "|" + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(int(view_task_list[0][4]))) + "|" +"Expired")
            for i in range(4, count - 1):
                if(i%2==1):
                    if int(view_task_list[0][i + 1]) > current_time:
                        rem_time = int(view_task_list[0][i + 1]) - current_time
                        print("%d.    |" % (i - j) + view_task_list[0][i] + "|" + time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(int(view_task_list[0][i + 1]))) + "|" + "Days:%d  Hours:%d  Minutes:%d " % (rem_time / 86400, (rem_time / 3600) % 24, (rem_time / 60) % 60))
                        j=j+1
                    else:
                        print("%d.    |" % (i - j) + view_task_list[0][i] + "|" + time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(int(view_task_list[0][i + 1]))) + "|" +"Expired")
            print()
            task_number=int(input("Please enter which task no. you have completed : "))
            if task_number<=i-2 :
                filename5=open(log_in_file,'w')
                for i in range(0,3):
                    filename5.write(view_task_list[0][i]+"`")
                for i in range(3,2*task_number+1) :
                    filename5.write(view_task_list[0][i]+"`")
                for i in range(2*task_number+3,count-1) :
                    filename5.write(view_task_list[0][i]+"`")
                filename5.close()
                ctlog_in_file='ct'+log_in_file
                ctfile=open(ctlog_in_file,'a')
                completion_time=int(time.time())
                ctfile.write(view_task_list[0][2*task_number+1]+'`%d`'%(completion_time))
                ctfile.close()
                print("Task deleted successfully")
                time.sleep(1)
                self.user_menu(log_in_file)
            else:
                print("Invalid task no. ")
                self.user_menu(log_in_file)
        else:
            print("You have no pending tasks to be completed ")
            self.user_menu(log_in_file)

    def completed_task(self,log_in_file):
        ctlog_in_file = 'ct' + log_in_file
        if os.path.isfile(ctlog_in_file) == 1:
            filename3 = open(ctlog_in_file, 'r')
            view_task_list = []
            for line in filename3:
                parts = line.split('`')
                view_task_list.append(parts)
            filename3.close()
            count = len(view_task_list[0])
            print("Showing completed tasks: ")
            print("Sl.no.|     Task     |    Completion date  ")
            time.sleep(1)
            j=-1
            for i in range(0, count-1 ):
                if(i%2==0):
                    print("%d.    |" % (i-j) + view_task_list[0][i]+"|"+time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(int(view_task_list[0][i+1]))))
                    j=j+1
            print()
        else:
            print("You have no completed tasks")
            time.sleep(1)
        self.user_menu(log_in_file)

    def settings(self,log_in_file):
        user_response3=input("""1. Enter 1 for changing username
2. Enter 2 for changing email
3. Enter 3 for changing password
4. Enter 4 for deleting this account
5. Enter 5 to go back to previous menu """)

        if user_response3=='1' :
            self.change_username(log_in_file)
        elif user_response3=='2' :
            self.change_email(log_in_file)
        elif user_response3=='3' :
            self.change_password(log_in_file)
        elif user_response3=='4' :
            self.delete_account(log_in_file)
        elif user_response3=='5' :
            self.user_menu(log_in_file)
        else:
            print("Invalid input")
            self.settings(log_in_file)

    def change_username(self,log_in_file):
        user=input("Please enter your new username: ")
        file=open(log_in_file,'r')
        view_task_list=[]
        for line in file:
            parts = line.split('`')
            view_task_list.append(parts)
        file.close()
        view_task_list[0][0]=user
        count = len(view_task_list[0])
        file=open(log_in_file,'w')
        for i in range(0,count-1):
            file.write(view_task_list[0][i]+'`')
        file.close()
        print("Your username has been successfully changed")
        time.sleep(1)
        self.user_menu(log_in_file)

    def change_email(self,log_in_file):
        email=input("Please enter your new email: ")
        print()
        file = open(log_in_file, 'r')
        view_task_list = []
        for line in file:
            parts = line.split('`')
            view_task_list.append(parts)
        file.close()
        view_task_list[0][1] = email
        count = len(view_task_list[0])
        file = open(log_in_file, 'w')
        for i in range(0, count - 1):
            file.write(view_task_list[0][i] + '`')
        file.close()
        new_log_in_file=view_task_list[0][1]+'.txt'
        old_ctlog_in_file='ct'+log_in_file
        new_ctlog_in_file='ct'+new_log_in_file
        os.rename(log_in_file,new_log_in_file)
        os.rename(old_ctlog_in_file,new_ctlog_in_file)

        print("Your username has been successfully changed")
        time.sleep(1)
        self.app_menu()

    def change_password(self,log_in_file):
        password = input("Please enter your new password: ")
        print()
        file = open(log_in_file, 'r')
        view_task_list = []
        for line in file:
            parts = line.split('`')
            view_task_list.append(parts)
        file.close()
        view_task_list[0][2] = password
        count = len(view_task_list[0])
        file = open(log_in_file, 'w')
        for i in range(0, count - 1):
            file.write(view_task_list[0][i] + '`')
        file.close()
        print("Your password has been successfully changed")
        time.sleep(1)
        self.user_menu(log_in_file)

    def delete_account(self,log_in_file):
        yesno=input("Are you sure you want to delete your account? ")
        print()
        if yesno=='yes':
            os.remove(log_in_file)
            ct_log_in_file='ct'+log_in_file
            if os.path.isfile(ct_log_in_file) == 1:
                os.remove(ct_log_in_file)
            print("Your account have been deleted successfully")
            time.sleep(1)
            self.app_menu()
        elif yesno=='no' :
            self.user_menu(log_in_file)
        else:
            print("Please enter yes or no")
            self.delete_account(log_in_file)

    def goodbye(self):
        print("Thanks for using To-Do task manager")
        print("Closing app...")
        time.sleep(2)
        print("Closed")

    def logout(self):
        print("Logging out...")
        time.sleep(2)
        #self.is_logged_in = 0
        print("You have successfully logged out")
        time.sleep(1)
        self.app_menu()

obj=to_do_task_manager()
