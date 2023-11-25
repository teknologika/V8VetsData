from setuptools import find_packages, setup

with open("README.md","r") as f:
    long_description = f.read()

setup (
    name="vetsdata",
    version="0.0.1",
    description="Data from the iRacing V8 Veterans League",
    package_dir={"":"app"},
    packages=find_packages(where="app"),
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/teknologika/V8VetsData",
    author='Bruce McLeod',
    author_email='nospam+bruce@teknologika.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    install_requires=["pandas >= 1.25.2"]
)
    
