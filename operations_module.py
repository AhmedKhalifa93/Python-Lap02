import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
phone_regex='(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
import json
phone_egypt='^01[0125]\d{8}$'

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
      if re.search(phone_egypt, _mobile):
            return True
      else:
            return False

# ============================= 3- branching Functions ==================
def branching_project_operation(second_choice , userEmail):
            if second_choice == 1:
                  add_project(userEmail,get_all_projcts_byUserEmail(userEmail))
            elif second_choice == 2:
                  update_projct_byUserEmail(userEmail)
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
