#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-type.html
	delete-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-type.html
	describe-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-type.html
	list-thing-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-types.html
    """

    write_parameter("iot", "deprecate-thing-type")