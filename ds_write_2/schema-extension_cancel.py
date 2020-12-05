#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/cancel-schema-extension.html
if __name__ == '__main__':
    """
	list-schema-extensions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-schema-extensions.html
	start-schema-extension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/start-schema-extension.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory whose schema extension will be canceled.
    # schema-extension-id : The identifier of the schema extension that will be canceled.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "cancel-schema-extension", "directory-id", "schema-extension-id", add_option_dict)
