#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-retention-configuration.html
if __name__ == '__main__':
    """
	describe-retention-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-retention-configurations.html
	put-retention-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-retention-configuration.html
    """

    parameter_display_string = """
    # retention-configuration-name : The name of the retention configuration to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "delete-retention-configuration", "retention-configuration-name", add_option_dict)





