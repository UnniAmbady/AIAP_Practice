#Setup.py
from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
name = 'AIAP_practice' ,
version='0.0.1'   ,
author = 'Ambady',
athour_email = 'ambady1960@gmail.com',
packages =find_packages(),
install_requirements = get_requirements('requirements.txt'),      
description = 'This is a practice project for AIAP'
)