#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-directory-config.html
if __name__ == '__main__':
    """
	create-directory-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-directory-config.html
	delete-directory-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-directory-config.html
	describe-directory-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-directory-configs.html
    """

    parameter_display_string = """
    # directory-name : The name of the Directory Config object.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appstream", "update-directory-config", "directory-name", add_option_dict)





