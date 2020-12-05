#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/stop-continuous-export.html
if __name__ == '__main__':
    """
	describe-continuous-exports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-continuous-exports.html
	start-continuous-export : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-continuous-export.html
    """

    parameter_display_string = """
    # export-id : The unique ID assigned to this export.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("discovery", "stop-continuous-export", "export-id", add_option_dict)





