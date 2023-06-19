import requests
import json
import csv

# Read IP addresses from a text file
with open('ip_address.txt', 'r') as file:
    ip_addresses = file.read().splitlines()

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'
headers = {
    'Accept': 'application/json',
    'Key': 'API KEY'
}

# Open CSV file for writing
with open('ip_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['IP Address', 'ISP', 'Abuse Confidence Score', 'Country Code', 'Usage Type', 'Hostnames', 'Domain', 'Whitelisted', 'Last Reported at']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write CSV header
    writer.writeheader()

    for ip_address in ip_addresses:
        querystring = {
            'ipAddress': ip_address,
            'maxAgeInDays': '90'
        }

        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        decodedResponse = json.loads(response.text)

        # Write IP details to CSV
        writer.writerow({
            'IP Address': ip_address,
            'ISP': decodedResponse['data']['isp'],
            'Abuse Confidence Score': decodedResponse['data']['abuseConfidenceScore'],
            'Country Code': decodedResponse['data']['countryCode'],
            'Usage Type': decodedResponse['data']['usageType'],
            'Hostnames' : decodedResponse['data']['hostnames'],
            'Domain' : decodedResponse['data']['domain'],
            'Whitelisted' : decodedResponse['data']['isWhitelisted'],
            'Last Reported at' : decodedResponse['data']['lastReportedAt']

        })