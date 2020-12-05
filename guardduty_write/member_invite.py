#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-members.html
	delete-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-members.html
	disassociate-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disassociate-members.html
	get-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-members.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-members.html
    """

    write_parameter("guardduty", "invite-members")