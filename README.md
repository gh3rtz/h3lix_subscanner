<h1>H3lix Subdomain Enumerator</h1>
This is a Python script that uses the SecurityTrails API to enumerate subdomains for a given domain.

Prerequisites
To run this script, you need:

Note that you need to replace YOUR_API_KEY_HERE with your actual SecurityTrails API key.
Python 3.x
The requests and termcolor Python modules
You can install the required modules using the pip package manager:
pip install -r requirements.txt

Usage
To run the script, use the following command:

python subdomain_enumerator.py -d <domain>
Replace <domain> with the domain you want to enumerate subdomains for.

By Default, This will save the list of subdomains to a file named <domain>\_subdomains.txt.

License
