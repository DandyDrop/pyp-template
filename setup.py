import setuptools

with open('requirements.txt', 'r') as f:
    requirements = f.read().split('\n')

setuptools.setup(
    name='',
    version='0.1.0',
    install_requires=requirements,
    packages=setuptools.find_packages()
)
