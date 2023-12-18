from setuptools import find_packages, setup
from typing import List

HYPHEN = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements    
    """
    requirements = []
    with open(file_path) as file_obg:
        requirements = file_obg.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)

    return requirements


setup(
    name='capstone_project01',
    version='0.0.1',
    author='snl',
    author_email='snl4994@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
