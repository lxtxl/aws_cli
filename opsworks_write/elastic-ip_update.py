#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-elastic-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/associate-elastic-ip.html
	deregister-elastic-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-elastic-ip.html
	describe-elastic-ips : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-elastic-ips.html
	disassociate-elastic-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/disassociate-elastic-ip.html
	register-elastic-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-elastic-ip.html
    """

    write_parameter("opsworks", "update-elastic-ip")