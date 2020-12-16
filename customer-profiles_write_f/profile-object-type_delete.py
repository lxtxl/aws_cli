#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-profile-object-type.html
	list-profile-object-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-profile-object-types.html
	put-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-profile-object-type.html
    """

    write_parameter("customer-profiles", "delete-profile-object-type")