#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-index.html
	delete-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-index.html
	describe-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-index.html
    """

    write_parameter("kendra", "update-index")