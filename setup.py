from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in okr/__init__.py
from okr import __version__ as version

setup(
	name="okr",
	version=version,
	description="OKR management app",
	author="emc",
	author_email="girum@eternal-media.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
