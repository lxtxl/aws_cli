#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-world-template.html
if __name__ == '__main__':
    """
	create-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-world-template.html
	delete-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-world-template.html
	describe-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-world-template.html
	list-world-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-world-templates.html
    """

    parameter_display_string = """
    # template : The Amazon Resource Name (arn) of the world template to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "update-world-template", "template", add_option_dict)





