# deep_smolm/external/__init__.py
"""
Expose the DeepSTORM3D code that sits in
deep_smolm/external/deepstorm3d/DeepSTORM3D
so that a plain  import DeepSTORM3D  works.
"""
import importlib.util, pathlib, sys

_pkg_dir = pathlib.Path(__file__).parent / "deepstorm3d" / "DeepSTORM3D"
_init_py = _pkg_dir / "__init__.py"

# Build a module spec from the real __init__.py
_spec = importlib.util.spec_from_file_location("DeepSTORM3D", _init_py)
_mod  = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)        # execute the real package
sys.modules["DeepSTORM3D"] = _mod     # register alias
