import setuptools

with open("README.rst", "r") as fh:  #removed encoding="utf-8"
    long_description = fh.read()

requirements = ["numpy"]

setuptools.setup(
    name="pyqudit",
    version="0.0.6",
    author="Ordoptimus, Rutuja343, kimyona-crypt",
    author_email="orodaux@gmail.com",
    description="Quantum Computing package. Use qudit gates and build simple N-D circuits.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ordoptimus/pyqudit",
    project_urls={
        "Bug Tracker": "https://github.com/ordoptimus/pyqudit/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(   #removed where='pyqudit',
        exclude=("tests",) #try [] instead of ()
        ),
    package_dir = {"pyqudit":"pyqudit"},
    install_requires=requirements,
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pyqudit=qudit.__main__:main",
        ]
    },
)
