#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-analysis.html
	delete-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-analysis.html
	describe-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-analysis.html
	update-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-analysis.html
    """

    write_parameter("quicksight", "restore-analysis")