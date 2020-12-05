#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html
if __name__ == '__main__':
    """
	create-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-canary.html
	describe-canaries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-canaries.html
	get-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary.html
	start-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary.html
	stop-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/stop-canary.html
	update-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/update-canary.html
    """

    parameter_display_string = """
    # name : The name of the canary that you want to delete. To find the names of your canaries, use DescribeCanaries .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("synthetics", "delete-canary", "name", add_option_dict)





