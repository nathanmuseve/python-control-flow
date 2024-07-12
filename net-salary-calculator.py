# Write a program whose major task is to calculate an individual’s Net Salary by getting the inputs of basic salary and benefits. Calculate the payee (i.e. Tax), NHIF Deductions, NSSF Deductions, gross salary, and net salary. 

basic_salary = int(input("Enter your basic salary:"))
benefits = int(input("Enter your benefits:"))

#detactions  
nssf = ""
taxable_income = ""
personal_relief = ""
paye = ""
nhif = ""
insurance_relief = ""
housing_levy = ""
affordable_housing = ""
net_pay = ""
