"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("README.md") as history_file:
    history = history_file.read()

requirements = ["pandas", "httpx"]

setup_requirements = ["pytest-runner"]

test_requirements = [
    "pytest",
    "pytest-cov",
    "pytest-timeout",
    "black",
    "isort",
    "pylama",
]

setup(
    author="Joris den Uijl",
    author_email="jorisdenuijl@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta" "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Basic calls to the World Trading Data API with Python.",
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="wtdpy",
    name="wtdpy",
    packages=find_packages(include=["wtdpy"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/uijl/wtdpy",
    version="0.0.1",
    zip_safe=False,
)
