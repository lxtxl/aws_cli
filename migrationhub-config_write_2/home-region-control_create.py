#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/create-home-region-control.html
if __name__ == '__main__':
    """
	describe-home-region-controls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/describe-home-region-controls.html
    """

    parameter_display_string = """
    # home-region : The name of the home region of the calling account.
    # target : The target type of the deployment. Valid values are GREENGRASS and CLOUD .
Possible values:

GREENGRASS
CLOUD
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("migrationhub-config", "create-home-region-control", "home-region", "target", add_option_dict)
