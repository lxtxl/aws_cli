#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/update-resource-collection.html
if __name__ == '__main__':
    """
	get-resource-collection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/get-resource-collection.html
    """

    parameter_display_string = """
    # action : Possible values:

ADD
REMOVE
    # resource-collection : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("devops-guru", "update-resource-collection", "action", "resource-collection", add_option_dict)
