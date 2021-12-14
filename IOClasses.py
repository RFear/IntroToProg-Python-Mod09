# ---------------------------------------------------------- #
# Title: Listing 11
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RFear,12.12.2021,Modified script to print data correctly.
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else:
    import DataClasses as DC


class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

        input_employee_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """

    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options:
        1) Show current employee data.
        2) Add new employee data.
        3) Save employee data to file.
        4) Exit program.
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee lstrows

        :param list_of_rows: (list) of lstrows you want to display
        """
        print("******* The current items employees are: *******")
        print("Employee ID |First Name  |Last Name  ")
        for row in list_of_rows:
            print('{0: <12}'.format(str(row.employee_id))
                  + "|"
                  + '{0: <12}'.format(row.first_name)
                  + "|"
                  + '{0: <12}'.format(row.last_name))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_employee_data():
        """ Gets data for an employee object

        :return: (employee) object with input data
        """
        emp = ''
        try:
            employee_id = (input("What is the employee Id? - ").strip())
            first_name = str(input("What is the employee First Name? - ").strip())
            last_name = str(input("What is the employee Last Name? - ").strip())
            print()  # Add an extra line for looks
            emp = DC.Employee(employee_id, first_name, last_name)
        except Exception as e:
            print(e)
        return emp
