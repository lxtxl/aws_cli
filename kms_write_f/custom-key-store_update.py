#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	connect-custom-key-store : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/connect-custom-key-store.html
	create-custom-key-store : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-custom-key-store.html
	delete-custom-key-store : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-custom-key-store.html
	describe-custom-key-stores : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-custom-key-stores.html
	disconnect-custom-key-store : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disconnect-custom-key-store.html
    """

    write_parameter("kms", "update-custom-key-store")