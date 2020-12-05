#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-organization-config-rule.html
if __name__ == '__main__':
    """
	delete-organization-config-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-organization-config-rule.html
	describe-organization-config-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-organization-config-rules.html
    """

    parameter_display_string = """
    # organization-config-rule-name : The name that you assign to an organization config rule.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "put-organization-config-rule", "organization-config-rule-name", add_option_dict)





