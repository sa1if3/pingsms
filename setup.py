import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pingsms-api",
    version="1.0.3",
    description="Interact with PingSMS API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sa1if3/pingsms",
    author="Md. Saifur Rahman",
    author_email="saif@techflow360.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"],
)
