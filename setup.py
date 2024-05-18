from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    '''
    函数作用将requirements.txt里面转换成List形式
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [rep.replace("\n", "") for rep in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name="ML_project_1",
version="0.0.1",
author="holy",
author_email="2725731392@qq.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")

)