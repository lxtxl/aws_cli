#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-capacity-reservation.html
if __name__ == '__main__':
    """
	create-capacity-reservation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-capacity-reservation.html
	describe-capacity-reservations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-reservations.html
	modify-capacity-reservation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-capacity-reservation.html
    """

    parameter_display_string = """
    # capacity-reservation-id : The ID of the Capacity Reservation to be cancelled.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "cancel-capacity-reservation", "capacity-reservation-id", add_option_dict)





