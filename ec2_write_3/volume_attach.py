#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-availability-zone-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # device : The device name (for example, /dev/sdh or xvdh ).
    # instance-id : The ID of the instance.
    # volume-id : The ID of the EBS volume. The volume and instance must be within the same Availability Zone.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "attach-volume", "device", "instance-id", "volume-id", add_option_dict)
