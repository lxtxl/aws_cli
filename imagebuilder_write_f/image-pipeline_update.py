#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-pipeline.html
	delete-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image-pipeline.html
	get-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-pipeline.html
	list-image-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-pipelines.html
    """

    write_parameter("imagebuilder", "update-image-pipeline")