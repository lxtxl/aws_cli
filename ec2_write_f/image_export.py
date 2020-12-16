#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	copy-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-image.html
	create-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-image.html
	deregister-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-image.html
	describe-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html
	import-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-image.html
	register-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html
    """

    write_parameter("ec2", "export-image")