import subprocess

def attack():
   
    f = open('hack.txt','r')
    num_lines = sum(1 for line in open('hack.txt'))
    i = 0
    content = f.readlines()
    while(i<num_lines):
        subprocess.call(["python","app.py",content[i][:-1]])
        i = i+1
if __name__ == "__main__":
    attack()