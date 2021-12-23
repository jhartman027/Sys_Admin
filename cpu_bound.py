import os

def main():
 dir_num = int(raw_input("Enter number of dirs to create: "))

 for dir in range(dir_num):
  dir_name = "Folder_%s" %dir # Creates the directory name

  os.mkdir(dir_name) #Creates directories in current directory
main()