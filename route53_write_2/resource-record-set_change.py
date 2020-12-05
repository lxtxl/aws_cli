#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/change-resource-record-sets.html
if __name__ == '__main__':
    """
	list-resource-record-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-resource-record-sets.html
    """

    parameter_display_string = """
    # hosted-zone-id : The ID of the hosted zone that contains the resource record sets that you want to change.
    # change-batch : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "change-resource-record-sets", "hosted-zone-id", "change-batch", add_option_dict)
