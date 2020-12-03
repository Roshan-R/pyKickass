import sys
import os
import re
import subprocess
from sys import platform

from tex import intro, section, first, end
class kickass:

    def __init__(self):
        self.name = ""
        self.verifyFiles()
        self.kick()
        self.save_text()

    def save_text(self):
        with open("outputfolder/output.tex", "w") as output:
            output.write(self.text)
            print("Output is written as output.tex")

        # os.rename("outputfolder/output.txt", "outputfolder/output.tex")
        self.zipPref = input("Do you want to make a .zip file for uploading to overleaf (y/N) : ")
        if self.zipPref == "y" or self.zipPref == "Y":

            import zipfile
            zipf = zipfile.ZipFile('output.zip', 'w', zipfile.ZIP_DEFLATED)
            for root, dirs, files in os.walk("./outputfolder"):
                for file in files:
                    zipf.write(os.path.join(root, file))
            zipf.close()
            print("output.zip created sucessfully!")

    def verifyFiles(self):
        import os.path
        for i in range(1, len(sys.argv)):
            if not os.path.exists(sys.argv[i]):
                print("Make sure those files exist")
                exit()
        if os.path.isdir("outputfolder"):
            print("A directory called outputfolder already exists!")
            print("please delete the directory to continue")
            exit()

    def platformStuff(self):
        if platform == "win32":
            self.basename = sys.argv[self.currentIndex].split(".\\")[1].split(".")[0]
            self.executable_name = self.basename + ".exe"
        elif platform == "linux":
            self.basename = sys.argv[self.currentIndex].split(".")[0]
            self.executable_name = self.basename

    def readfile(self):
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
        aim_pattern = "--AIM--"

        if len(sys.argv) > 2 :
            if self.currentIndex == 1:
                self.text = "%s%s%s" % (intro, first, section)
                # self.text = intro + first + section 
            else:
                    self.section = "%s%s" % (self.text, section)
        else:
            self.text = "%s%s%s%s" %(intro, first, section, end)
            # self.text = intro + first + section + end

        print()
        aim = input("Enter the aim of this program : ")
        print()

        self.text = re.sub(code_pattern,self.code, self.text)
        self.text = re.sub(algo_pattern,self.algorithm, self.text)
        self.text = re.sub(number_pattern,str(self.currentIndex), self.text)
        self.text = re.sub(name_pattern,self.name, self.text)
        self.text = re.sub(title_pattern,self.title, self.text)
        self.text = re.sub(aim_pattern,aim, self.text)
        # print(self.text)
        if self.screenshot_pref != "n" and self.screenshot_pref != "N":
            self.text = re.sub(screenshot_pattern,self.basename, self.text)
            self.takescreenshot()

    def kick(self):
        print("Welcome to the script ! ")
        print()

        self.name = input("Enter your name : ")
        self.title = input("Enter the title : ")

        self.screenshot_pref = input("Do you want to take screenshot ? (Y/n) : ")

        try:
            os.mkdir("outputfolder")
            os.mkdir("outputfolder/pics")
        except FileExistsError:
            print("A directory called outputfolder already exists!")
            print("please delete the directory to continue")
            exit()

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
                print("compilation completed sucessfully")
        except :
            print("Make sure you have gcc installed and it is in your $PATH variable")
            exit()
        self.run()

    def run(self):
        print()
        if platform == "win32":
            print("Opening cmd for making screenshot")
            print("run .\\"+ self.executable_name)
            run_cmd = subprocess.run(["cmd.exe"])
        elif platform == "linux":
            print("Opening bash for making screenshot")
            print("run ./"+ self.executable_name)
            run_bash = subprocess.run(["bash"])

    def takescreenshot(self):
        self.compile()

        if platform == "win32":
            import win32api
            import win32con

            os.system('explorer.exe ms-screenclip:')
            import time
            print('Screenshot captured. Opening image for viewing.')
            time.sleep(9) # It takes some time to register the screenshot into the clipboard

            from PIL import ImageGrab
            img = ImageGrab.grabclipboard()
            img.show()
            outputimage = "outputfolder/pics/" + self.basename + ".png"
            img.save(outputimage, 'PNG')

        elif platform=="linux":
            try:
                outputimage = self.basename + ".png"
                maim_ret = subprocess.run(["maim", "-s", "outputfolder/pics/"+ outputimage])
            except PermissionError:
                print("Make sure maim is installed")


a = kickass()
# a.verifyFiles()
# a.readfile()
# a.replace_stuff()
