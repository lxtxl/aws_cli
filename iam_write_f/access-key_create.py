#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-access-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-access-key.html
	list-access-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-access-keys.html
	update-access-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-access-key.html
    """

    write_parameter("iam", "create-access-key")