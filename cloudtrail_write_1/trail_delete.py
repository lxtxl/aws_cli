#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-trail.html
if __name__ == '__main__':
    """
	create-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-trail.html
	describe-trails : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/describe-trails.html
	get-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail.html
	list-trails : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-trails.html
	update-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-trail.html
    """

    parameter_display_string = """
    # name : Specifies the name or the CloudTrail ARN of the trail to be deleted. The format of a trail ARN is: arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudtrail", "delete-trail", "name", add_option_dict)





