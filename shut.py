#!/usr/bin/env python
import os
import time
import novaclient.v1_1.client as nvclient

from cred import get_nova_creds


creds = get_nova_creds()

# Create an instance with our credentials
nova = nvclient.Client(**creds)

server_list = nova.servers.list()
# Delete all nova servers
for s in server_list:
    nova.servers.delete(s)
