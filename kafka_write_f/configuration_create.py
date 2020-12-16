#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/delete-configuration.html
	describe-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-configuration.html
	list-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-configurations.html
	update-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-configuration.html
    """

    write_parameter("kafka", "create-configuration")