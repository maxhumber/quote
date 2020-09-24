from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="quote",
    version="2.0.2",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    description="quote is a wrapper for the Goodreads Quote API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxhumber/quote",
    packages=find_packages(),
    install_requires=["gazpacho>=1.0"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    keywords=["quote", "quotes", "goodreads", "wrapper", "api"],
    entry_points={"console_scripts": ["quote=quote.cli:cli"]},
    python_requires=">=3.7",
    setup_requires=["setuptools>=38.6.0"],
)
