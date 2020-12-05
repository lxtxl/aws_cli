#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-ec2-instance-recommendations.html
if __name__ == '__main__':
    """
	get-ec2-instance-recommendations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html
    """

    parameter_display_string = """
    # s3-destination-config : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("compute-optimizer", "export-ec2-instance-recommendations", "s3-destination-config", add_option_dict)





