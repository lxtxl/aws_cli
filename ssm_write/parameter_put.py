#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html
	delete-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameters.html
	describe-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-parameters.html
	get-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html
	get-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters.html
    """

    write_parameter("ssm", "put-parameter")