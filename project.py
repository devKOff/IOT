class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")

    def view_employees(self):
        if not self.employees:
            print("No employees in the system.")
            return
        print("Employee List:")
        for employee in self.employees:
            employee.display_info()

    def update_employee_salary(self, emp_id, new_salary):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.salary = new_salary
                print(f"Salary updated for employee {employee.name}.")
                return
        print(f"Employee with ID {emp_id} not found.")

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"Employee {employee.name} removed.")
                return
        print(f"Employee with ID {emp_id} not found.")

# Example usage
if __name__ == "__main__":
    ems = EmployeeManagementSystem()

    # Adding employees
    emp1 = Employee(101, "John Doe", "Manager", 70000)
    emp2 = Employee(102, "Jane Smith", "Developer", 60000)
    ems.add_employee(emp1)
    ems.add_employee(emp2)

    # Viewing employees
    ems.view_employees()

    # Updating salary
    ems.update_employee_salary(101, 75000)
    ems.view_employees()

    # Removing an employee
    ems.remove_employee(102)
    ems.view_employees()