#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-project.html
if __name__ == '__main__':
    """
	create-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-project.html
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-project.html
	get-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-projects.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the project whose name to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devicefarm", "update-project", "arn", add_option_dict)





