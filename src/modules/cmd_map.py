from .copy import copy
from .file import file
from .synchronize import synchronize
from .command import command
from .template import template
cmd_map = {"copy": copy, "file": file, "synchronize": synchronize, "command": command, "template": template}
