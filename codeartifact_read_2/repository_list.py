#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-repository.html
if __name__ == '__main__':
    """
	create-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/create-repository.html
	delete-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository.html
	list-repositories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-repositories.html
	update-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-repository.html
    """

    parameter_display_string = """
    # domain : The name of the domain that contains the repository to describe.
    # repository : A string that specifies the name of the requested repository.
    """

    execute_two_parameter("codeartifact", "describe-repository", "domain", "repository", parameter_display_string)