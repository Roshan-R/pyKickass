import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyKickass", # Replace with your own username
    version="0.0.1",
    author="Roshan R Chandar",
    author_email="roshan@cet.ac.in",
    description="Python program to help create assignments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Roshan-R/pyKickass",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['pyKickass=pyKickass.pyKickass:main'],
    },
    python_requires='>=3.6',
)

