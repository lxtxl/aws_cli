#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/purchase-reserved-elasticsearch-instance-offering.html
if __name__ == '__main__':
    """
	describe-reserved-elasticsearch-instance-offerings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-reserved-elasticsearch-instance-offerings.html
    """

    parameter_display_string = """
    # reserved-elasticsearch-instance-offering-id : The ID of the reserved Elasticsearch instance offering to purchase.
    # reservation-name : A customer-specified identifier to track this reservation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("es", "purchase-reserved-elasticsearch-instance-offering", "reserved-elasticsearch-instance-offering-id", "reservation-name", add_option_dict)
