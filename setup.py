from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='my_package',
    version='1.0.0',
    author='Pramod',
    author_email='pramodvepada99@gmail.com',
    description='A sample package',
    packages=find_packages(),  # Automatically discover and include all packages in the project
    install_requires= get_requirements('requirements.txt')
)