#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-environment-configuration.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # application-name : The name of the application the environment is associated with.
    # environment-name : The name of the environment to delete the draft configuration from.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticbeanstalk", "delete-environment-configuration", "application-name", "environment-name", add_option_dict)
