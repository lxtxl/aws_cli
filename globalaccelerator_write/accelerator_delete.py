#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-accelerator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-accelerator.html
	describe-accelerator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-accelerator.html
	list-accelerators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-accelerators.html
	update-accelerator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-accelerator.html
    """

    write_parameter("globalaccelerator", "delete-accelerator")