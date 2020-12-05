#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-crawler-schedule.html
if __name__ == '__main__':
    """
	start-crawler-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-crawler-schedule.html
	stop-crawler-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-crawler-schedule.html
    """

    parameter_display_string = """
    # crawler-name : The name of the crawler whose schedule to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "update-crawler-schedule", "crawler-name", add_option_dict)





