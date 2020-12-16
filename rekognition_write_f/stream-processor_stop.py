#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-stream-processor.html
	delete-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-stream-processor.html
	describe-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-stream-processor.html
	list-stream-processors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-stream-processors.html
	start-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-stream-processor.html
    """

    write_parameter("rekognition", "stop-stream-processor")