from setuptools import setup,find_packages
from typing import List
REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name="House_Price",
    version="0.0.1",
    author="Mahadev94",
    author_email="mahadev.mk294@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)