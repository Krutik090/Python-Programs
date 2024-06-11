print("Select a role from below")
print("Manager,project leader,Developer")

emp = input("Enter your Role:")
bs = int(input("Enter your Basic salary:"))
HRA = bs*(5/100)
DA = bs*(105/100)
PF = bs*(10/100)

Net =(bs+HRA+DA)-PF
print("your net salary is ",Net)
