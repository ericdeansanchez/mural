import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ericdeansanchez", # Replace with your own username
    version="0.0.1",
    author="Eric Sanchez",
    author_email="ericsanchez@berkeley.edu",
    description="A micro library for manipulating palette colors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericdeansanchez/mural",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)