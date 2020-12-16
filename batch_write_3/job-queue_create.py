#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html
if __name__ == '__main__':
    """
	delete-job-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-job-queue.html
	describe-job-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-queues.html
	update-job-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-job-queue.html
    """

    parameter_display_string = """
    # job-queue-name : The name of the job queue.
    # priority : The priority of the job queue. Job queues with a higher priority (or a higher integer value for the priority parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of 10 is given scheduling preference over a job queue with a priority value of 1 .
    # compute-environment-order : The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment should run a specific job. Compute environments must be in the VALID state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 (EC2 or SPOT ) or Fargate (FARGATE or FARGATE_SPOT ); EC2 and Fargate compute environments canât be mixed.
(structure)

The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.
order -> (integer)

The order of the compute environment. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.

computeEnvironment -> (string)

The Amazon Resource Name (ARN) of the compute environment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("batch", "create-job-queue", "job-queue-name", "priority", "compute-environment-order", add_option_dict)
