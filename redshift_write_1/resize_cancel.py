#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/cancel-resize.html
if __name__ == '__main__':
    """
	describe-resize : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-resize.html
    """

    parameter_display_string = """
    # cluster-identifier : The unique identifier for the cluster that you want to cancel a resize operation for.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "cancel-resize", "cluster-identifier", add_option_dict)





