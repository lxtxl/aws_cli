#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshot-attribute.html
if __name__ == '__main__':
    """
	modify-snapshot-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-snapshot-attribute.html
	reset-snapshot-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-snapshot-attribute.html
    """

    parameter_display_string = """
    # attribute : The snapshot attribute you would like to view.
Possible values:

productCodes
createVolumePermission
    # snapshot-id : The ID of the EBS snapshot.
    """

    execute_two_parameter("ec2", "describe-snapshot-attribute", "attribute", "snapshot-id", parameter_display_string)