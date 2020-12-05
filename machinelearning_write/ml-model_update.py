#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-ml-model.html
	delete-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-ml-model.html
	describe-ml-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-ml-models.html
	get-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-ml-model.html
    """

    write_parameter("machinelearning", "update-ml-model")