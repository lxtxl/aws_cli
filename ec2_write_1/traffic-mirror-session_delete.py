#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-traffic-mirror-session.html
if __name__ == '__main__':
    """
	create-traffic-mirror-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-traffic-mirror-session.html
	describe-traffic-mirror-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-traffic-mirror-sessions.html
	modify-traffic-mirror-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-session.html
    """

    parameter_display_string = """
    # traffic-mirror-session-id : The ID of the Traffic Mirror session.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-traffic-mirror-session", "traffic-mirror-session-id", add_option_dict)





