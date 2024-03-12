## About the connector

Google Cloud Functions is a serverless execution environment for building and connecting cloud services.
<p>This document provides information about the Google Cloud Functions Connector, which facilitates automated interactions, with a Google Cloud Functions server using FortiSOAR&trade; playbooks. Add the Google Cloud Functions Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Google Cloud Functions.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No

## Installing the connector

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-google-cloud-functions</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Google Cloud Functions server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Google Cloud Functions server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector

For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Google Cloud Functions</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>The service-based URI to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Client ID</td><td>Unique Client ID of the Google Cloud Functions that is used to create an authentication token required to access the Google Cloud Functions API.
</td>
</tr><tr><td>Client Secret</td><td>Unique Client Secret of the Google Cloud Functions that is used to create an authentication token required to access the API. For information on how to get the client secret, see https://developers.google.com/identity/protocols/oauth2/web-server.
</td>
</tr><tr><td>Authorization Code</td><td>The authorization code that you acquired during the authorization step. For more information, see the Accessing the Google Cloud Functions API section.
</td>
</tr><tr><td>Redirect URL</td><td>The redirect_uri of your app, where authentication responses can be sent and received by your app. It must exactly match one of the redirect_uri's you registered in the app registration portal.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector

The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Locations List</td><td>Retrieves a list of information about the supported locations for this service from Google Cloud Functions based on the project name and other input parameters you have specified.</td><td>get_locations_list <br/>Investigation</td></tr>
<tr><td>Get Functions List</td><td>Retrieves a list of functions that belong to the requested project from Google Calendar based on the project name, location, and other input parameters you have specified.</td><td>get_functions_list <br/>Investigation</td></tr>
<tr><td>Get Function Details</td><td>Retrieves an specific function information from Google Cloud Functions based on the project name, location name, and function name you have specified.</td><td>get_function_details <br/>Investigation</td></tr>
<tr><td>Get Access Control Policy</td><td>Retrieves the access control policy for a resource from Google Cloud Functions, it returns an empty policy if the resource exists and does not have a policy set.</td><td>get_access_control_policy <br/>Investigation</td></tr>
<tr><td>Set Access Control Policy</td><td>Sets the access control policy on the specified resource. Replaces any existing policy.</td><td>set_access_control_policy <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Locations List

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Project Name</td><td>Specify the name of the project based on which you want to retrieve locations from Google Cloud Functions.
</td></tr><tr><td>Filter</td><td>Specify the filter using values of certain attributes, for example, displayName=tokyo, based on which you want to filter the locations retrieved from Google Cloud Functions.
</td></tr><tr><td>PageSize</td><td>Specify the maximum number of results to return. If not set, the service selects a default.
</td></tr><tr><td>PageToken</td><td>Specify a PageToken if a previous operation returned a partial result. If the previous response contains a nextPageToken element, the value of the nextPageToken element includes a PageToken parameter that specifies a starting point to use for subsequent calls.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Functions List

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Project Name</td><td>Specify the name of the project based on which you want to retrieve functions from Google Cloud Functions.
</td></tr><tr><td>Location</td><td>Specify the location based on which you want to retrieve functions from Google Cloud Functions.
</td></tr><tr><td>Filter</td><td>Specify the filter using values of certain attributes, for example, displayName=tokyo, based on which you want to filter the locations retrieved from Google Cloud Functions.
</td></tr><tr><td>Order By</td><td>Specify the comma separated list of fields. The default sorting oder is ascending.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Function Details

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Project Name</td><td>Specify the name of the project based on which you want to retrieve specific function details from Google Cloud Functions.
</td></tr><tr><td>Location</td><td>Specify the location based on which you want to retrieve specific function details from Google Cloud Functions.
</td></tr><tr><td>Function Name</td><td>Specify the name of the function based on which you want to retrieve specific function details from Google Cloud Functions.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Access Control Policy

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Project Name</td><td>Specify the name of the project based on which you want to retrieve access control policy from Google Cloud Functions.
</td></tr><tr><td>Location</td><td>Specify the location based on which you want to retrieve access control policy from Google Cloud Functions.
</td></tr><tr><td>Function Name</td><td>Specify the name of the function based on which you want to retrieve access control policy from Google Cloud Functions.
</td></tr><tr><td>Policy Version</td><td>Specify the maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Set Access Control Policy

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Project Name</td><td>Specify the name of the project based on which you want to set the access control policy in Google Cloud Functions.
</td></tr><tr><td>Location</td><td>Specify the location based on which you want to set the access control policy in Google Cloud Functions.
</td></tr><tr><td>Function Name</td><td>Specify the name of the function based on which you want to set the access control policy in Google Cloud Functions.
</td></tr><tr><td>Audit Configs</td><td>Specifies the audit configuration for a service, configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs.
</td></tr><tr><td>Bindings</td><td>A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role.
</td></tr><tr><td>Etag</td><td>Specify the etag based on which you want to set the access control policy in Google Cloud Functions.
</td></tr><tr><td>Policy Version</td><td>Specify the maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3.
</td></tr><tr><td>Update Mask</td><td>Specify the comma-separated list of fully qualified names of fields.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

## Included playbooks

The `Sample - google-cloud-functions - 1.0.0` playbook collection comes bundled with the Google Cloud Functions connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Google Cloud Functions connector.

- Get Access Control Policy
- Get Function Details
- Get Functions List
- Get Locations List
- Set Access Control Policy

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
