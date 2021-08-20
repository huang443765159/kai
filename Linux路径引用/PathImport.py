import os
import sys
launch_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
root_dir = os.path.dirname(launch_dir)
sys.path.append(root_dir)