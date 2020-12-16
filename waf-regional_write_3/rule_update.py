#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-rule.html
if __name__ == '__main__':
    """
	create-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-rule.html
	delete-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-rule.html
	get-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-rule.html
	list-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-rules.html
    """

    parameter_display_string = """
    # rule-id : The RuleId of the Rule that you want to update. RuleId is returned by CreateRule and by  ListRules .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    # updates : An array of RuleUpdate objects that you want to insert into or delete from a  Rule . For more information, see the applicable data types:

RuleUpdate : Contains Action and Predicate
Predicate : Contains DataId , Negated , and Type
FieldToMatch : Contains Data and Type

(structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies a Predicate (such as an IPSet ) and indicates whether you want to add it to a Rule or delete it from a Rule .
Action -> (string)

Specify INSERT to add a Predicate to a Rule . Use DELETE to remove a Predicate from a Rule .

Predicate -> (structure)

The ID of the Predicate (such as an IPSet ) that you want to add to a Rule .
Negated -> (boolean)

Set Negated to False if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow or block requests based on that IP address.
Set Negated to True if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an IPSet includes the IP address 192.0.2.44 , AWS WAF will allow, block, or count requests based on all IP addresses except 192.0.2.44 .

Type -> (string)

The type of predicate in a Rule , such as ByteMatch or IPSet .

DataId -> (string)

A unique identifier for a predicate in a Rule , such as ByteMatchSetId or IPSetId . The ID is returned by the corresponding Create or List command.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf-regional", "update-rule", "rule-id", "change-token", "updates", add_option_dict)
