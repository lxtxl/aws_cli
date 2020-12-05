#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/remove-tags.html
if __name__ == '__main__':
    """
	add-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/add-tags.html
	list-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-tags.html
    """

    parameter_display_string = """
    # resource-id : Specifies the ARN of the trail from which tags should be removed. The format of a trail ARN is:

arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudtrail", "remove-tags", "resource-id", add_option_dict)





