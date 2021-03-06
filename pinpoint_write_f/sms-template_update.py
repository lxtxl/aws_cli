#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-sms-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-sms-template.html
	delete-sms-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-sms-template.html
	get-sms-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-sms-template.html
    """

    write_parameter("pinpoint", "update-sms-template")