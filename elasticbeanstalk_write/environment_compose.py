#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-environment.html
	describe-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-environments.html
	rebuild-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/rebuild-environment.html
	terminate-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/terminate-environment.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-environment.html
    """

    write_parameter("elasticbeanstalk", "compose-environments")