def print_menu():
    print("╔═════════════════════════════════════╗")
    print("║         PAYCHECK CALCULATOR          ║")
    print("╠═════════════════════════════════════╣")
    print("║  1. Start Pay Calculation            ║")
    print("║  2. Exit                             ║")
    print("╚═════════════════════════════════════╝")

def calculate_regular_pay(hours_worked, hourly_rate):
    # Constants based on provided example
    federal_tax_rate = 410.82 / 2550.00
    social_security_tax_rate = 158.10 / 2550.00
    medicare_tax_rate = 36.98 / 2550.00

    # Calculate regular earnings
    regular_pay = hours_worked * hourly_rate

    # Calculate taxes
    federal_tax = regular_pay * federal_tax_rate
    social_security_tax = regular_pay * social_security_tax_rate
    medicare_tax = regular_pay * medicare_tax_rate

    # Calculate take-home pay
    total_taxes = federal_tax + social_security_tax + medicare_tax
    take_home_pay = regular_pay - total_taxes

    return regular_pay, take_home_pay, total_taxes

def calculate_overtime_pay(overtime_hours, hourly_rate):
    # Constants based on provided example
    overtime_rate_multiplier = 1.5
    federal_tax_rate = 410.82 / 2550.00
    social_security_tax_rate = 158.10 / 2550.00
    medicare_tax_rate = 36.98 / 2550.00

    # Calculate overtime earnings
    overtime_pay = overtime_hours * hourly_rate * overtime_rate_multiplier

    # Calculate taxes
    federal_tax = overtime_pay * federal_tax_rate
    social_security_tax = overtime_pay * social_security_tax_rate
    medicare_tax = overtime_pay * medicare_tax_rate

    # Calculate take-home pay
    total_taxes = federal_tax + social_security_tax + medicare_tax
    take_home_pay = overtime_pay - total_taxes

    return overtime_pay, take_home_pay, total_taxes

def main():
    while True:
        print_menu()
        choice = input("Please choose an option (1-2): ")
        
        if choice == '1':
            print("\nLet's start calculating your paycheck!")
            try:
                hourly_rate = float(input("\nEnter your hourly rate: "))
                if hourly_rate <= 0:
                    print("Hourly rate must be greater than zero.")
                    continue

                hours_worked = float(input("\nEnter the total number of hours you worked this week: "))
                if hours_worked < 0:
                    print("Hours worked cannot be negative.")
                    continue

                calculate_overtime = input("Would you like to calculate overtime hours separately? (y/n): ").lower()

                if calculate_overtime == 'y':
                    # Overtime kicks in after 40 hours
                    regular_hours = min(hours_worked, 40)  # Up to 40 hours for regular time
                    overtime_hours = max(0, hours_worked - 40)  # Anything over 40 hours is overtime

                    # Calculate pay for regular hours
                    regular_gross, regular_take_home, regular_taxes = calculate_regular_pay(regular_hours, hourly_rate)
                    
                    # Calculate pay for overtime hours
                    overtime_gross, overtime_take_home, overtime_taxes = calculate_overtime_pay(overtime_hours, hourly_rate)
                else:
                    # All hours are calculated as regular hours (no overtime split)
                    regular_hours = hours_worked
                    overtime_hours = 0
                    regular_gross, regular_take_home, regular_taxes = calculate_regular_pay(regular_hours, hourly_rate)
                    overtime_gross = overtime_take_home = overtime_taxes = 0.00

                # Combine regular and overtime for total
                total_gross = regular_gross + overtime_gross
                total_taxes = regular_taxes + overtime_taxes
                total_take_home = regular_take_home + overtime_take_home

                # Print the summary
                print("\n╔═══════════════════════════════════════╗")
                print(f"  Summary for {hours_worked:.2f} hours worked this week")
                print("╠═══════════════════════════════════════╣")
                print(f"  Regular Hours Worked  : {regular_hours:.2f} hours")
                print(f"  Overtime Hours Worked : {overtime_hours:.2f} hours")
                print("╠═══════════════════════════════════════╣")
                print(f"  Gross Pay             : ${total_gross:.2f}")
                print(f"  Total Taxes           : ${total_taxes:.2f}")
                print(f"  Take Home Pay         : ${total_take_home:.2f}")
                print("╚═══════════════════════════════════════╝\n")
            except ValueError:
                print("Please enter a valid number for hours worked and hourly rate.")
        elif choice == '2':
            print("\nThank you for using the Paycheck Calculator!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
