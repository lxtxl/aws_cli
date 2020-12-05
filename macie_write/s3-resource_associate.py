#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	disassociate-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/disassociate-s3-resources.html
	list-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/list-s3-resources.html
	update-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/update-s3-resources.html
    """

    write_parameter("macie", "associate-s3-resources")