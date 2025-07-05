"""
Expose   import DeepSTORM3D
for the vendored copy inside deep_smolm/external/deepstorm3d/DeepSTORM3D
"""
import importlib, pathlib, sys

# folder that *contains* the DeepSTORM3D package
_vendor_root = pathlib.Path(__file__).with_suffix('') / "deepstorm3d"

# put that folder on sys.path (only once)
sys.path.insert(0, str(_vendor_root))

# import it, then pin it in sys.modules under the canonical name
_mod = importlib.import_module("DeepSTORM3D")
sys.modules["DeepSTORM3D"] = _mod
