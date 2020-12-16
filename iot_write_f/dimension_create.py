#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-dimension.html
	describe-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-dimension.html
	list-dimensions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-dimensions.html
	update-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dimension.html
    """

    write_parameter("iot", "create-dimension")