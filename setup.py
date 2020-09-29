import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

with open("requirements-dev.txt", "r") as f:
    requirements_dev = f.readlines()

setuptools.setup(
    name="wl-jira",
    version="0.1.0",
    author="Robert Hansel",
    author_email="oss@fam-hansel.de",
    description="Simple CLI tool to handle worklogs with JIRA",
    license="Apache 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HaRo87/wl-jira",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        # see: https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: Apache 2.0",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={"develop": requirements_dev},
    entry_points={
        "console_scripts": [
            "wlj=wljira.wljira:cli",
        ]
    },
)