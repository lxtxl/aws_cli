#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mobile/export-bundle.html
if __name__ == '__main__':
    """
	describe-bundle : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mobile/describe-bundle.html
	list-bundles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mobile/list-bundles.html
    """

    parameter_display_string = """
    # bundle-id : Unique bundle identifier.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mobile", "export-bundle", "bundle-id", add_option_dict)





