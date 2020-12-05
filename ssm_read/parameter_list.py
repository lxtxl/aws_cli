#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-parameters.html
if __name__ == '__main__':
    """
	delete-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html
	delete-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameters.html
	get-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html
	get-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters.html
	put-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("ssm", "describe-parameters", add_option_dict)