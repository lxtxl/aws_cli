#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule-group.html
if __name__ == '__main__':
    """
	create-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule-group.html
	delete-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-rule-group.html
	get-rule-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rule-group.html
	list-rule-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rule-groups.html
    """

    parameter_display_string = """
    # rule-group-id : The RuleGroupId of the  RuleGroup that you want to update. RuleGroupId is returned by  CreateRuleGroup and by  ListRuleGroups .
    # updates : An array of RuleGroupUpdate objects that you want to insert into or delete from a  RuleGroup .
You can only insert REGULAR rules into a rule group.

ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .

(structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies an ActivatedRule and indicates whether you want to add it to a RuleGroup or delete it from a RuleGroup .
Action -> (string)

Specify INSERT to add an ActivatedRule to a RuleGroup . Use DELETE to remove an ActivatedRule from a RuleGroup .

ActivatedRule -> (structure)

The ActivatedRule object specifies a Rule that you want to insert or delete, the priority of the Rule in the WebACL , and the action that you want AWS WAF to take when a web request matches the Rule (ALLOW , BLOCK , or COUNT ).
Priority -> (integer)

Specifies the order in which the Rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before Rules with a higher value. The value must be a unique integer. If you add multiple Rules to a WebACL , the values donât need to be consecutive.

RuleId -> (string)

The RuleId for a Rule . You use RuleId to get more information about a Rule (see  GetRule ), update a Rule (see  UpdateRule ), insert a Rule into a WebACL or delete a one from a WebACL (see  UpdateWebACL ), or delete a Rule from AWS WAF (see  DeleteRule ).

RuleId is returned by  CreateRule and by  ListRules .


Action -> (structure)

Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the Rule . Valid values for Action include the following:

ALLOW : CloudFront responds with the requested object.
BLOCK : CloudFront responds with an HTTP 403 (Forbidden) status code.
COUNT : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.


ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case, you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .

Type -> (string)

Specifies how you want AWS WAF to respond to requests that match the settings in a Rule . Valid settings include the following:

ALLOW : AWS WAF allows requests
BLOCK : AWS WAF blocks requests
COUNT : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You canât specify COUNT for the default action for a WebACL .



OverrideAction -> (structure)

Use the OverrideAction to test your RuleGroup .
Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup will block a request if any individual rule in the RuleGroup matches the request and is configured to block that request. However if you first want to test the RuleGroup , set the OverrideAction to Count . The RuleGroup will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests .

ActivatedRule|OverrideAction applies only when updating or adding a RuleGroup to a WebACL . In this case you do not use ActivatedRule|Action . For all other update requests, ActivatedRule|Action is used instead of ActivatedRule|OverrideAction .

Type -> (string)

COUNT overrides the action specified by the individual rule within a RuleGroup . If set to NONE , the ruleâs action will take place.


Type -> (string)

The rule type, either REGULAR , as defined by  Rule , RATE_BASED , as defined by  RateBasedRule , or GROUP , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.

ExcludedRules -> (list)

An array of rules to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup .
Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.
Specifying ExcludedRules does not remove those rules from the rule group. Rather, it changes the action for the rules to COUNT . Therefore, requests that match an ExcludedRule are counted but not blocked. The RuleGroup owner will receive COUNT metrics for each ExcludedRule .
If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:

Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see Logging Web ACL Traffic Information .
Submit an  UpdateWebACL request that has two actions:

The first action deletes the existing rule group from the web ACL. That is, in the  UpdateWebACL request, the first Updates:Action should be DELETE and Updates:ActivatedRule:RuleId should be the rule group that contains the rules that you want to exclude.
The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second Updates:Action should be INSERT , Updates:ActivatedRule:RuleId should be the rule group that you just removed, and ExcludedRules should contain the rules that you want to exclude.



(structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


The rule to exclude from a rule group. This is applicable only when the ActivatedRule refers to a RuleGroup . The rule must belong to the RuleGroup that is specified by the ActivatedRule .
RuleId -> (string)

The unique identifier for the rule to exclude from the rule group.
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf", "update-rule-group", "rule-group-id", "updates", "change-token", add_option_dict)
