#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-configuration-recorders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorders.html
	put-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-recorder.html
	start-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-configuration-recorder.html
	stop-configuration-recorder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/stop-configuration-recorder.html
    """

    write_parameter("configservice", "delete-configuration-recorder")