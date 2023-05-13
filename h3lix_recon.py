import requests
import json
from art import text2art
from termcolor import colored
import sys

# ASCII art for "Givari Hertz"
ascii_art = text2art("Givari Hertz")
instagram_handle = "Twitter: @gh3rtz    Instagram: @givarirmdn"

# Print the ASCII art and Instagram handle in green color
print(colored(ascii_art, "green"))
print(colored(instagram_handle, "green"))

# SecurityTrails API endpoint
api_url = "https://api.securitytrails.com/v1/domain/"

# API key
api_key = "Adds0tR77oE62HwQRLAFJeGjSEBg08C2"

# Helper message for the command-line arguments
helper = '''
Usage: python filename.py -d <domain> [-o <output_file>] | -l <input_file>

Options:
  -d <domain>          Scans the subdomains of the specified domain.
  -l <input_file>      Scans the subdomains of the domains in the specified file.
  -o <output_file>     Saves the output to the specified file. If not specified, creates a file with the default name.
  -h                   Shows this helper message.
'''

# Get the target domains from the command-line arguments
if len(sys.argv) < 3 or '-h' in sys.argv:
    print(colored(helper, 'yellow'))
    sys.exit(0)

if sys.argv[1] == "-d":
    target_domains = [sys.argv[2]]
elif sys.argv[1] == "-l":
    input_file = sys.argv[2]
    with open(input_file, "r") as f:
        target_domains = [line.strip() for line in f.readlines()]
else:
    print(colored(helper, "yellow"))
    sys.exit(1)

# Loop through the target domains and scan their subdomains
for target_domain in target_domains:
    # Construct the API request URL
    api_request_url = api_url + target_domain + "/subdomains"

    # API request headers
    api_request_headers = {
        "APIKEY": api_key,
        "Content-Type": "application/json"
    }

    # Send the API request
    response = requests.get(api_request_url, headers=api_request_headers)

    # Parse the API response JSON data
    subdomains_data = json.loads(response.text)

    # Extract the subdomains from the response data
    subdomains_list = subdomains_data["subdomains"]

    # Print the subdomains with their URLs in green color
    print(colored(f"\nSubdomains for {target_domain}:", "green"))
    output = []
    for subdomain in subdomains_list:
        url = f"https://{subdomain}.{target_domain}"
        output.append(url)
        print(colored(url, "green"))

    # Save the output to a file if specified with the -o argument, or create a new file with the default name
    output_file_name = f"{target_domain}_subdomains.txt"
    if "-o" in sys.argv:
        output_file_index = sys.argv.index("-o") + 1
        output_file_name = sys.argv[output_file_index]
    with open(output_file_name, "w") as f:
        f.write("\n".join(output))
    print(colored(f"\nOutput saved to {output_file_name}", "red"))
