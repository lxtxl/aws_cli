#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-connector-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-connector-profile.html
	describe-connector-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-profiles.html
	update-connector-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/update-connector-profile.html
    """

    write_parameter("appflow", "delete-connector-profile")