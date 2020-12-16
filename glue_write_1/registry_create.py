#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-registry.html
if __name__ == '__main__':
    """
	delete-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-registry.html
	get-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-registry.html
	list-registries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-registries.html
	update-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-registry.html
    """

    parameter_display_string = """
    # registry-name : Name of the registry to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "create-registry", "registry-name", add_option_dict)





