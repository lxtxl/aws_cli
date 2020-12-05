#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-config-rule.html
if __name__ == '__main__':
    """
	describe-config-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rules.html
	put-config-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-config-rule.html
    """

    parameter_display_string = """
    # config-rule-name : The name of the AWS Config rule that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "delete-config-rule", "config-rule-name", add_option_dict)





