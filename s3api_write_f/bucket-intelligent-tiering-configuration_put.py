#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-bucket-intelligent-tiering-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-intelligent-tiering-configuration.html
	get-bucket-intelligent-tiering-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-intelligent-tiering-configuration.html
	list-bucket-intelligent-tiering-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-intelligent-tiering-configurations.html
    """

    write_parameter("s3api", "put-bucket-intelligent-tiering-configuration")