# Ahmed Abdel Hameed Abdel Qader
# Tech- Amb Track

# ======================  Imports  ====================
import json
import pickle
import ast
import re
from builtins import print
from os import uname_result

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

f_users = open("users.txt","a")
f_projects = open("projects.txt")

#  Logged in user email
global_email=None

# ========================== Functions Def

# ==========================    1-  Vadation Methods =================================================
def check_email(email):
     if re.search(regex, email):
           return True
     else:
           return  False

def validate_empty(*args):
     for arg in args:
           if len(arg):
                 return True
           else:
                 return False

def vaildate_date(_date):
      pass
def vaildate_mobile(_mobile):
      pass

# ============================= 3- branching Functions ==================
def branching_project_operation(second_choice , userEmail):
            if second_choice == 1:
                  add_project(userEmail,get_all_projcts_byUserEmail(userEmail))
            elif second_choice == 2:
                  update_projct_byUserEmail(user_info)
            elif second_choice == 3:
                  delete_projct_byUserEmail(userEmail)
            elif second_choice == 4:
                  print(get_all_projcts_byUserEmail(userEmail))
            else:
                  exit()
# ============================= 3- Decoration functions ============================================
def welcome_operations():
      print(" \t please Press on your choice ... \n"
            " \t \t 1- Login , you have an Account \n"
            " \t \t 2- Register , Create New User \n"
            " \t \t 3- Exit, Close The App \n")


def project_operations():
      print(" \t select what you want to do ... \n"
            " \t \t 1- Add project \n"
            " \t \t 2- Update project \n"
            " \t \t 3- Delete Project \n"
            "\t \t 4- Get your Project \n")


# ============================= 2-   CRUD Operations ============================================

def login(email, password):
      f_users = open("users.txt", "r")
      lines = f_users.readline()
      while lines:
            js = json.loads(lines)
            lines = f_users.readline()  # Get the next line
            print(js)
            if js['Email'] == email and js['Password']==password:
                  print("Logged In Successfully ! ")
                  global_email=js['Email']
                  return True
            else:
                  continue

def get_userInfo(userEmail):
        f_users = open("users.txt","r")
        lines= f_users.readline()
        while lines:
              js = json.loads(lines)
              print(js)
              lines = f_users.readline() # Get the next line
              # print(lines[2])
              print(js['Email'])
              if js['Email'] == userEmail:
                    print("founded ! ")
                    return js
                    break

def register(users):
      f_users = open("users.txt","a")
      f_users.write(json.dumps(users)+"\n")
      print("Registered Successfully ! \n")
      print("Your Data : \t \t ",users)
      f_users.close()

def get_all_projcts_byUserEmail(userEmail):
      f_users = open("users.txt", "r")
      lines = f_users.readline()
      while lines:
            js = json.loads(lines)
            lines = f_users.readline()  # Get the next line
            if js['Email'] == userEmail:
                  print("Found")
                  # print(type(js['projects'][0]))
                  return js['projects']


def add_project(userEmail,projects):
      project_title = input("Enter project title : \t")
      project_details = input("Enter Project details(Description) : \t")
      project_target_total = input("Enter Project Total budget (Cost) : \t")
      project_start_date = input("Enter Project Start Date : \t")
      project_end_date = input("Enter Projec End Date : \t")
      new_project={
         "title":project_title,
         "details": project_details,
         "total target": project_target_total,
         "start": project_start_date,
         "end": project_end_date
      }

      dictionary_copy = new_project.copy()
      projects.append(dictionary_copy)

      # Get the user to update

def update_projct_byUserEmail(user_email):
      f_users = open("users.txt", "r+")
      lines = f_users.readline()
      while lines:
            js = json.loads(lines)
            print(js)
            lines = f_users.readline()  # Get the next line
            # print(lines[2])
            print(js['Email'])
            if js['Email'] == user_email:
                  print("founded ! ")
                  return js
                  break


def get_projct_byId(projectId):
      print("get - p - id")

def get_all_projcts_ByUserId(userId,projectId):
      print("get - p - all")

def update_projct_byId(userId,projectId):
      print("update - p")
def delete_projct_byUserEmail(userEmail):
      print("del - p -id")
def delete_projct_byId(userId,projectId):
      print("del - p -id")
def delete_all_projct(userId):
      print("del - p-all")

# ==============  App Flow  =====================

# ============================ Login || Registeration Branching ======================
print(" \n \n \t \t \t  Welcome To Your App \n ")

while True:
      welcome_operations()  #  Get the Dashboard for user management
      first_choice = int(input("Enter Your CHoice from the previus Menue \t "))

      if first_choice == 1:
            user_email = input("Enter Your Email : \t")
            user_password = input("Enter Your Password : \t")
            if login(user_email, user_password):
                  print("Success !  ")
                  # Get the Projects operation
                  project_operations()
                  # User Input
                  while True:
                        second_choice = int(input(" \t \t Enter Your Choice from the previus Menue \t "))
                        branching_project_operation(second_choice,user_email)
            else:
                  print("Wrong User Name or  Password !! ")

            # login("ahmed","123")

      elif first_choice==2:
            user_firstName=input("Enter Your First Name : \t")
            user_lastName = input("Enter Your Last Name : \t")
            user_email = input("Enter Your Email : \t")
            user_password = input("Enter Your Password : \t")
            user_confirmPassword = input("Enter Password Again : \t")
            project_title = input("Enter project title : \t")
            project_details = input("Enter Project details(Description) : \t")
            project_target_total = input("Enter Project Total budget (Cost) : \t")
            project_start_date = input("Enter Project Start Date : \t")
            project_end_date = input("Enter Projec End Date : \t")

            if validate_empty(user_firstName,user_lastName, user_email,user_password) and check_email(user_email) and user_password==user_confirmPassword:
                  users = {
                        "First_Name": user_firstName,
                        "Last_Name": user_lastName,
                        "Email": user_email,
                         "Password": user_password,
                         "projects":[{
                              "title":project_title,
                              "details": project_details,
                              "total target": project_target_total,
                              "start": project_start_date,
                              "end": project_end_date
                        }]
                  }
                  # Call Register Function
                  register(users)
            else:
                  print("Empty Fileds Not Allowed !! \t \t OR Email Not Valid  \t \t Unmatched password\n ")




      else:
            exit()

# =============  Projects

projects={
      "title":"",
      "details": "",
      "total target": "",
      "start": "",
      "end": ""
}