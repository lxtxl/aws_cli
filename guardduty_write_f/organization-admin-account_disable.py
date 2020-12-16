#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	enable-organization-admin-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/enable-organization-admin-account.html
	list-organization-admin-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-organization-admin-accounts.html
    """

    write_parameter("guardduty", "disable-organization-admin-account")