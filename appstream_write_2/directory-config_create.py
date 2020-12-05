#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-directory-config.html
if __name__ == '__main__':
    """
	delete-directory-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-directory-config.html
	describe-directory-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-directory-configs.html
	update-directory-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-directory-config.html
    """

    parameter_display_string = """
    # directory-name : The fully qualified name of the directory (for example, corp.example.com).
    # organizational-unit-distinguished-names : The distinguished names of the organizational units for computer accounts.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appstream", "create-directory-config", "directory-name", "organizational-unit-distinguished-names", add_option_dict)
