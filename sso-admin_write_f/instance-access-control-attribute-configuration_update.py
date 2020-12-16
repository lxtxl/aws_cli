#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-instance-access-control-attribute-configuration.html
	delete-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-instance-access-control-attribute-configuration.html
	describe-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-instance-access-control-attribute-configuration.html
    """

    write_parameter("sso-admin", "update-instance-access-control-attribute-configuration")