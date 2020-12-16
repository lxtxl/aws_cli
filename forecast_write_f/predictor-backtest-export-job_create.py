#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-predictor-backtest-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-predictor-backtest-export-job.html
	describe-predictor-backtest-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-predictor-backtest-export-job.html
	list-predictor-backtest-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-predictor-backtest-export-jobs.html
    """

    write_parameter("forecast", "create-predictor-backtest-export-job")