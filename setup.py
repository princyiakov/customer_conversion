from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        # Read the file and strip newlines from each line
        requirements = [line.strip() for line in file_obj]

        # Remove the `HYPEN_E_DOT` string if it's present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='customer_conversion',
    version='0.0.1',
    author='Princy Iakov',
    author_email='princy.iakov@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
