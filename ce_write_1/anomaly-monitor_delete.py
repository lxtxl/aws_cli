#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-anomaly-monitor.html
if __name__ == '__main__':
    """
	create-anomaly-monitor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-anomaly-monitor.html
	get-anomaly-monitors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-anomaly-monitors.html
	update-anomaly-monitor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-anomaly-monitor.html
    """

    parameter_display_string = """
    # monitor-arn : The unique identifier of the cost anomaly monitor that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ce", "delete-anomaly-monitor", "monitor-arn", add_option_dict)





