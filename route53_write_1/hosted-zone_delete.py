#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-hosted-zone.html
if __name__ == '__main__':
    """
	create-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html
	get-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html
	list-hosted-zones : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones.html
    """

    parameter_display_string = """
    # id : The ID of the hosted zone you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("route53", "delete-hosted-zone", "id", add_option_dict)





