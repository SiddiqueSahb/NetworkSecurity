from setuptools import find_packages,setup
from typing import List

def get_requirments() -> List[str]:
    """
    This function will return list of requirements

    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found")
    return requirement_lst  

print(get_requirments())       



#setup meta-data
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Mohammad Asim",
    author_email="asimsiddiqui776@gmail.com",
    packages=find_packages(),
    install_requires = get_requirments()
)