import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='quote',
    version='0.5',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    description='Wrapper for the Goodreads Quote API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/maxhumber/quote',
    packages=['quote'],
    install_requires=['gazpacho'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
