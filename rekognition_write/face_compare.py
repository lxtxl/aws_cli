#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-faces.html
	detect-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-faces.html
	index-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index-faces.html
	list-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-faces.html
	search-faces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces.html
    """

    write_parameter("rekognition", "compare-faces")