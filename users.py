# Dominick Orlando 
# CIS261 Course Project Phase 4 (Second Application)

USER_FILE = "user_login.txt" 

def load_user_ids():
    user_ids = [] 
    try:
        file = open(USER_FILE, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split("|")
            user_ids.append(parts[0])
        file.close()
    except:
        pass
    return user_ids

def add_users():
    user_ids = load_user_ids()
    file = open(USER_FILE, "a")

    while True:
        user_id = input("Enter User ID, or type 'End' to exit: ")
        if user_id.lower() == "end":
            break

        if user_id in user_ids:
            print("User ID already exists. Please try another ID.")
            continue

        password = input("Enter Password:")

        auth = input("Enter Authorization Code (Only Admin or User are permitted): ")
        while auth != "Admin" and auth != "User":
            print("Authorization Code must be Admin or User.")
            auth = input("Enter Authoization Code (Admin or User): ")

        record = user_id + "|" + password + "|" + auth 
        file.write(record + "\n")
        user_ids.append(user_id)
        print("User has been saved.")

    file.close()

def display_users():
    print("\nAll Registered Users")
    try:
        file = open(USER_FILE, "r")
        for line in file: 
            line = line.strip()
            if line == "":
                continue
            parts = line.split("|")
            print("User ID", parts[0], "Password:", parts[1], "Authorization:", parts[2])
        file.close()
    except:
        print("No user data detected.")

add_users()
display_users()
