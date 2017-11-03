#!/usr/bin/env python
import os
import time
import novaclient.v1_1.client as nvclient

from cred import get_nova_creds


creds = get_nova_creds()
# Create an instance with our creds
nova = nvclient.Client(**creds)

# Make sure the keypair exist, if not create one
if not nova.keypairs.findall(name="key"):
    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as pubkey:
        nova.keypairs.create(name="key", public_key=pubkey.read())

image = nova.images.find(name="cirros-0.3.1-x86_64-uec")
flavor = nova.flavors.find(name="m1.tiny")

#vm = input("Select number of VMs to spawn: ")


# start counter
start = time.time()

# Launch the instance
instance = nova.servers.create(name="test",
        image=image, flavor=flavor, key_name="key", min_count=20)

# Poll at 5 second intervals, until the status is no longer 'BUILD'
status = instance.status
while status == 'BUILD':
    time.sleep(1)
    # Retrieve the instance again so the status field updates
    instance = nova.servers.get(instance.id)
    status = instance.status

end = time.time()
print "status: %s" % status
delta = end-start
print "%.2gs" % delta


output_file = open('output.txt','w')
print >> output_file, delta
