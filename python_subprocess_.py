import numbers
from re import sub
import subprocess
import argparse

def extract_numeric(word):
    for i in word.splitlines():
       if i.strip().isdigit() or (i.strip().lstrip('-').isdigit() and '-' in i):
            return int(i.strip())
    return 0

#def sum_numbers(a, b):
#    return a + b
#print(sum_numbers(1, 2))

#def parse_input():
#    parser = argparse.ArgumentParser()

#    args = parser.parse_args()
#    return args

def printHello():
    print("Hello World!")
    
if __name__ == "__main__":

    print(f"first run num=100 XX=90")
    p1 = subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"], capture_output=True)
    print(f"------------------------------------------------------\n")
    print(f"second run num=-10 XX=-90")
    p2 = subprocess.run(["python", "firstpy.py", "--num", "-10", "--XX", "-90"], capture_output=True)
    print(f"------------------------------------------------------\n")
    print(f"third run num=0")
    p3 = subprocess.run(["python", "firstpy.py", "--num", "0"], capture_output=True)
    print(f"------------------------------------------------------\n")

    output1 = extract_numeric(p1.stdout.decode('utf-8'))
    output2 = extract_numeric(p2.stdout.decode('utf-8'))
    output3 = extract_numeric(p3.stdout.decode('utf-8'))

#    print(f"Result 1: {result1}")
#    print(f"Result 2: {result2}")
#    print(f"Result 3: {result3}")

    total_sum = sum([output1, output2, output3])
    print(f"Summation of: {output1} + ({output2}) + {output3} = {total_sum}")
    printHello()
