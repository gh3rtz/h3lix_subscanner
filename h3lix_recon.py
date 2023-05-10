import sys
import requests
import json
from art import text2art
from termcolor import colored

# ASCII art for "Givari Hertz"
ascii_art = text2art("Givari Hertz")
instagram_handle = "Twitter: @gh3rtz    Instagram: @givarihertz"

# Print the ASCII art and Instagram handle in green color
print(colored(ascii_art, "green"))
print(colored(instagram_handle, "green"))

# SecurityTrails API endpoint
api_url = "https://api.securitytrails.com/v1/domain/"

# API key
api_key = "<YOUR_API_KEY_HERE>"

# Get the target domain from the command-line arguments
if len(sys.argv) < 3 or sys.argv[1] != "-d":
    print(
        colored("Usage: python filename.py -d <domain> [-o <output_file>]", "red"))
    sys.exit(1)

target_domain = sys.argv[2]

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
if "-o" in sys.argv:
    output_file_index = sys.argv.index("-o") + 1
    output_file_name = sys.argv[output_file_index]
else:
    output_file_name = f"{target_domain}_subdomains.txt"

with open(output_file_name, "w") as f:
    f.write("\n".join(output))
print(colored(f"\nOutput saved to {output_file_name}", "red"))
