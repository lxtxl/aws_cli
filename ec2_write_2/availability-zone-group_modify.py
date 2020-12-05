#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-availability-zone-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # group-name : The name of the Availability Zone group, Local Zone group, or Wavelength Zone group.
    # opt-in-status : Indicates whether you are opted in to the Local Zone group or Wavelength Zone group. The only valid value is opted-in . You must contact AWS Support to opt out of a Local Zone group, or Wavelength Zone group.
Possible values:

opted-in
not-opted-in
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "modify-availability-zone-group", "group-name", "opt-in-status", add_option_dict)
