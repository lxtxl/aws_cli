#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-continuous-exports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-continuous-exports.html
	stop-continuous-export : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/stop-continuous-export.html
    """

    write_parameter("discovery", "start-continuous-export")