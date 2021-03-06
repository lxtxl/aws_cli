#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/stop-bulk-deployment.html
if __name__ == '__main__':
    """
	list-bulk-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-bulk-deployments.html
	start-bulk-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/start-bulk-deployment.html
    """

    parameter_display_string = """
    # bulk-deployment-id : The ID of the bulk deployment.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("greengrass", "stop-bulk-deployment", "bulk-deployment-id", add_option_dict)





