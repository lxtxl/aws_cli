#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-configuration-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-configuration-template.html
	delete-configuration-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/delete-configuration-template.html
    """

    write_parameter("elasticbeanstalk", "update-configuration-template")