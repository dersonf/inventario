#!/bin/bash
SERVER_IP=192.168.1.63
HOSTNAME=$(hostname)
GREP=$(which grep)
KERNEL=$(uname -r)
ID=$(cat /etc/machine-id)
TEST_DISTRO=$(grep -i 'debian' /etc/*-release)

if [ ! -z "$TEST_DISTRO" ] ; then
    DISTRO='Debian'
    RELEASE=$($GREP PRETTY_NAME /etc/os-release | cut -d '=' -f2 | sed 's/"//g')
    VERSION=$(cat /etc/debian_version)
    IP=$(hostname -I | awk {'print $1'})
fi

generate_post_data()
{
  cat <<EOF
{
    "hostname": "$HOSTNAME",
    "hostid": "$ID",
    "kernel": "$KERNEL",
    "distro": "$DISTRO",
    "release": "$RELEASE",
    "version": "$VERSION",
    "host_ip": "$IP"
}
EOF
}

curl -H "Content-Type:application/json" -X POST -d "$(generate_post_data)" http://$SERVER_IP:5000/inventory/api

