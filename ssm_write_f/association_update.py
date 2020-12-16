#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association.html
	delete-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-association.html
	describe-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association.html
	list-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-associations.html
    """

    write_parameter("ssm", "update-association")