from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Insurance Price Prediction"
VERSION = "0.0.1"
DESCRIPTION = """The goal of this project is to give people an estimate of how much they need based on
                their individual health situation. After that, customers can work with any health
                insurance carrier and its plans and perks while keeping the projected cost from our
                study in mind. This can assist a person in concentrating on the health side of an
                insurance policy rather than the ineffective part."""


AUTHOR_NAME = "Anuj Dhyani"
AUTHOR_EMAIL = "anujdhyani232@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."
# Requriments.txt file open
# read
# \n ""
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requriment_file:
        requriment_list = requriment_file.readlines()
        requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

        if HYPHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPHEN_E_DOT)

        return requriment_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requries = get_requirements_list()
     )