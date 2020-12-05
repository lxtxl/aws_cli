#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-credit-specification.html
if __name__ == '__main__':
    """
	describe-instance-credit-specifications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-credit-specifications.html
    """

    parameter_display_string = """
    # instance-credit-specifications : Information about the credit option for CPU usage.
(structure)

Describes the credit option for CPU usage of a burstable performance instance.
InstanceId -> (string)

The ID of the instance.

CpuCredits -> (string)

The credit option for CPU usage of the instance. Valid values are standard and unlimited .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "modify-instance-credit-specification", "instance-credit-specifications", add_option_dict)





