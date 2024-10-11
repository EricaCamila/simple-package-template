from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="teste_ericamila0002",
    version="0.0.1",
    author="my_name",
    author_email="my_email",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)