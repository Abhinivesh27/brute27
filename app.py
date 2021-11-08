import sys
def login(pass_key):
    match_key = "ten" #len 1
    if (pass_key == match_key):
        print("Login Success")
    else:
        print("Failed")

if __name__ == "__main__":
    pass_ = sys.argv[1]
    login(pass_)