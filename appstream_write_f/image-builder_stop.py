#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-image-builder.html
	delete-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-image-builder.html
	describe-image-builders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-image-builders.html
	start-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/start-image-builder.html
    """

    write_parameter("appstream", "stop-image-builder")