#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/delete-dedicated-ip-pool.html
if __name__ == '__main__':
    """
	create-dedicated-ip-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-dedicated-ip-pool.html
	list-dedicated-ip-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-dedicated-ip-pools.html
    """

    parameter_display_string = """
    # pool-name : The name of the dedicated IP pool that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("pinpoint-email", "delete-dedicated-ip-pool", "pool-name", add_option_dict)





