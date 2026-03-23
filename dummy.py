import sys
import os

print(sys.argv)
cwd = os.getcwd()
print(cwd)

script_path = os.path.join(cwd, sys.argv[0])
print(script_path)
