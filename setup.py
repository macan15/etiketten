from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in etiketten/__init__.py
from etiketten import __version__ as version

setup(
	name="etiketten",
	version=version,
	description="Drucken von Etiketten",
	author="Stefan Macanovic",
	author_email="stefan.macan@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
