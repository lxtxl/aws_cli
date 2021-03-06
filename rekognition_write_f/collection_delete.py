#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-collection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-collection.html
	describe-collection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-collection.html
	list-collections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-collections.html
    """

    write_parameter("rekognition", "delete-collection")