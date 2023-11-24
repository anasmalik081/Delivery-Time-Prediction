# importing libraries
from setuptools import setup, find_packages
from typing import List


# defining project information
PROJECT_NAME = 'delivery_time_prediction'
VERSION = '0.0.1'
DESCRIPTION = "Machine Learning project to predict delivery time"
AUTHOR_NAME = 'Anas Malik'
AUTHOR_EMAIL = 'anasmalik081@gmail.com'


# getting a list of dependencies
def get_requirements(file_path:str)->List[str]:
    """
    This function returns the list of requirements for this package

    Inputs: file path
    Output: list of required libraries or packages
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements


# setup
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)