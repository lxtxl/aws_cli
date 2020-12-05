#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-retention-configuration.html
if __name__ == '__main__':
    """
	delete-retention-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-retention-configuration.html
	describe-retention-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-retention-configurations.html
    """

    parameter_display_string = """
    # retention-period-in-days : Number of days AWS Config stores your historical information.

Note
Currently, only applicable to the configuration item history.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "put-retention-configuration", "retention-period-in-days", add_option_dict)





