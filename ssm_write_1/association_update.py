#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-association.html
if __name__ == '__main__':
    """
	create-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association.html
	delete-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-association.html
	describe-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association.html
	list-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-associations.html
    """

    parameter_display_string = """
    # association-id : The ID of the association you want to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "update-association", "association-id", add_option_dict)





