#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-application-version.html
if __name__ == '__main__':
    """
	list-application-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/list-application-versions.html
    """

    parameter_display_string = """
    # application-id : The Amazon Resource Name (ARN) of the application.
    # semantic-version : The semantic version of the new version.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("serverlessrepo", "create-application-version", "application-id", "semantic-version", add_option_dict)
