#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	grant-flow-entitlements : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/grant-flow-entitlements.html
	update-flow-entitlement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-entitlement.html
    """

    write_parameter("mediaconnect", "revoke-flow-entitlement")