#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	accept-invitation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/accept-invitation.html
	decline-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/decline-invitations.html
	list-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-invitations.html
    """

    write_parameter("securityhub", "delete-invitations")