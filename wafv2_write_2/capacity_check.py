#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/check-capacity.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # scope : Specifies whether this is for an AWS CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an API Gateway REST API, or an AppSync GraphQL API.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

CLI - Specify the Region when you use the CloudFront scope: --scope=CLOUDFRONT --region=us-east-1 .
API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

CLOUDFRONT
REGIONAL
    # rules : An array of  Rule that youâre configuring to use in a rule group or web ACL.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

A single rule, which you can use in a  WebACL or  RuleGroup to identify web requests that you want to allow, block, or count. Each rule includes one top-level  Statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.
Name -> (string)

The name of the rule. You canât change the name of a Rule after you create it.

Priority -> (integer)

If you define more than one Rule in a WebACL , AWS WAF evaluates each request against the Rules in order based on the value of Priority . AWS WAF processes rules with lower priority first. The priorities donât need to be consecutive, but they must all be different.

Statement -> (structure)

The AWS WAF processing statement for the rule, for example  ByteMatchStatement or  SizeConstraintStatement .
ByteMatchStatement -> (structure)

A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.
SearchString -> (blob)

A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in  FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the component that you specify for inspection in FieldToMatch :

Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .

If SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If youâre using the AWS WAF API

Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .

If youâre using the AWS CLI or one of the AWS SDKs

The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.



PositionalConstraint -> (string)

The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:

CONTAINS

The specified part of the web request must include the value of SearchString , but the location doesnât matter.

CONTAINS_WORD

The specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:

SearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .
SearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .


EXACTLY

The value of the specified part of the web request must exactly match the value of SearchString .

STARTS_WITH

The value of SearchString must appear at the beginning of the specified part of the web request.

ENDS_WITH

The value of SearchString must appear at the end of the specified part of the web request.


SqliMatchStatement -> (structure)

Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




XssMatchStatement -> (structure)

A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




SizeConstraintStatement -> (structure)

A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.
If you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.
If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


ComparisonOperator -> (string)

The operator to use to compare the request part to the size setting.

Size -> (long)

The size, in byte, to compare to the request part, after any transformations.

TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




GeoMatchStatement -> (structure)

A rule statement used to identify web requests based on country of origin.
CountryCodes -> (list)

An array of two-character country codes, for example, [ "US", "CN" ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.
(string)

ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




RuleGroupReferenceStatement -> (structure)

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
ARN -> (string)

The Amazon Resource Name (ARN) of the entity.

ExcludedRules -> (list)

The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.




IPSetReferenceStatement -> (structure)

A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an  IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see  CreateIPSet .
Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  IPSet that this statement references.

IPSetForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.


Position -> (string)

The position in the header to search for the IP address. The header can contain IP addresses of the original client and also of proxies. For example, the header value could be 10.1.1.1, 127.0.0.0, 10.10.10.10 where the first IP address identifies the original client and the rest identify proxies that the request went through.
The options for this setting are the following:

FIRST - Inspect the first IP address in the list of IP addresses in the header. This is usually the clientâs original IP.
LAST - Inspect the last IP address in the list of IP addresses in the header.
ANY - Inspect all IP addresses in the header for a match. If the header contains more than 10 IP addresses, AWS WAF inspects the last 10.




RegexPatternSetReferenceStatement -> (structure)

A rule statement used to search web request components for matches with regular expressions. To use this, create a  RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see  CreateRegexPatternSet .
Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  RegexPatternSet that this statement references.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




RateBasedStatement -> (structure)

A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.
When the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.
You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:

An IP match statement with an IP set that specified the address 192.0.2.44.
A string match statement that searches in the User-Agent header for the string BadBot.

In this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.
You cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
Limit -> (long)

The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopeDownStatement , this limit is applied only to the requests that match the statement.

AggregateKeyType -> (string)

Setting that indicates how to aggregate the request counts. The options are the following:

IP - Aggregate the request counts on the IP address from the web request origin.
FORWARDED_IP - Aggregate the request counts on the first IP address in an HTTP header. If you use this, configure the ForwardedIPConfig , to specify the header to use.


ScopeDownStatement -> (structure)

An optional nested statement that narrows the scope of the rate-based statement to matching web requests. This can be any nestable statement, and you can nest statements at any level below this scope-down statement.
ByteMatchStatement -> (structure)

A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.
SearchString -> (blob)

A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in  FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the component that you specify for inspection in FieldToMatch :

Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .

If SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If youâre using the AWS WAF API

Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .

If youâre using the AWS CLI or one of the AWS SDKs

The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.



PositionalConstraint -> (string)

The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:

CONTAINS

The specified part of the web request must include the value of SearchString , but the location doesnât matter.

CONTAINS_WORD

The specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:

SearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .
SearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .


EXACTLY

The value of the specified part of the web request must exactly match the value of SearchString .

STARTS_WITH

The value of SearchString must appear at the beginning of the specified part of the web request.

ENDS_WITH

The value of SearchString must appear at the end of the specified part of the web request.


SqliMatchStatement -> (structure)

Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




XssMatchStatement -> (structure)

A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




SizeConstraintStatement -> (structure)

A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.
If you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.
If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


ComparisonOperator -> (string)

The operator to use to compare the request part to the size setting.

Size -> (long)

The size, in byte, to compare to the request part, after any transformations.

TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




GeoMatchStatement -> (structure)

A rule statement used to identify web requests based on country of origin.
CountryCodes -> (list)

An array of two-character country codes, for example, [ "US", "CN" ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.
(string)

ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




RuleGroupReferenceStatement -> (structure)

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
ARN -> (string)

The Amazon Resource Name (ARN) of the entity.

ExcludedRules -> (list)

The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.




IPSetReferenceStatement -> (structure)

A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an  IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see  CreateIPSet .
Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  IPSet that this statement references.

IPSetForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.


Position -> (string)

The position in the header to search for the IP address. The header can contain IP addresses of the original client and also of proxies. For example, the header value could be 10.1.1.1, 127.0.0.0, 10.10.10.10 where the first IP address identifies the original client and the rest identify proxies that the request went through.
The options for this setting are the following:

FIRST - Inspect the first IP address in the list of IP addresses in the header. This is usually the clientâs original IP.
LAST - Inspect the last IP address in the list of IP addresses in the header.
ANY - Inspect all IP addresses in the header for a match. If the header contains more than 10 IP addresses, AWS WAF inspects the last 10.




RegexPatternSetReferenceStatement -> (structure)

A rule statement used to search web request components for matches with regular expressions. To use this, create a  RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see  CreateRegexPatternSet .
Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  RegexPatternSet that this statement references.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




RateBasedStatement -> (structure)

A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.
When the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.
You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:

An IP match statement with an IP set that specified the address 192.0.2.44.
A string match statement that searches in the User-Agent header for the string BadBot.

In this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.
You cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
Limit -> (long)

The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopeDownStatement , this limit is applied only to the requests that match the statement.

AggregateKeyType -> (string)

Setting that indicates how to aggregate the request counts. The options are the following:

IP - Aggregate the request counts on the IP address from the web request origin.
FORWARDED_IP - Aggregate the request counts on the first IP address in an HTTP header. If you use this, configure the ForwardedIPConfig , to specify the header to use.


( â¦ recursive â¦ )ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

This is required if AggregateKeyType is set to FORWARDED_IP .
HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




AndStatement -> (structure)

A logical rule statement used to combine other rule statements with AND logic. You provide more than one  Statement within the AndStatement .
Statements -> (list)

The statements to combine with AND logic. You can use any statements that can be nested.
( â¦ recursive â¦ )


OrStatement -> (structure)

A logical rule statement used to combine other rule statements with OR logic. You provide more than one  Statement within the OrStatement .
Statements -> (list)

The statements to combine with OR logic. You can use any statements that can be nested.
( â¦ recursive â¦ )


NotStatement -> (structure)

A logical rule statement used to negate the results of another rule statement. You provide one  Statement within the NotStatement .
( â¦ recursive â¦ )

ManagedRuleGroupStatement -> (structure)

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You canât nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
VendorName -> (string)

The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name -> (string)

The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules -> (list)

The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.





ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

This is required if AggregateKeyType is set to FORWARDED_IP .
HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




AndStatement -> (structure)

A logical rule statement used to combine other rule statements with AND logic. You provide more than one  Statement within the AndStatement .
Statements -> (list)

The statements to combine with AND logic. You can use any statements that can be nested.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The processing guidance for a  Rule , used by AWS WAF to determine whether a web request matches the rule.
ByteMatchStatement -> (structure)

A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.
SearchString -> (blob)

A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in  FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the component that you specify for inspection in FieldToMatch :

Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .

If SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If youâre using the AWS WAF API

Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .

If youâre using the AWS CLI or one of the AWS SDKs

The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.



PositionalConstraint -> (string)

The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:

CONTAINS

The specified part of the web request must include the value of SearchString , but the location doesnât matter.

CONTAINS_WORD

The specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:

SearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .
SearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .


EXACTLY

The value of the specified part of the web request must exactly match the value of SearchString .

STARTS_WITH

The value of SearchString must appear at the beginning of the specified part of the web request.

ENDS_WITH

The value of SearchString must appear at the end of the specified part of the web request.


SqliMatchStatement -> (structure)

Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




XssMatchStatement -> (structure)

A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




SizeConstraintStatement -> (structure)

A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.
If you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.
If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


ComparisonOperator -> (string)

The operator to use to compare the request part to the size setting.

Size -> (long)

The size, in byte, to compare to the request part, after any transformations.

TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




GeoMatchStatement -> (structure)

A rule statement used to identify web requests based on country of origin.
CountryCodes -> (list)

An array of two-character country codes, for example, [ "US", "CN" ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.
(string)

ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




RuleGroupReferenceStatement -> (structure)

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
ARN -> (string)

The Amazon Resource Name (ARN) of the entity.

ExcludedRules -> (list)

The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.




IPSetReferenceStatement -> (structure)

A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an  IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see  CreateIPSet .
Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  IPSet that this statement references.

IPSetForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.


Position -> (string)

The position in the header to search for the IP address. The header can contain IP addresses of the original client and also of proxies. For example, the header value could be 10.1.1.1, 127.0.0.0, 10.10.10.10 where the first IP address identifies the original client and the rest identify proxies that the request went through.
The options for this setting are the following:

FIRST - Inspect the first IP address in the list of IP addresses in the header. This is usually the clientâs original IP.
LAST - Inspect the last IP address in the list of IP addresses in the header.
ANY - Inspect all IP addresses in the header for a match. If the header contains more than 10 IP addresses, AWS WAF inspects the last 10.




RegexPatternSetReferenceStatement -> (structure)

A rule statement used to search web request components for matches with regular expressions. To use this, create a  RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see  CreateRegexPatternSet .
Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  RegexPatternSet that this statement references.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




RateBasedStatement -> (structure)

A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.
When the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.
You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:

An IP match statement with an IP set that specified the address 192.0.2.44.
A string match statement that searches in the User-Agent header for the string BadBot.

In this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.
You cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
Limit -> (long)

The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopeDownStatement , this limit is applied only to the requests that match the statement.

AggregateKeyType -> (string)

Setting that indicates how to aggregate the request counts. The options are the following:

IP - Aggregate the request counts on the IP address from the web request origin.
FORWARDED_IP - Aggregate the request counts on the first IP address in an HTTP header. If you use this, configure the ForwardedIPConfig , to specify the header to use.


( â¦ recursive â¦ )ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

This is required if AggregateKeyType is set to FORWARDED_IP .
HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




AndStatement -> (structure)

A logical rule statement used to combine other rule statements with AND logic. You provide more than one  Statement within the AndStatement .
Statements -> (list)

The statements to combine with AND logic. You can use any statements that can be nested.
( â¦ recursive â¦ )


OrStatement -> (structure)

A logical rule statement used to combine other rule statements with OR logic. You provide more than one  Statement within the OrStatement .
Statements -> (list)

The statements to combine with OR logic. You can use any statements that can be nested.
( â¦ recursive â¦ )


NotStatement -> (structure)

A logical rule statement used to negate the results of another rule statement. You provide one  Statement within the NotStatement .
( â¦ recursive â¦ )

ManagedRuleGroupStatement -> (structure)

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You canât nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
VendorName -> (string)

The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name -> (string)

The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules -> (list)

The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.







OrStatement -> (structure)

A logical rule statement used to combine other rule statements with OR logic. You provide more than one  Statement within the OrStatement .
Statements -> (list)

The statements to combine with OR logic. You can use any statements that can be nested.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

The processing guidance for a  Rule , used by AWS WAF to determine whether a web request matches the rule.
ByteMatchStatement -> (structure)

A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.
SearchString -> (blob)

A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in  FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the component that you specify for inspection in FieldToMatch :

Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .

If SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If youâre using the AWS WAF API

Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .

If youâre using the AWS CLI or one of the AWS SDKs

The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.



PositionalConstraint -> (string)

The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:

CONTAINS

The specified part of the web request must include the value of SearchString , but the location doesnât matter.

CONTAINS_WORD

The specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:

SearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .
SearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .


EXACTLY

The value of the specified part of the web request must exactly match the value of SearchString .

STARTS_WITH

The value of SearchString must appear at the beginning of the specified part of the web request.

ENDS_WITH

The value of SearchString must appear at the end of the specified part of the web request.


SqliMatchStatement -> (structure)

Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




XssMatchStatement -> (structure)

A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




SizeConstraintStatement -> (structure)

A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.
If you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.
If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


ComparisonOperator -> (string)

The operator to use to compare the request part to the size setting.

Size -> (long)

The size, in byte, to compare to the request part, after any transformations.

TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




GeoMatchStatement -> (structure)

A rule statement used to identify web requests based on country of origin.
CountryCodes -> (list)

An array of two-character country codes, for example, [ "US", "CN" ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.
(string)

ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




RuleGroupReferenceStatement -> (structure)

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
ARN -> (string)

The Amazon Resource Name (ARN) of the entity.

ExcludedRules -> (list)

The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.




IPSetReferenceStatement -> (structure)

A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an  IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see  CreateIPSet .
Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  IPSet that this statement references.

IPSetForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.


Position -> (string)

The position in the header to search for the IP address. The header can contain IP addresses of the original client and also of proxies. For example, the header value could be 10.1.1.1, 127.0.0.0, 10.10.10.10 where the first IP address identifies the original client and the rest identify proxies that the request went through.
The options for this setting are the following:

FIRST - Inspect the first IP address in the list of IP addresses in the header. This is usually the clientâs original IP.
LAST - Inspect the last IP address in the list of IP addresses in the header.
ANY - Inspect all IP addresses in the header for a match. If the header contains more than 10 IP addresses, AWS WAF inspects the last 10.




RegexPatternSetReferenceStatement -> (structure)

A rule statement used to search web request components for matches with regular expressions. To use this, create a  RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see  CreateRegexPatternSet .
Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  RegexPatternSet that this statement references.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




RateBasedStatement -> (structure)

A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.
When the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.
You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:

An IP match statement with an IP set that specified the address 192.0.2.44.
A string match statement that searches in the User-Agent header for the string BadBot.

In this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.
You cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
Limit -> (long)

The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopeDownStatement , this limit is applied only to the requests that match the statement.

AggregateKeyType -> (string)

Setting that indicates how to aggregate the request counts. The options are the following:

IP - Aggregate the request counts on the IP address from the web request origin.
FORWARDED_IP - Aggregate the request counts on the first IP address in an HTTP header. If you use this, configure the ForwardedIPConfig , to specify the header to use.


( â¦ recursive â¦ )ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

This is required if AggregateKeyType is set to FORWARDED_IP .
HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




AndStatement -> (structure)

A logical rule statement used to combine other rule statements with AND logic. You provide more than one  Statement within the AndStatement .
Statements -> (list)

The statements to combine with AND logic. You can use any statements that can be nested.
( â¦ recursive â¦ )


OrStatement -> (structure)

A logical rule statement used to combine other rule statements with OR logic. You provide more than one  Statement within the OrStatement .
Statements -> (list)

The statements to combine with OR logic. You can use any statements that can be nested.
( â¦ recursive â¦ )


NotStatement -> (structure)

A logical rule statement used to negate the results of another rule statement. You provide one  Statement within the NotStatement .
( â¦ recursive â¦ )

ManagedRuleGroupStatement -> (structure)

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You canât nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
VendorName -> (string)

The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name -> (string)

The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules -> (list)

The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.







NotStatement -> (structure)

A logical rule statement used to negate the results of another rule statement. You provide one  Statement within the NotStatement .
Statement -> (structure)

The statement to negate. You can use any statement that can be nested.
ByteMatchStatement -> (structure)

A rule statement that defines a string match search for AWS WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want AWS WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the AWS WAF console and the developer guide, this is refered to as a string match statement.
SearchString -> (blob)

A string value that you want AWS WAF to search for. AWS WAF searches only in the part of web requests that you designate for inspection in  FieldToMatch . The maximum length of the value is 50 bytes.
Valid values depend on the component that you specify for inspection in FieldToMatch :

Method : The HTTP method that you want AWS WAF to search for. This indicates the type of operation specified in the request.
UriPath : The value that you want AWS WAF to search for in the URI path, for example, /images/daily-ad.jpg .

If SearchString includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

If youâre using the AWS WAF API

Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.
For example, suppose the value of Type is HEADER and the value of Data is User-Agent . If you want to search the User-Agent header for the value BadBot , you base64-encode BadBot using MIME base64-encoding and include the resulting value, QmFkQm90 , in the value of SearchString .

If youâre using the AWS CLI or one of the AWS SDKs

The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.



PositionalConstraint -> (string)

The area within the portion of a web request that you want AWS WAF to search for SearchString . Valid values include the following:

CONTAINS

The specified part of the web request must include the value of SearchString , but the location doesnât matter.

CONTAINS_WORD

The specified part of the web request must include the value of SearchString , and SearchString must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, SearchString must be a word, which means that both of the following are true:

SearchString is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and ;BadBot .
SearchString is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, BadBot; and -BadBot; .


EXACTLY

The value of the specified part of the web request must exactly match the value of SearchString .

STARTS_WITH

The value of SearchString must appear at the beginning of the specified part of the web request.

ENDS_WITH

The value of SearchString must appear at the end of the specified part of the web request.


SqliMatchStatement -> (structure)

Attackers sometimes insert malicious SQL code into web requests in an effort to extract data from your database. To allow or block web requests that appear to contain malicious SQL code, create one or more SQL injection match conditions. An SQL injection match condition identifies the part of web requests, such as the URI or the query string, that you want AWS WAF to inspect. Later in the process, when you create a web ACL, you specify whether to allow or block requests that appear to contain malicious SQL code.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




XssMatchStatement -> (structure)

A rule statement that defines a cross-site scripting (XSS) match search for AWS WAF to apply to web requests. XSS attacks are those where the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. The XSS match statement provides the location in requests that you want AWS WAF to search and text transformations to use on the search area before AWS WAF searches for character sequences that are likely to be malicious strings.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




SizeConstraintStatement -> (structure)

A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.
If you configure AWS WAF to inspect the request body, AWS WAF inspects only the first 8192 bytes (8 KB). If the request body for your web requests never exceeds 8192 bytes, you can create a size constraint condition and block requests that have a request body greater than 8192 bytes.
If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.
FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


ComparisonOperator -> (string)

The operator to use to compare the request part to the size setting.

Size -> (long)

The size, in byte, to compare to the request part, after any transformations.

TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




GeoMatchStatement -> (structure)

A rule statement used to identify web requests based on country of origin.
CountryCodes -> (list)

An array of two-character country codes, for example, [ "US", "CN" ] , from the alpha-2 country ISO codes of the ISO 3166 international standard.
(string)

ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




RuleGroupReferenceStatement -> (structure)

A rule statement used to run the rules that are defined in a  RuleGroup . To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.
You cannot nest a RuleGroupReferenceStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
ARN -> (string)

The Amazon Resource Name (ARN) of the entity.

ExcludedRules -> (list)

The names of rules that are in the referenced rule group, but that you want AWS WAF to exclude from processing for this rule statement.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.




IPSetReferenceStatement -> (structure)

A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an  IPSet that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see  CreateIPSet .
Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  IPSet that this statement references.

IPSetForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.


Position -> (string)

The position in the header to search for the IP address. The header can contain IP addresses of the original client and also of proxies. For example, the header value could be 10.1.1.1, 127.0.0.0, 10.10.10.10 where the first IP address identifies the original client and the rest identify proxies that the request went through.
The options for this setting are the following:

FIRST - Inspect the first IP address in the list of IP addresses in the header. This is usually the clientâs original IP.
LAST - Inspect the last IP address in the list of IP addresses in the header.
ANY - Inspect all IP addresses in the header for a match. If the header contains more than 10 IP addresses, AWS WAF inspects the last 10.




RegexPatternSetReferenceStatement -> (structure)

A rule statement used to search web request components for matches with regular expressions. To use this, create a  RegexPatternSet that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see  CreateRegexPatternSet .
Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.
ARN -> (string)

The Amazon Resource Name (ARN) of the  RegexPatternSet that this statement references.

FieldToMatch -> (structure)

The part of a web request that you want AWS WAF to inspect. For more information, see  FieldToMatch .
SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, User-Agent or Referer . This setting isnât case sensitive.
Name -> (string)

The name of the query header to inspect.


SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as UserName or SalesRegion . The name can be up to 30 characters long and isnât case sensitive.
This is used only to indicate the web request component for AWS WAF to inspect, in the  FieldToMatch specification.
Name -> (string)

The name of the query argument to inspect.


AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of a web request that identifies a resource, for example, /images/daily-ad.jpg .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a ? character, if any.

Body -> (structure)

Inspect the request body, which immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.
Note that only the first 8 KB (8192 bytes) of the request body are forwarded to AWS WAF for inspection by the underlying host service. If you donât need to inspect more than 8 KB, you can guarantee that you donât allow additional bytes in by combining a statement that inspects the body of the web request, such as  ByteMatchStatement or  RegexPatternSetReferenceStatement , with a  SizeConstraintStatement that enforces an 8 KB size limit on the body of the request. AWS WAF doesnât support inspecting the entire contents of web requests whose bodies exceed the 8 KB limit.

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.


TextTransformations -> (list)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by FieldToMatch , starting from the lowest priority setting, before inspecting the content for a match.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.
Priority -> (integer)

Sets the relative processing order for multiple transformations that are defined for a rule statement. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities donât need to be consecutive, but they must all be different.

Type -> (string)

You can specify the following transformation types:

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

NONE

Specify NONE if you donât want any text transformations.




RateBasedStatement -> (structure)

A rate-based rule tracks the rate of requests for each originating IP address, and triggers the rule action when the rate exceeds a limit that you specify on the number of requests in any 5-minute time span. You can use this to put a temporary block on requests from an IP address that is sending excessive requests.
When the rule action triggers, AWS WAF blocks additional requests from the IP address until the request rate falls below the limit.
You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts requests that match the nested statement. For example, based on recent requests that you have seen from an attacker, you might create a rate-based rule with a nested AND rule statement that contains the following nested statements:

An IP match statement with an IP set that specified the address 192.0.2.44.
A string match statement that searches in the User-Agent header for the string BadBot.

In this rate-based rule, you also define a rate limit. For this example, the rate limit is 1,000. Requests that meet both of the conditions in the statements are counted. If the count exceeds 1,000 requests per five minutes, the rule action triggers. Requests that do not meet both conditions are not counted towards the rate limit and are not affected by this rule.
You cannot nest a RateBasedStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
Limit -> (long)

The limit on requests per 5-minute period for a single originating IP address. If the statement includes a ScopeDownStatement , this limit is applied only to the requests that match the statement.

AggregateKeyType -> (string)

Setting that indicates how to aggregate the request counts. The options are the following:

IP - Aggregate the request counts on the IP address from the web request origin.
FORWARDED_IP - Aggregate the request counts on the first IP address in an HTTP header. If you use this, configure the ForwardedIPConfig , to specify the header to use.


( â¦ recursive â¦ )ForwardedIPConfig -> (structure)

The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address thatâs reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

This is required if AggregateKeyType is set to FORWARDED_IP .
HeaderName -> (string)

The name of the HTTP header to use for the IP address. For example, to use the X-Forwarded-For (XFF) header, set this to X-Forwarded-For .

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.


FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a valid IP address in the specified position.

Note
If the specified header isnât present in the request, AWS WAF doesnât apply the rule to the web request at all.

You can specify the following fallback behaviors:

MATCH - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
NO_MATCH - Treat the web request as not matching the rule statement.




AndStatement -> (structure)

A logical rule statement used to combine other rule statements with AND logic. You provide more than one  Statement within the AndStatement .
Statements -> (list)

The statements to combine with AND logic. You can use any statements that can be nested.
( â¦ recursive â¦ )


OrStatement -> (structure)

A logical rule statement used to combine other rule statements with OR logic. You provide more than one  Statement within the OrStatement .
Statements -> (list)

The statements to combine with OR logic. You can use any statements that can be nested.
( â¦ recursive â¦ )


NotStatement -> (structure)

A logical rule statement used to negate the results of another rule statement. You provide one  Statement within the NotStatement .
( â¦ recursive â¦ )

ManagedRuleGroupStatement -> (structure)

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You canât nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
VendorName -> (string)

The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name -> (string)

The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules -> (list)

The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.






ManagedRuleGroupStatement -> (structure)

A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling  ListAvailableManagedRuleGroups .
You canât nest a ManagedRuleGroupStatement , for example for use inside a NotStatement or OrStatement . It can only be referenced as a top-level statement within a rule.
VendorName -> (string)

The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.

Name -> (string)

The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

ExcludedRules -> (list)

The rules whose actions are set to COUNT by the web ACL, regardless of the action that is set on the rule. This effectively excludes the rule from acting on web requests.
(structure)


Note
This is the latest version of AWS WAF , named AWS WAFV2, released in November, 2019. For information, including how to migrate your AWS WAF resources from the prior release, see the AWS WAF Developer Guide .

Specifies a single rule to exclude from the rule group. Excluding a rule overrides its action setting for the rule group in the web ACL, setting it to COUNT . This effectively excludes the rule from acting on web requests.
Name -> (string)

The name of the rule to exclude.





Action -> (structure)

The action that AWS WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting.
This is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include RuleGroupReferenceStatement and ManagedRuleGroupStatement .
You must specify either this Action setting or the rule OverrideAction setting, but not both:

If the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting.
If the rule statement references a rule group, use the override action setting and not this action setting.

Block -> (structure)

Instructs AWS WAF to block the web request.

Allow -> (structure)

Instructs AWS WAF to allow the web request.

Count -> (structure)

Instructs AWS WAF to count the web request and allow it.


OverrideAction -> (structure)

The override action to apply to the rules in a rule group. Used only for rule statements that reference a rule group, like RuleGroupReferenceStatement and ManagedRuleGroupStatement .
Set the override action to none to leave the rule actions in effect. Set it to count to only count matches, regardless of the rule action settings.
In a  Rule , you must specify either this OverrideAction setting or the rule Action setting, but not both:

If the rule statement references a rule group, use this override action setting and not the action setting.
If the rule statement does not reference a rule group, use the rule action setting and not this rule override action setting.

Count -> (structure)

Override the rule action setting to count.

None -> (structure)

Donât override the rule action setting.


VisibilityConfig -> (structure)

Defines and enables Amazon CloudWatch metrics and web request sample collection.
SampledRequestsEnabled -> (boolean)

A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.

CloudWatchMetricsEnabled -> (boolean)

A boolean indicating whether the associated resource sends metrics to CloudWatch. For the list of available metrics, see AWS WAF Metrics .

MetricName -> (string)

A name of the CloudWatch metric. The name can contain only the characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore). The name can be from one to 128 characters long. It canât contain whitespace or metric names reserved for AWS WAF, for example âAllâ and âDefault_Action.â
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("wafv2", "check-capacity", "scope", "rules", add_option_dict)
