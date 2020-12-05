#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-account.html
	delete-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-account.html
	get-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-account.html
	list-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-accounts.html
    """

    write_parameter("chime", "update-account")