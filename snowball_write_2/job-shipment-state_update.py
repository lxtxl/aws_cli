#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/update-job-shipment-state.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : The job ID of the job whose shipment date you want to update, for example JID123e4567-e89b-12d3-a456-426655440000 .
    # shipment-state : The state of a device when it is being shipped.
Set to RECEIVED when the device arrives at your location.
Set to RETURNED when you have returned the device to AWS.
Possible values:

RECEIVED
RETURNED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("snowball", "update-job-shipment-state", "job-id", "shipment-state", add_option_dict)
