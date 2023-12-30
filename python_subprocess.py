from re import sub
import subprocess #สำหรับรัน terminal command

if __name__ == "__main__":
    # basic terminal command
    #subprocess.run(["ls", "-ltr"])
    #subprocess.run(["rm", "-r", "/home/dewbtrg/testfolder1"])

    #python commands
    print(f"first run num=100 XX=90")
    subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"])
    print(f"------------------------------------------------------")
    print(f"second run num=-10 XX=-90")
    subprocess.run(["python", "firstpy.py", "--num", "-10", "--XX", "-90"])
    print(f"------------------------------------------------------")
    print(f"third run num=0")
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    print(f"------------------------------------------------------")


          
    #use output from other program
    process_output = subprocess.Popen(["python", "firstpy.py", "--num", "sum"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
    out, err = process_output.communicate()
    print(out.decode('utf-8'))
    print(len(out.decode('utf-8')))
                                      