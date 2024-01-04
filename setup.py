from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:

    '''
    this function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
#metadata about my project

setup(
    name = 'ML Project',
    version = '0.0.1',
    author = 'Anushka Rai',
    author_email= 'anushka010mca23@igdtuw.ac.in',
    packages = find_packages(), #it checks for __init.py file. Treats it like package
    install_requires = get_requirements('requirements.txt') # all the packages are present in requirements.txt file

)