#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-registry.html
if __name__ == '__main__':
    """
	create-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-registry.html
	delete-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-registry.html
	get-registry : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-registry.html
	list-registries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-registries.html
    """

    parameter_display_string = """
    # registry-id : 
    # description : A description of the registry. If description is not provided, this field will not be updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "update-registry", "registry-id", "description", add_option_dict)
