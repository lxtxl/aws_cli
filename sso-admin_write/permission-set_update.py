#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-permission-set.html
	delete-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-permission-set.html
	describe-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-permission-set.html
	list-permission-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-permission-sets.html
	provision-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/provision-permission-set.html
    """

    write_parameter("sso-admin", "update-permission-set")