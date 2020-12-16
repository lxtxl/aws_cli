#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-input.html
	describe-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-input.html
	list-inputs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-inputs.html
	update-input : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-input.html
    """

    write_parameter("medialive", "delete-input")