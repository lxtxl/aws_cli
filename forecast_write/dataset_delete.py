#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-dataset.html
	describe-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset.html
	list-datasets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-datasets.html
    """

    write_parameter("forecast", "delete-dataset")