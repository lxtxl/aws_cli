#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	disassociate-member-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/disassociate-member-account.html
	list-member-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/list-member-accounts.html
    """

    write_parameter("macie", "associate-member-account")