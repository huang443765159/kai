import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="XYZGuides",
    version="0.0.7",
    author="huangkai",
    # author_email="author@example.com",
    # description="A small example package",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/WillEEEEEE/VISUAL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


'''
[Real Python]
pip3 install .
pip3 uninstall XYZMission


[Will's MAC]
/usr/bin/python3 -m pip install .
/usr/bin/python3 -m pip uninstall XYZMission
'''