from .copy import copy
from .file import file
from .synchronize import synchronize
from .command import command
cmd_map = {"copy": copy, "file": file, "synchroize": synchronize, "command": command}
