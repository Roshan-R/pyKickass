from sys import platform
import os
import subprocess

try:
    from subprocess import DEVNULL  # Python 3.
except ImportError:
    DEVNULL = open(os.devnull, 'wb')

screenshot_tools = ['gnome-screenshot', 'spectacle', 'deepin-screenshot', 'xfce4-screenshooter', 'maim']
#screenshot_tools = ['1gnome-screenshot', '1spectacle', '1deepin-screenshot', '1xfce4-screenshooter', '1maim']

def takeScreenshot(basename):
    if platform == "win32":
            os.system('explorer.exe ms-screenclip:')
            import time
            print('Screenshot captured. Opening image for viewing.')
            time.sleep(9) # It takes some time to register the screenshot into the clipboard

            from PIL import ImageGrab
            img = ImageGrab.grabclipboard()
            img.show()
            outputimage = "outputfolder/pics/" + basename + ".png"
            img.save(outputimage, 'PNG')

    elif platform=="linux":
        try:
            outputimage = "outputfolder/pics/" + basename + ".png"
            if os.getenv("WAYLAND_DISPLAY"): # If user is running wayland session
                print("Using grim for taking screenshot..")
                print(os.getenv("WAYLAND_DISPLAY"))
                grim = subprocess.run("grim", stdout=DEVNULL, stderr=DEVNULL)
                if grim.returncode == 1 : #GNOME does not support grim screenshots
                    subprocess.run(['gnome-screenshot', '-a', '-f', "outputfolder/pics/"+ outputimage]) #assuming the DE in question is GNOME
                else:
                    try:
                        cmd = 'grim -g "$(slurp)" outputfolder/pics/' + outputimage
                        print(cmd)
                        os.system(cmd)
                    except:
                        print("Not Working")
            else:
                try:
                    tool = get_tool()
                    if tool == "gnome-screenshot":
                        out  = subprocess.run(['gnome-screenshot', '-a', '-f', outputimage], stdout=DEVNULL, stderr=DEVNULL)
                    elif tool == "spectacle":
                        out  = subprocess.run(['spectacle', '-b', '-r', '-o', outputimage], stdout=DEVNULL, stderr=DEVNULL)
                    elif tool == "deepin-screenshot":
                        out  = subprocess.run(['deepin-screenshot', '-s', outputimage], stdout=DEVNULL, stderr=DEVNULL)
                    elif tool == "xfce4-screenshooter":
                        out  = subprocess.run(['xfce4-screenshooter', '-r', '-s', outputimage], stdout=DEVNULL, stderr=DEVNULL)
                    elif tool == "maim":
                        out  = subprocess.run(['maim', '-s', outputimage], stdout=DEVNULL, stderr=DEVNULL)
                    else:
                        print("please install maim to continue...")
                except:
                    print("Something happened....")
                    exit()
        except:
            print("Some error occured")
            exit()

    elif platform == "darwin":
        outputimage = self.basename + ".png"
        ret  = subprocess.run(['screencapture', '-i',  "outputfolder/pics/"+ outputimage]) 

def get_tool():
    tool = ""
    for x in screenshot_tools:
        proc = subprocess.Popen(['which', x], stdout=subprocess.PIPE) 
        out, err = proc.communicate() 
        if out:
            tool = x
            return tool
    return ""
