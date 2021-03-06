#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/create-profile.html
	delete-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-profile.html
	search-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/search-profiles.html
    """

    write_parameter("customer-profiles", "update-profile")