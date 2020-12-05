#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	allocate-public-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-public-virtual-interface.html
	create-public-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-public-virtual-interface.html
    """

    write_parameter("directconnect", "confirm-public-virtual-interface")