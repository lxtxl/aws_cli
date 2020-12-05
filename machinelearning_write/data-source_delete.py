#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-data-sources.html
	get-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-data-source.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-data-source.html
    """

    write_parameter("machinelearning", "delete-data-source")