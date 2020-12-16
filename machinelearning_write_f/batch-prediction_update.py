#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-batch-prediction.html
	delete-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-batch-prediction.html
	describe-batch-predictions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-batch-predictions.html
	get-batch-prediction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-batch-prediction.html
    """

    write_parameter("machinelearning", "update-batch-prediction")