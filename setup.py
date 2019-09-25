import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='quote',
    version='0.5',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    description='Goodreads Quote Search',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/maxhumber/quote',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
