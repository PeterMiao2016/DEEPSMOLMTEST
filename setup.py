from setuptools import setup, find_packages

setup(
    name="deep_smolm",
    version="0.0.0",
    packages=find_packages(),   # finds deep_smolm, deep_smolm.external, …
    include_package_data=True,  # keeps data files if any
)
