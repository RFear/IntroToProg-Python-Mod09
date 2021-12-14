# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudocode to start assignment 9
# RFear,12.12.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as emp
    from ProcessingClasses import FileProcessor as fp
    from IOClasses import EmployeeIO as io
else:
    raise Exception("This file was not created to be imported.")

# global variables
emp_data = 'EmployeeData.txt'
per_data = 'PersonData.txt'  # may be able to remove
lst_objs = []

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
temp_list = fp.read_data_from_file(emp_data)
for item in temp_list:
    lst_objs.append(emp(item[0], item[1], item[2]))

io.print_current_list_items(lst_objs)

while True:
    io.print_menu_items()  # Show user a menu of options
    choice = io.input_menu_options()  # Get user's menu option choice

    if choice == '1':  # Show user current data in the list of employee objects
        io.print_current_list_items(lst_objs)

    elif choice == '2':  # Let user add data to the list of employee objects
        while True:
            try:
                new_employee = io.input_employee_data()
                for item in lst_objs:
                    if new_employee.employee_id == item.employee_id:
                        raise Exception
            except:
                print("WARNING:  Employee ID in use. Please choose another ID.")
                ids = []
                for item in lst_objs:
                    ids.append(item.employee_id)
                print(f"The employee ID in user are: {ids}")
            else:
                lst_objs.append(new_employee)
                break

    elif choice == '3':  # let user save current data to file
        fp.save_data_to_file(emp_data, lst_objs)
        print(f"Data has been saved to the file: '{emp_data}'!")

    elif choice == '4':  # Let user exit program
        print("Program is exiting...")
        break
