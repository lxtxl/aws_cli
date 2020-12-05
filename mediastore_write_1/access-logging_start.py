#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/start-access-logging.html
if __name__ == '__main__':
    """
	stop-access-logging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/stop-access-logging.html
    """

    parameter_display_string = """
    # container-name : The name of the container that you want to start access logging on.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediastore", "start-access-logging", "container-name", add_option_dict)





