#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-platform-version.html
if __name__ == '__main__':
    """
	delete-platform-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-platform-version.html
	describe-platform-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-platform-version.html
	list-platform-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-platform-versions.html
    """

    parameter_display_string = """
    # platform-name : The name of your custom platform.
    # platform-version : The number, such as 1.0.2, for the new platform version.
    # platform-definition-bundle : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("elasticbeanstalk", "create-platform-version", "platform-name", "platform-version", "platform-definition-bundle", add_option_dict)
