import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grqs",
    version="0.1",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    description="Wrapper for Goodreads Quote Search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxhumber/grqs",
    packages=setuptools.find_packages(),
    install_requires=[
        'bs4',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
