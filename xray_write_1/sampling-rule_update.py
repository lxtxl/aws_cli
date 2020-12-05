#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/update-sampling-rule.html
if __name__ == '__main__':
    """
	create-sampling-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/create-sampling-rule.html
	delete-sampling-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/delete-sampling-rule.html
	get-sampling-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-sampling-rules.html
    """

    parameter_display_string = """
    # sampling-rule-update : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("xray", "update-sampling-rule", "sampling-rule-update", add_option_dict)





