#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-schedule.html
if __name__ == '__main__':
    """
	create-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-schedule.html
	describe-snapshot-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-schedules.html
	modify-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-schedule.html
    """

    parameter_display_string = """
    # schedule-identifier : A unique identifier of the snapshot schedule to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "delete-snapshot-schedule", "schedule-identifier", add_option_dict)





