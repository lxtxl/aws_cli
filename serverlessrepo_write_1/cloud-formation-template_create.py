#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-template.html
if __name__ == '__main__':
    """
	get-cloud-formation-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/get-cloud-formation-template.html
    """

    parameter_display_string = """
    # application-id : The Amazon Resource Name (ARN) of the application.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("serverlessrepo", "create-cloud-formation-template", "application-id", add_option_dict)





