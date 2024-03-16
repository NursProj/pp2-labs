import os
import string 

#1
# a=os.listdir()
# print(a)

#2
# path=os.getcwd() #get current working directory
# if os.access(path, os.F_OK): # F_OK - существование файла
#     print("exist")
# else:
#     print("not exist")
    
# if os.access(path, os.R_OK): R_OK читать
#     print("readable")
# else:
#     print("not readable")
    
# if os.access(path, os.W_OK): #W_OK записать
#     print("writable")
# else:
#     print("not writable")
      
# if os.access(path, os.X_OK): #X_OK исполняемый
#     print("execute")
# else:
#     print("not execute")
    
#3
# path=os.getcwd()
# if os.path.exists(path):
#     print("exists")
#     filename = os.path.basename(path)
#     direct = os.path.dirname(path)
#     print(filename)
#     print(direct)
# else:
#     print("doesnt exist")   
    
#4
# file_path="demofile.txt"
# with open(file_path, 'r') as file:
#     line_count = 0
#     for line in file:
#         line_count += 1
# print(line_count+1)

#5
# MyList=[1,2,3,4,5,6]
# with open("demofile.txt", 'w') as file:
#     for i in MyList:
#         file.write(str(i)+', ') 
        
#6
# alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for letter in alphabet:
#         filename = letter + ".txt"
#         with open(filename, 'w') as file:
#             file.write("This is file " + filename)
        
#7
# with open('source.txt', 'r') as source:
#     with open('receiver.txt', 'w') as receiver:
#         receiver.write(source.read())
        
#8
file_path = os.getcwd() 
file_name = "name_of_file.txt" 
file_to_delete = os.path.join(file_path, file_name)  
if os.path.exists(file_to_delete) and os.access(file_to_delete, os.X_OK):
    os.remove(file_to_delete)
       
