#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # alarm-name : The name for the composite alarm. This name must be unique within the Region.
    # alarm-rule : An expression that specifies which other alarms are to be evaluated to determine this composite alarmâs state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.
You can use either alarm names or ARNs to reference the other alarms that are to be evaluated.
Functions can include the following:

ALARM("*alarm-name* or *alarm-ARN* ") is TRUE if the named alarm is in ALARM state.
OK("*alarm-name* or *alarm-ARN* ") is TRUE if the named alarm is in OK state.
INSUFFICIENT_DATA("*alarm-name* or *alarm-ARN* ") is TRUE if the named alarm is in INSUFFICIENT_DATA state.
TRUE always evaluates to TRUE.
FALSE always evaluates to FALSE.

TRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions.
Alarm names specified in AlarmRule can be surrounded with double-quotes (â), but do not have to be.
The following are some examples of AlarmRule :

ALARM(CPUUtilizationTooHigh) AND ALARM(DiskReadOpsTooHigh) specifies that the composite alarm goes into ALARM state only if both CPUUtilizationTooHigh and DiskReadOpsTooHigh alarms are in ALARM state.
ALARM(CPUUtilizationTooHigh) AND NOT ALARM(DeploymentInProgress) specifies that the alarm goes to ALARM state if CPUUtilizationTooHigh is in ALARM state and DeploymentInProgress is not in ALARM state. This example reduces alarm noise during a known deployment window.
(ALARM(CPUUtilizationTooHigh) OR ALARM(DiskReadOpsTooHigh)) AND OK(NetworkOutTooHigh) goes into ALARM state if CPUUtilizationTooHigh OR DiskReadOpsTooHigh is in ALARM state, and if NetworkOutTooHigh is in OK state. This provides another example of using a composite alarm to prevent noise. This rule ensures that you are not notified with an alarm action on high CPU or disk usage if a known network problem is also occurring.

The AlarmRule can specify as many as 100 âchildrenâ alarms. The AlarmRule expression can have as many as 500 elements. Elements are child alarms, TRUE or FALSE statements, and parentheses.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudwatch", "put-composite-alarm", "alarm-name", "alarm-rule", add_option_dict)
