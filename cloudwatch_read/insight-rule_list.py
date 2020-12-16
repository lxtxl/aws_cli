#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-insight-rules.html
if __name__ == '__main__':
    """
	delete-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-insight-rules.html
	disable-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/disable-insight-rules.html
	enable-insight-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/enable-insight-rules.html
	put-insight-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-insight-rule.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("cloudwatch", "describe-insight-rules", add_option_dict)