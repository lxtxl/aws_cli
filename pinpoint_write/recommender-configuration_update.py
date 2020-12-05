#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-recommender-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-recommender-configuration.html
	delete-recommender-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-recommender-configuration.html
	get-recommender-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-recommender-configuration.html
	get-recommender-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-recommender-configurations.html
    """

    write_parameter("pinpoint", "update-recommender-configuration")