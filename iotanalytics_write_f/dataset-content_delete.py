#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-dataset-content : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-dataset-content.html
	get-dataset-content : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/get-dataset-content.html
	list-dataset-contents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-dataset-contents.html
    """

    write_parameter("iotanalytics", "delete-dataset-content")