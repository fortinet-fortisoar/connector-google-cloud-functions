"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from requests import request
from connectors.core.connector import get_logger, ConnectorError
from .google_api_auth import *
from .constants import *

CLOUD_FUNCTIONS_API_VERSION = 'v2'

logger = get_logger('google-cloud-functions')


def api_request(method, endpoint, connector_info, config, params=None, data=None, headers={}):
    try:
        go = GoogleAuth(config)
        endpoint = go.host + "/" + endpoint
        token = go.validate_token(config, connector_info)
        headers['Authorization'] = token
        headers['Content-Type'] = 'application/json'
        response = request(method, endpoint, headers=headers, params=params, data=data, verify=go.verify_ssl)
        if response.ok or response.status_code == 204:
            if 'json' in str(response.headers):
                return response.json()
            else:
                return response
        else:
            logger.error("{0}".format(response.status_code))
            raise ConnectorError("{0}:{1}".format(response.status_code, response.text))
    except requests.exceptions.SSLError:
        raise ConnectorError('SSL certificate validation failed')
    except requests.exceptions.ConnectTimeout:
        raise ConnectorError('The request timed out while trying to connect to the server')
    except requests.exceptions.ReadTimeout:
        raise ConnectorError(
            'The server did not send any data in the allotted amount of time')
    except requests.exceptions.ConnectionError:
        raise ConnectorError('Invalid Credentials')
    except Exception as err:
        raise ConnectorError(str(err))


def check_payload(payload):
    l = {}
    for k, v in payload.items():
        if isinstance(v, dict):
            x = check_payload(v)
            if len(x.keys()) > 0:
                l[k] = x
        elif isinstance(v, list):
            p = []
            for c in v:
                if isinstance(c, dict):
                    x = check_payload(c)
                    if len(x.keys()) > 0:
                        p.append(x)
                elif c is not None and c != '':
                    p.append(c)
            if p != []:
                l[k] = p
        elif v is not None and v != '':
            l[k] = v
    return l


def build_payload(payload):
    payload = {k: v for k, v in payload.items() if v is not None and v != ''}
    return payload


def get_locations_list(config, params, connector_info):
    try:
        url = '{0}/projects/{1}/locations'.format(CLOUD_FUNCTIONS_API_VERSION, params.pop('project_name'))
        query_parameter = build_payload(params)
        response = api_request('GET', url, connector_info, config, params=query_parameter)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def get_functions_list(config, params, connector_info):
    try:
        url = '{0}/projects/{1}/locations/{2}/functions'.format(CLOUD_FUNCTIONS_API_VERSION, params.pop('project_name'),
                                                                params.pop('location_name'))
        query_parameter = build_payload(params)
        response = api_request('GET', url, connector_info, config, params=query_parameter)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def get_function_details(config, params, connector_info):
    try:
        url = '{0}/projects/{1}/locations/{2}/functions/{3}'.format(CLOUD_FUNCTIONS_API_VERSION,
                                                                    params.get('project_name'),
                                                                    params.get('location_name'),
                                                                    params.get('function_name'))
        response = api_request('GET', url, connector_info, config)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def get_access_control_policy(config, params, connector_info):
    try:
        url = '{0}/projects/{1}/locations/{2}/functions/{3}:getIamPolicy'.format(CLOUD_FUNCTIONS_API_VERSION,
                                                                                 params.get('project_name'),
                                                                                 params.get('location_name'),
                                                                                 params.get('function_name'))
        query_parameter = {
            'options': {
                'requestedPolicyVersion': params.get('requestedPolicyVersion')
            }
        }
        query_parameter = check_payload(query_parameter)
        response = api_request('GET', url, connector_info, config, params=query_parameter)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def set_access_control_policy(config, params, connector_info):
    try:
        url = '{0}/projects/{1}/locations/{2}/functions/{3}:setIamPolicy'.format(CLOUD_FUNCTIONS_API_VERSION,
                                                                                 params.get('project_name'),
                                                                                 params.get('location_name'),
                                                                                 params.get('function_name'))
        query_parameter = {
            'policy': {
                'auditConfigs': params.get('auditConfigs'),
                'bindings': params.get('bindings'),
                'etag': params.get('etag'),
                'version': params.get('version')
            },
            'updateMask': params.get('updateMask')
        }
        query_parameter = check_payload(query_parameter)
        response = api_request('GET', url, connector_info, config, params=query_parameter)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def _check_health(config, connector_info):
    try:
        return check(config, connector_info)
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


operations = {
    'get_locations_list': get_locations_list,
    'get_functions_list': get_functions_list,
    'get_function_details': get_function_details,
    'get_access_control_policy': get_access_control_policy,
    'set_access_control_policy': set_access_control_policy
}
