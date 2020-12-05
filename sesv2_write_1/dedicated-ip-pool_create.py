#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-dedicated-ip-pool.html
if __name__ == '__main__':
    """
	delete-dedicated-ip-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-dedicated-ip-pool.html
	list-dedicated-ip-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-dedicated-ip-pools.html
    """

    parameter_display_string = """
    # pool-name : The name of the dedicated IP pool.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sesv2", "create-dedicated-ip-pool", "pool-name", add_option_dict)





