#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-member.html
	delete-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-member.html
	get-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-member.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-members.html
    """

    write_parameter("macie2", "disassociate-member")