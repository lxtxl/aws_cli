#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-remediation-configurations.html
if __name__ == '__main__':
    """
	delete-remediation-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-remediation-configuration.html
	describe-remediation-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-remediation-configurations.html
    """

    parameter_display_string = """
    # remediation-configurations : A list of remediation configuration objects.
(structure)

An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.
ConfigRuleName -> (string)

The name of the AWS Config rule.

TargetType -> (string)

The type of the target. Target executes remediation. For example, SSM document.

TargetId -> (string)

Target ID is the name of the public document.

TargetVersion -> (string)

Version of the target. For example, version of the SSM document.

Note
If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.


Parameters -> (map)

An object of the RemediationParameterValue.
key -> (string)
value -> (structure)

The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.
ResourceValue -> (structure)

The value is dynamic and changes at run-time.
Value -> (string)

The value is a resource ID.


StaticValue -> (structure)

The value is static and does not change at run-time.
Values -> (list)

A list of values. For example, the ARN of the assumed role.
(string)




ResourceType -> (string)

The type of a resource.

Automatic -> (boolean)

The remediation is triggered automatically.

ExecutionControls -> (structure)

An ExecutionControls object.
SsmControls -> (structure)

A SsmControls object.
ConcurrentExecutionRatePercentage -> (integer)

The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.

ErrorPercentage -> (integer)

The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.



MaximumAutomaticAttempts -> (integer)

The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.
For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.

RetryAttemptSeconds -> (long)

Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a number, the default is 60 seconds.
For example, if you specify RetryAttemptsSeconds as 50 seconds and MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an exception.

Arn -> (string)

Amazon Resource Name (ARN) of remediation configuration.

CreatedByService -> (string)

Name of the service that owns the service linked rule, if applicable.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "put-remediation-configurations", "remediation-configurations", add_option_dict)





