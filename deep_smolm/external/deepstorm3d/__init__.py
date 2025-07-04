"""
Makes  import DeepSTORM3D  work even though the real package
lives one folder deeper (deepstorm3d/DeepSTORM3D).
"""
from importlib import import_module
DeepSTORM3D = import_module("DeepSTORM3D")     # load real code
import sys
sys.modules["DeepSTORM3D"] = DeepSTORM3D       # register alias