#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html
if __name__ == '__main__':
    """
	delete-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-repository.html
	describe-repositories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-repositories.html
    """

    parameter_display_string = """
    # repository-name : The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app ) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app ).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecr", "create-repository", "repository-name", add_option_dict)





