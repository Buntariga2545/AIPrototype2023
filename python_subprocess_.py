from re import sub
import subprocess

def extract_numeric(text):
    for line in text.splitlines():
        if line.strip().isdigit() or (line.strip().lstrip('-').isdigit() and '-' in line):
            return int(line.strip())
    return 0

def printHello():
    print("Hello World!")
    
if __name__ == "__main__":

    print(f"first run num=100 XX=90")
    p1 = subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"])
    print(f"------------------------------------------------------\n")
    print(f"second run num=-10 XX=-90")
    p2 = subprocess.run(["python", "firstpy.py", "--num", "-10", "--XX", "-90"])
    print(f"------------------------------------------------------\n")
    print(f"third run num=0")
    p3 = subprocess.run(["python", "firstpy.py", "--num", "0"])
    print(f"------------------------------------------------------\n")

    result1 = extract_numeric(p1.stdout.decode('utf-8'))
    result2 = extract_numeric(p2.stdout.decode('utf-8'))
    result3 = extract_numeric(p3.stdout.decode('utf-8'))

    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print(f"Result 3: {result3}")

    result_sum = sum([result1, result2, result3])
    print(f"Summation of {result1} + ({result2}) + {result3} is: {result_sum}")
    printHello()
