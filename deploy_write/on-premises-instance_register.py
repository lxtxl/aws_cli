#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-on-premises-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/deregister-on-premises-instance.html
	get-on-premises-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-on-premises-instance.html
	list-on-premises-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-on-premises-instances.html
    """

    write_parameter("deploy", "register-on-premises-instance")