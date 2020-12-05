#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image.html
	get-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image.html
	list-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html
    """

    write_parameter("imagebuilder", "create-image")