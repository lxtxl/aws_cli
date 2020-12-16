#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-evaluation.html
	describe-evaluations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-evaluations.html
	get-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-evaluation.html
	update-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-evaluation.html
    """

    write_parameter("machinelearning", "delete-evaluation")