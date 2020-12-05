#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing.html
	delete-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing.html
	describe-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing.html
	list-things : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-things.html
	update-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing.html
    """

    write_parameter("iot", "register-thing")