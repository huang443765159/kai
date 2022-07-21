import setuptools

setuptools.setup(
    name="XYZChemicals4",
    version="2022.06.28.17.43",
    author="HuangKai",
    url="https://github.com/WillEEEEEE/XYZUtils4.git",
    packages=setuptools.find_packages(),
    package_data={
        '': ['**/*.ini', '**/*.json']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
