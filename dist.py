import sys
import shutil
import os

inspiro_version = sys.argv[1]
print("###\nStarting Build for inspiro in version %s\n###" %inspiro_version)

# Cleanup
print("Removing build folder...")
try:
    shutil.rmtree("./build")
except FileNotFoundError:
    pass
print("Removing dist folder...")
try:
    shutil.rmtree("./dist")
except FileNotFoundError:
    pass

# Build and Dist
print("Starting build...")
os.system("pyinstaller --onefile --noconsole inspiro.py")

# Add version number to executable
inspiro_exe_filename = str.format("./dist/inspiro_v{}.exe", inspiro_version)
print("Renaming executable to \"{}\"".format(inspiro_exe_filename))
os.rename(r"./dist/inspiro.exe", inspiro_exe_filename)

# Copy necessary files
print("Copying config.json to dist...")
shutil.copy("config.json", "./dist")
print("Copying quotes.csv to dist...")
shutil.copy("quotes.csv", "./dist")
print("Copying assets to dist")
shutil.copytree("./assets", "./dist/assets")

print("DONE")