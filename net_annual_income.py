def annual_net_income(gross_salary):

    # complete your function implementation here...
    if gross_salary >= 45000:
       net_salary = gross_salary * 0.5

    elif 30000 <= gross_salary < 45000:
        net_salary = gross_salary * 0.7

    elif gross_salary < 30000:
        net_salary = gross_salary * 0.85

    return net_salary
        
gross_salary = float(input("Enter the annual gross salary: £"))
print(f"£{gross_salary} after tax is a net annual salary of £{annual_net_income(gross_salary)}.")