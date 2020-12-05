#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-volume.html
if __name__ == '__main__':
    """
	attach-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-volume.html
	delete-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-volume.html
	describe-volumes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volumes.html
	detach-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-volume.html
	modify-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume.html
    """

    parameter_display_string = """
    # availability-zone : The Availability Zone in which to create the volume.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "create-volume", "availability-zone", add_option_dict)





