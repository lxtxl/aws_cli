#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-traffic-mirror-filter-rule.html
if __name__ == '__main__':
    """
	create-traffic-mirror-filter-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-traffic-mirror-filter-rule.html
	modify-traffic-mirror-filter-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-filter-rule.html
    """

    parameter_display_string = """
    # traffic-mirror-filter-rule-id : The ID of the Traffic Mirror rule.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-traffic-mirror-filter-rule", "traffic-mirror-filter-rule-id", add_option_dict)





