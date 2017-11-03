#!/usr/bin/env python
import os

def get_keystone_creds():
    user = {}
    user['username'] = os.environ['OS_USERNAME']
    user['password'] = os.environ['OS_PASSWORD']
    user['auth_url'] = os.environ['OS_AUTH_URL']
    user['tenant_name'] = os.environ['OS_TENANT_NAME']
    return user

def get_nova_creds():
    user = {}
    user['username'] = os.environ['OS_USERNAME']
    user['api_key'] = os.environ['OS_PASSWORD']
    user['auth_url'] = os.environ['OS_AUTH_URL']
    user['project_id'] = os.environ['OS_TENANT_NAME']
    return user
