import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements-repl.txt', 'r') as f:
    requirements = f.read().split('\n')

setuptools.setup(
    name='pyp-template',
    version='0.1.0',
    author='DandyDrop',
    description='A python package template',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DandyDrop/pyp-template',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    keywords='python package template',
    install_requires=requirements,
    packages=setuptools.find_packages()
)
