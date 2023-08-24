import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-ngrok",
    version="0.1.0",
    author="DandyDrop",
    description="A simple way to allow others access your Flask server using public url.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gstaff/flask-ngrok",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords='flask ngrok expose public url',
    install_requires=['Flask>=0.8', 'requests']
)
