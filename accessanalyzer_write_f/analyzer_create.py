#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-analyzer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-analyzer.html
	get-analyzer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-analyzer.html
	list-analyzers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-analyzers.html
    """

    write_parameter("accessanalyzer", "create-analyzer")