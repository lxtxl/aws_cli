#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-ip-set.html
	delete-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-ip-set.html
	get-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-ip-set.html
	list-ip-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-ip-sets.html
    """

    write_parameter("guardduty", "update-ip-set")