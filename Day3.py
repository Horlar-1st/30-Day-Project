# Predefined credentials
username = "Moshood"
password = "Success_1"

# number of trials and the counts
n_trials = 3                # 3 trials
count = 0

# the while loop
while count < n_trials:
    name = input("Enter your username: ")
    pass_ = input("Enter your password: ")

    if name == username and password == pass_:
        print("Login Successfully!!")
        break
    elif (name == username and password != pass_) and count != n_trials - 1:
        print(f"Incorrect password!! You have {n_trials - count -1} more trials.")
    elif name != username and count != n_trials - 1:
        print(f"Incorrect login details!! You have {n_trials - count - 1} more trials.")
    elif count == n_trials - 1:
        print(f"Try again! Or contact the IT manager")
    
    print("-"*50)
    count += 1
