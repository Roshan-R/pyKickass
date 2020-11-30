import sys
import os
import re
import subprocess
from sys import platform

class kickass:

    def __init__(self):
        self.text = ""
        self.name = ""
        self.verifyFiles()
        self.kick()
        self.save_text()


    def save_text(self):
        with open("output.tex", "w+") as output:
            output.write(self.text)
            print("Output is written as output.tex")



    def verifyFiles(self):
        import os.path
        for i in range(1, len(sys.argv)):
            if not os.path.exists(sys.argv[i]):
                print("Make sure those files exist")
                exit()



    def platformStuff(self):
        if platform == "win32":
            self.basename = sys.argv[self.currentIndex].split(".\\")[1].split(".")[0]
            self.executable_name = self.basename + ".exe"
        elif platform == "linux":
            self.basename = sys.argv[self.currentIndex].split(".")[0]
            self.executable_name = self.basename

    def readfile(self):
        print(sys.argv[self.currentIndex])
        try:
            with open(sys.argv[self.currentIndex], 'r') as file:
                self.code = file.read()
                self.platformStuff()
                self.ctoalgo()

        except FileNotFoundError:
            print("File not found.")


    def replace_stuff(self):
        code_pattern = "--CODE--"
        algo_pattern = "--ALGORITHM--"
        screenshot_pattern = "--OUTPUT--"
        number_pattern = "--NUMBER--"
        name_pattern = "--NAME--"
        title_pattern = "--TITLE--"

        if len(sys.argv) > 2 :
            if self.currentIndex == 1:
                with open("first.tex", 'r') as first:
                    self.text = first.read()
            else:
                with open('partbaseout.tex', 'r') as part:
                    self.text = self.text + part.read()
        else:
            with open('baseout.tex', 'r') as base:
                self.text = base.read()

        self.text = re.sub(code_pattern,self.code, self.text)
        self.text = re.sub(algo_pattern,self.algorithm, self.text)
        self.text = re.sub(screenshot_pattern,self.basename, self.text)
        self.text = re.sub(number_pattern,str(self.currentIndex), self.text)
        self.text = re.sub(name_pattern,self.name, self.text)
        self.text = re.sub(title_pattern,self.title, self.text)
        # print(self.text)
        self.takescreenshot()

    def kick(self):
        print("Welcome to the script ! ")
        print()

        self.name = input("Enter your name : ")
        self.title = input("Enter the title : ")

        for i in range(1, len(sys.argv)):
            self.currentIndex = i
            print("Current file : ", sys.argv[self.currentIndex])
            self.readfile()
            self.replace_stuff()


    def ctoalgo(self):
        replace_strings = {
            "{":"",
            "}":"",
            "#.*":"",
            r"\/\/.*":"",
            # "ifs":"IF",
            r"while\s*\((.*)\)":"WHILE \\1 : ",
            r"\|\|":"or",
            r"if\s(\(.*\))":"If \\1 THEN",
            r"printf\s*\((.*)\);":"PRINT \\1",
            r"puts\((.*)\)":"/PRINT \\1",
            r"fgets\(([^,]*).*\)":"INPUT \\1",
            r"scanf\((.*).*\)":"INPUT \\1",
            r"--":" Decrements ",
            r"\+\+":" Increments ",
            r"for \(\w*\s(\w*)[^;]*; ([^;]*);.*\)":"FOR \\1 till \\2 do ",
            r";":"",
            r"return":"RETURN",
            r"void (.*)\(.*\)|int (.*)\(.*\)":"Start of function \\1\\2",
            r"\/\* [\w\W]* \*\/":"",
            r"\/\*[\w\.\s]*\*\/":"",

        }
        algorithm = self.code
        for key, value in replace_strings.items():
            algorithm = re.sub(key, value, algorithm)
        self.algorithm = algorithm
        # print(self.algorithm)

    def compile(self):
        try:
            # print(self.executable_name)
            print("Compiling ...")
            gcc_ret = subprocess.run(["gcc", sys.argv[self.currentIndex],"-o",self.executable_name])
            if gcc_ret.returncode != 0:
                print("You have some compile issues")
                exit()
            else:
                print("compilation done sucessfully")
        except :
            print("Make sure you have gcc installed and it is in your $PATH variable")
            exit()
        self.run()

    def run(self):
        print("Compilation completed sucessfully!")
        print()
        print("Running the program for making screeshot ")
        if platform == "win32":
            run_cmd = subprocess.run(["cmd.exe"])
        elif platform == "linux":
            run_bash = subprocess.run(["bash"])

    def takescreenshot(self):
        self.compile()

        if platform == "win32":
            import win32api
            import win32con

            win32api.keybd_event(win32con.VK_LSHIFT,0,0,0) 
            win32api.keybd_event(win32con.VK_LWIN,0,0,0) 
            win32api.keybd_event(0x53,0,0,0)

            win32api.keybd_event(win32con.VK_LSHIFT,0,win32con.KEYEVENTF_KEYUP,0) 
            win32api.keybd_event(win32con.VK_LWIN,0,win32con.KEYEVENTF_KEYUP,0) 
            win32api.keybd_event(0x53,0,win32con.KEYEVENTF_KEYUP,0)

            import time
            time.sleep(4) # It takes some time to register the screenshot into the clipboard

            from PIL import ImageGrab
            img = ImageGrab.grabclipboard()
            img.show()

        elif platform=="linux":
            try:
                outputimage = self.basename + ".png"
                maim_ret = subprocess.run(["maim", "-s",outputimage])
            except PermissionError:
                print("Make sure maim is installed")


a = kickass()
# a.verifyFiles()
# a.readfile()
# a.replace_stuff()


