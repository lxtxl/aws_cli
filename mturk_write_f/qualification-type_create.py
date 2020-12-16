#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/delete-qualification-type.html
	get-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-qualification-type.html
	list-qualification-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-qualification-types.html
	update-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/update-qualification-type.html
    """

    write_parameter("mturk", "create-qualification-type")