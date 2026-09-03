class Employee:
    def __init__(self, emp_id, name, designation, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_deductions(self):
        return self.basic_salary * 0.05

    def calculate_net_salary(self):
        gross = self.basic_salary + self.calculate_hra() + self.calculate_da()
        net = gross - self.calculate_deductions()
        return net

    def display_payslip(self):
        print("\n" + "=" * 40)
        print(f"Payslip for {self.name} ({self.designation})")
        print("=" * 40)
        print(f"Employee ID     : {self.emp_id}")
        print(f"Basic Salary    : {self.basic_salary:.2f}")
        print(f"HRA             : {self.calculate_hra():.2f}")
        print(f"DA              : {self.calculate_da():.2f}")
        print(f"Deductions      : {self.calculate_deductions():.2f}")
        print(f"Net Salary      : {self.calculate_net_salary():.2f}")
        print("=" * 40)


class Manager(Employee):
    def __init__(self, emp_id, name, basic_salary, team_size):
        super().__init__(emp_id, name, "Manager", basic_salary)
        self.team_size = team_size

    def calculate_hra(self):
        return self.basic_salary * 0.25

    def calculate_bonus(self):
        return self.team_size * 500

    def calculate_net_salary(self):
        base_net = super().calculate_net_salary()
        return base_net + self.calculate_bonus()

    def display_payslip(self):
        super().display_payslip()
        print(f"Team Size       : {self.team_size}")
        print(f"Bonus           : {self.calculate_bonus():.2f}")
        print(f"Updated Net Pay : {self.calculate_net_salary():.2f}")
        print("=" * 40)


class SalaryProcessingSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def process_all_salaries(self):
        for emp in self.employees:
            emp.display_payslip()

    def total_payout(self):
        return sum(emp.calculate_net_salary() for emp in self.employees)


def main():
    system = SalaryProcessingSystem()
    n = int(input("Enter number of employees to add: "))

    for i in range(n):
        print(f"\nEmployee {i + 1}")
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        is_manager = input("Is this employee a manager? (y/n): ").lower() == "y"
        basic_salary = float(input("Enter Basic Salary: "))

        if is_manager:
            team_size = int(input("Enter Team Size: "))
            employee = Manager(emp_id, name, basic_salary, team_size)
        else:
            designation = input("Enter Designation: ")
            employee = Employee(emp_id, name, designation, basic_salary)

        system.add_employee(employee)

    system.process_all_salaries()
    print(f"\nTotal Payout for all employees: {system.total_payout():.2f}")


if __name__ == "__main__":
    main()