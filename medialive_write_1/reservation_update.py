#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-reservation.html
if __name__ == '__main__':
    """
	delete-reservation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-reservation.html
	describe-reservation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-reservation.html
	list-reservations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-reservations.html
    """

    parameter_display_string = """
    # reservation-id : Unique reservation ID, e.g. â1234567â
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("medialive", "update-reservation", "reservation-id", add_option_dict)





