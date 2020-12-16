#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/create-parallel-data.html
	delete-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/delete-parallel-data.html
	get-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-parallel-data.html
	list-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-parallel-data.html
    """

    write_parameter("translate", "update-parallel-data")