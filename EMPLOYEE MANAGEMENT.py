class Employee:
    emp_count = 0

    def __init__(self, emp_id, name, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary
        Employee.emp_count += 1

    def display(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: Rs.{self.salary}")

class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        if emp_id in self.employees:
            print("Employee with this ID already exists.")
            return
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        salary = float(input("Enter Salary: "))
        emp = Employee(emp_id, name, designation, salary)
        self.employees[emp_id] = emp
        print("Employee added successfully.")

    def view_all(self):
        if not self.employees:
            print("No employees found.")
        else:
            for emp in self.employees.values():
                emp.display()

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in self.employees:
            self.employees[emp_id].display()
        else:
            print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            Employee.emp_count -= 1
            print("Employee deleted.")
        else:
            print("Employee not found.")

    def total_employees(self):
        print(f"Total Employees: {Employee.emp_count}")

def main():
    manager = EmployeeManager()
    while True:
        print("\n1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Total Employees")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.view_all()
        elif choice == '3':
            manager.search_employee()
        elif choice == '4':
            manager.delete_employee()
        elif choice == '5':
            manager.total_employees()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
