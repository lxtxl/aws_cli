#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	disassociate-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/disassociate-team-member.html
	list-team-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-team-members.html
	update-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-team-member.html
    """

    write_parameter("codestar", "associate-team-member")