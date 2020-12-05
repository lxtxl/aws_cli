#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-alias.html
if __name__ == '__main__':
    """
	create-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-alias.html
	update-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-alias.html
    """

    parameter_display_string = """
    # alias-name : The alias to be deleted. The alias name must begin with alias/ followed by the alias name, such as alias/ExampleAlias .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kms", "delete-alias", "alias-name", add_option_dict)





