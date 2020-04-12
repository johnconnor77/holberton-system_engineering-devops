#!/usr/bin/env bash
#Bash script that display info about subdomains

if [ $# -eq 1 ]; then
  subs=("www" "lb-01" "web-01" "web-02")
  for sub in "${subs[@]}"; do
    type=$(dig "$sub"."$1" | grep -A1 'ANSWER SECTION'| tail -n 1 | awk '{print $4}')
    ip_address=$(dig "$sub"."$1" | grep -A1 'ANSWER SECTION'| tail -n 1 | awk '{print $5}')
    echo "The subdomain $sub is a $type record and point to $ip_address"
  done
elif [ $# -eq 2 ]; then
  type=$(dig "$2"."$1" | grep -A1 'ANSWER SECTION'| tail -n 1 | awk '{print $4}')
  ip_address=$(dig "$2"."$1" | grep -A1 'ANSWER SECTION'| tail -n 1 | awk '{print $5}')
  echo "The subdomain $2 is a $type record and point to $ip_address"
fi