#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-host-reservation-purchase-preview.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # host-id-set : The IDs of the Dedicated Hosts with which the reservation is associated.
(string)
    # offering-id : The offering ID of the reservation.
    """

    execute_two_parameter("ec2", "get-host-reservation-purchase-preview", "host-id-set", "offering-id", parameter_display_string)