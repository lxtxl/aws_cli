#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-constraint.html
if __name__ == '__main__':
    """
	create-constraint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-constraint.html
	delete-constraint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-constraint.html
	describe-constraint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-constraint.html
    """

    parameter_display_string = """
    # id : The identifier of the constraint.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog", "update-constraint", "id", add_option_dict)





