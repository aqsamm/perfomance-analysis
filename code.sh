. ./openrc

# Loop for adding delays
for x in {1000..10000..1000}
do
sudo tc qdisc add dev eth0 root netem delay $x

# Add key pair and save private key in the file
nova keypair-add key > key.pem

python launch.py
sleep 5

#removing the delay
sudo tc qdisc del dev eth0 root

#shutting down VMs
python shut.py
sleep 5

done
