File_staff = "Jia Yi/staff.txt"
def add_staff_manager(File_staff):
    username= input(f"Enter manager username: ")
    password= input(f"Enter password: ")
    email= input(f"Enter email address: ")
    phone= input(f"Enter phone number: ")
    gender= input(f"Enter gender: ")
    experience= input(f"Enter how many years of experience: ")

    with open(File_staff, "a") as file:
        # write manager's info to the file
        file.write(f"{username} \n{password} \n{email} \n{phone} \n{gender} \n{experience} \n")
    print(f"Hello, manager {username} added successfully. ")

def edit_staff_manager(File_staff):
    username= input(f"Enter username of the manager that you want to edit: ")

    try:
        with open(File_staff, "r") as file:
            line= file.readlines() #read each line in the file into the lines list
    except FileNotFoundError:
        print(f"No staff records found")
        return
    update= False
helooooo