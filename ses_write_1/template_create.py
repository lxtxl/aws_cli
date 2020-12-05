#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-template.html
if __name__ == '__main__':
    """
	delete-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-template.html
	get-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-template.html
	list-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-templates.html
	update-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/update-template.html
    """

    parameter_display_string = """
    # template : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ses", "create-template", "template", add_option_dict)





