#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-email-template.html
	get-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-email-template.html
	update-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-email-template.html
    """

    write_parameter("pinpoint", "create-email-template")