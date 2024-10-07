from os import path


import setuptools


root_dir = path.abspath(path.dirname(path.dirname(__file__)))
with open(path.join(root_dir, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="test_devops",
    version="v1.5.3",
    author="T2O Media Tech",
    author_email="test@t2omedia.com",
    description="Test Devops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
