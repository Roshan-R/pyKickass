import sys
import os
import re
import subprocess
from sys import platform

class kickass:

    def verifyFiles(self):
        import os.path
        for i in range(1, len(sys.argv)):
            if not os.path.exists(sys.argv[i]):
                print("Make sure those files exist")


    def readfile(self):
        self.basename = sys.argv[1].split(".")[0]
        try:
            with open(sys.argv[1], 'r') as file:
                self.code = file.read()
                self.ctoalgo()

        except FileNotFoundError:
            print("File not found.")

    def replace_stuff(self):
        code_pattern = "--CODE--"
        algo_pattern = "--ALGORITHM--"
        f = open("baseout.tex", 'r')
        text = f.read()

        text = re.sub(code_pattern,self.code, text)
        text = re.sub(algo_pattern,self.algorithm, text)
        print(text)
        self.takescreenshot()


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
        for key, value in replace_strings.items():
            self.algorithm = re.sub(key, value, self.code)

    def compile(self):
        try:
            gcc_ret = subprocess.run(["gcc", sys.argv[1],"-o",self.basename])
            if gcc_ret.returncode != 0:
                print("You have some compile issues")
                exit()
            self.run()
        except PermissionError:
            print("Make sure you have gcc installed and it is in your $PATH variable")
            exit()

    def run(self):
        if platform == "win32":
            pass
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
a.readfile()
a.replace_stuff()


