#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-service-action.html
if __name__ == '__main__':
    """
	create-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-service-action.html
	describe-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-service-action.html
	list-service-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-service-actions.html
	update-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-service-action.html
    """

    parameter_display_string = """
    # id : The self-service action identifier. For example, act-fs7abcd89wxyz .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog", "delete-service-action", "id", add_option_dict)





