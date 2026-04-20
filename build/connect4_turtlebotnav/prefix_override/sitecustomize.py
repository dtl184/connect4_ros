import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/danie/connect4_ros/install/connect4_turtlebotnav'
