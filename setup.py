from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Learn_math",
    version="0.0.1",
    author="Ricardo Augusto Nisiide",
    author_email="rnisiide@gmail.com",
    description="Calculator that shows the basic math operations",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rnisiide/projeto_packages_creation',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)