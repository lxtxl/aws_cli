#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-upload.html
	get-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-upload.html
	list-uploads : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-uploads.html
	update-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-upload.html
    """

    write_parameter("devicefarm", "create-upload")