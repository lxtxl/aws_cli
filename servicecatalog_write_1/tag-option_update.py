#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-tag-option.html
if __name__ == '__main__':
    """
	create-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-tag-option.html
	delete-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-tag-option.html
	describe-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-tag-option.html
	list-tag-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-tag-options.html
    """

    parameter_display_string = """
    # id : The TagOption identifier.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog", "update-tag-option", "id", add_option_dict)





