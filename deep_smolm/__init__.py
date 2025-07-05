"""
deep_smolm package bootstrapper.

Importing this package also exposes the DeepSTORM3D code that lives in
deep_smolm/external/deepstorm3d/DeepSTORM3D so that a plain

    import DeepSTORM3D

works everywhere.
"""
# Register the alias (defined in deep_smolm.external.__init__)
from . import external as _external        # noqa: F401