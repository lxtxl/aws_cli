#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-platform-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-platform-version.html
	describe-platform-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-platform-version.html
	list-platform-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-platform-versions.html
    """

    write_parameter("elasticbeanstalk", "create-platform-version")