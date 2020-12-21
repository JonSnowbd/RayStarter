import glob
import argparse
import os
import subprocess

# Build config here.
cc = "gcc"
file = "{{cookiecutter.project_name}}"
binfolder = "bin"

# ============= No Editing below
# Config based on platform now
cfiles = []
ldflags = ["-Isrc", "-Iinclude"] # Default include folders
defaultflags = ["-std=c99"]
debugflags = ["-Wextra", "-Wall", "-g"]
releaseflags = ["-Os", "-s"]
defines = []

if os.name == "nt": # WINDOWS
    defines.append("WINDOWS")
    file = file+".exe"
    ldflags = ldflags + ["-Wl,--subsystem,windows","-lraylib","-lopengl32","-lgdi32","-lwinmm","-static","-lpthread"]
else: # LINUX, Untested but should work.
    defines.append("LINUX")
    ldflags = ldflags + ["-lraylib", "-lGL", "-lm", "-lpthread", "-ldl", "-lrt", "-lX11"]

folder = os.path.dirname(os.path.realpath(__file__))
bincontainer = os.path.join(folder, binfolder)
file_output = os.path.join(bincontainer, file)

cfiles = ["main.c"] + glob.glob("src/**/*.c", recursive=True)

# Parser Setup
parser = argparse.ArgumentParser(description='The build script for {{cookiecutter.project_name}}')
parser.add_argument("--release", "-r", action="store_true", help="Build {{cookiecutter.project_name}} with release features and optimization.")
parser.add_argument("--gdb", "-g",     action="store_true", help="Launch {{cookiecutter.project_name}} with GDB after build(precedence over -l)")
parser.add_argument("--launch", "-l",  action="store_true", help="Launch {{cookiecutter.project_name}} after build")
parser.add_argument("--output", "-o",  action="store_true", help="Show the CC command that will be ran.")
args = parser.parse_args()

if(args.release == False):
    defines.append("DEBUG")
else:
    defines.append("RELEASE")

command = cc
command += " "+" ".join(cfiles)
command += " -o "+file_output

if len(defines) > 0:
    for d in defines:
        command += " -D "+d

command += " "+" ".join(defaultflags)

if args.release: # C flags:
    command += " "+" ".join(releaseflags)
else:
    command += " "+" ".join(debugflags)

command += " "+" ".join(ldflags)

if(args.output):
    print("\n===\n"+command+"\n===\n")

# Create the bin folder if it doesnt exist already.
os.makedirs(bincontainer, mode=0o777, exist_ok=True)

print("Building {{cookiecutter.project_name}}...", end=" ")
command_res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
if command_res.returncode != 0:
    print("Welp, something went wrong. StdErr:\n"+command_res.stderr+"\n\n StdOut:\n"+command_res.stdout)
else:
    print("Success!")
    if args.release:
        print("Minimizing Binary...", end=" ")
        upx_res = subprocess.run("upx "+file_output, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        if upx_res.returncode != 0:
            print("Failed! Errors are as follows:\n"+upx_res.stderr)
        else:
            print("Finished!")
    if args.launch or args.gdb:
        print ("Launching {{cookiecutter.project_name}}...")
        os.chdir(bincontainer)
        if args.gdb:
            if args.release:
                print("Warning! GDB might act weird with a release build .exe and breaking.\n")
            os.system("gdb "+file) # GDB Will not output properly with subprocess run. Use old syscall
        else:
            game_res = subprocess.run(file, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
            if game_res.returncode == 0:
                print("Lovely! Works fine.")
            else:
                print("Welp, something went wrong. StdErr:\n"+game_res.stderr+"\n\n StdOut:\n"+game_res.stdout)