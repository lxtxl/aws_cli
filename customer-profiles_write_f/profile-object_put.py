#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-profile-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-profile-object.html
	list-profile-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-profile-objects.html
    """

    write_parameter("customer-profiles", "put-profile-object")