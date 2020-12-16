#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-snapshot-schedule.html
if __name__ == '__main__':
    """
	delete-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-snapshot-schedule.html
	describe-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-snapshot-schedule.html
    """

    parameter_display_string = """
    # volume-arn : The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a list of gateway volumes.
    # start-at : The hour of the day at which the snapshot schedule begins represented as hh , where hh is the hour (0 to 23). The hour of the day is in the time zone of the gateway.
    # recurrence-in-hours : Frequency of snapshots. Specify the number of hours between snapshots.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("storagegateway", "update-snapshot-schedule", "volume-arn", "start-at", "recurrence-in-hours", add_option_dict)
