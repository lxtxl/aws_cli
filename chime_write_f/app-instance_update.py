#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-app-instance.html
	delete-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance.html
	describe-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-app-instance.html
	list-app-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-app-instances.html
    """

    write_parameter("chime", "update-app-instance")