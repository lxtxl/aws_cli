#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/create-app.html
	delete-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/delete-app.html
	get-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/get-app.html
	list-apps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/list-apps.html
	terminate-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/terminate-app.html
	update-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/update-app.html
    """

    write_parameter("sms", "launch-app")