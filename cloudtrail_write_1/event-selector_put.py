#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html
if __name__ == '__main__':
    """
	get-event-selectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-selectors.html
    """

    parameter_display_string = """
    # trail-name : Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:

Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
Start with a letter or number, and end with a letter or number
Be between 3 and 128 characters
Have no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.
Not be in IP address format (for example, 192.168.5.4)

If you specify a trail ARN, it must be in the format:

arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudtrail", "put-event-selectors", "trail-name", add_option_dict)





