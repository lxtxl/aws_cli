#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-sip-media-application.html
	get-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-sip-media-application.html
	list-sip-media-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-sip-media-applications.html
	update-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-sip-media-application.html
    """

    write_parameter("chime", "delete-sip-media-application")