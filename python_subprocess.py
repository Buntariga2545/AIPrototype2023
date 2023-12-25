from multiprocessing import process
import subprocess
from sys import stdout #สำหรับรัน terminal command

if __name__ == "__main__":
    # basic terminal command
    print('first run num=100 XX=90')
    subprocess.run(["python","firstpy.py", "--num", "100", "--XX", "90"])
    print('------------------------------------------------------')
    print('second run num=-10 XX=-90')
    subprocess.run(["python","firstpy.py", "--num", "-10", "--XX", "-90"])
    print('------------------------------------------------------')
    print('third run num=0')
    subprocess.run(["python","firstpy.py", "--num", "0"])
    print('------------------------------------------------------')

    process_output = subprocess.Popen(["python", "firstpy.py", "--num", "0"],
                                      stdout=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
    out, err = process_output.communicate()
    print(out.decode('utf-8'))
    print(len(out.decode(utf-8)))
                                      