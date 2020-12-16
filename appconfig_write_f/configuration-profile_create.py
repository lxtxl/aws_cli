#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-configuration-profile.html
	get-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-configuration-profile.html
	list-configuration-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-configuration-profiles.html
	update-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-configuration-profile.html
    """

    write_parameter("appconfig", "create-configuration-profile")