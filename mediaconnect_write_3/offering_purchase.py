#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/purchase-offering.html
if __name__ == '__main__':
    """
	describe-offering : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-offering.html
	list-offerings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/list-offerings.html
    """

    parameter_display_string = """
    # offering-arn : The Amazon Resource Name (ARN) of the offering.
    # reservation-name : The name that you want to use for the reservation.
    # start : The date and time that you want the reservation to begin, in Coordinated Universal Time (UTC). You can specify any date and time between 12:00am on the first day of the current month to the current time on todayâs date, inclusive. Specify the start in a 24-hour notation. Use the following format: YYYY-MM-DDTHH:mm:SSZ, where T and Z are literal characters. For example, to specify 11:30pm on March 5, 2020, enter 2020-03-05T23:30:00Z.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("mediaconnect", "purchase-offering", "offering-arn", "reservation-name", "start", add_option_dict)
