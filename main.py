# Ahmed Abdel Hameed Abdel Qader
# Tech- Amb Track

# ======================  Imports  ====================
import json
import pickle
import ast
import re
from builtins import print
from os import uname_result
import operations_module

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
phone_regex='(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

f_users = open("users.txt","a")
f_projects = open("projects.txt")

#  Logged in user email
global_email=None



# ==============  App Flow  =====================

# ============================ Login || Registeration Branching ======================
print(" \n \n \t \t \t  Welcome To Your App \n ")

while True:
      operations_module.welcome_operations()  #  Get the Dashboard for user management
      first_choice = int(input("Enter Your CHoice from the previus Menue \t "))

      if first_choice == 1:
            user_email = input("Enter Your Email : \t")
            user_password = input("Enter Your Password : \t")
            if operations_module.login(user_email, user_password):
                  print("Success !  ")
                  # Get the Projects operation
                  operations_module.project_operations()
                  # User Input
                  while True:
                        second_choice = int(input(" \t \t Enter Your Choice from the previus Menue \t "))
                        operations_module.branching_project_operation(second_choice,user_email)
            else:
                  print("Wrong User Name or  Password !! ")

            # login("ahmed","123")

      elif first_choice==2:
            user_firstName=input("Enter Your First Name : \t")
            user_lastName = input("Enter Your Last Name : \t")
            user_email = input("Enter Your Email : \t")
            user_phone= input("Enter Your phone : \t")
            user_password = input("Enter Your Password : \t")
            user_confirmPassword = input("Enter Password Again : \t")
            project_title = input("Enter project title : \t")
            project_details = input("Enter Project details(Description) : \t")
            project_target_total = input("Enter Project Total budget (Cost) : \t")
            project_start_date = input("Enter Project Start Date : \t")
            project_end_date = input("Enter Projec End Date : \t")

            if operations_module.validate_empty(user_firstName,user_lastName, user_email,user_password) and operations_module.check_email(user_email) and user_password==user_confirmPassword and operations_module.vaildate_mobile(user_phone):
                  users = {
                        "First_Name": user_firstName,
                        "Last_Name": user_lastName,
                        "phone": user_lastName,
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
                  operations_module.register(users)
            else:
                  print("Empty Fileds Not Allowed !! \t \t OR Email Not Valid  \t \t Unmatched password\n ")




      else:
            exit()

# =============  Projects