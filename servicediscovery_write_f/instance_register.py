#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/deregister-instance.html
	discover-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html
	get-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html
	list-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html
    """

    write_parameter("servicediscovery", "register-instance")