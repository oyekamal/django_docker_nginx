

local = False

if local:
    from .local import *
else:
    from .docker_settings import *
