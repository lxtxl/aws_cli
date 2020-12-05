#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-authorizer.html
	describe-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-authorizer.html
	list-authorizers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-authorizers.html
	update-authorizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-authorizer.html
    """

    write_parameter("iot", "delete-authorizer")