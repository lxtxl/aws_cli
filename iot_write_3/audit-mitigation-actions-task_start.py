#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/start-audit-mitigation-actions-task.html
if __name__ == '__main__':
    """
	cancel-audit-mitigation-actions-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-audit-mitigation-actions-task.html
	describe-audit-mitigation-actions-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-mitigation-actions-task.html
	list-audit-mitigation-actions-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-mitigation-actions-tasks.html
    """

    parameter_display_string = """
    # task-id : A unique identifier for the task. You can use this identifier to check the status of the task or to cancel it.
    # target : The group or principal for which the policies will be listed. Valid principals are CertificateArn (arn:aws:iot:region :accountId :cert/certificateId ), thingGroupArn (arn:aws:iot:region :accountId :thinggroup/groupName ) and CognitoId (region :id ).
    # audit-check-to-actions-mapping : For an audit check, specifies which mitigation actions to apply. Those actions must be defined in your AWS account.
key -> (string)

An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)

value -> (list)

(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot", "start-audit-mitigation-actions-task", "task-id", "target", "audit-check-to-actions-mapping", add_option_dict)
