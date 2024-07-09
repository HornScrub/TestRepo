f = 'subdomains.txt'

subdomain_list = []

with open(f, 'r') as file:
    subdomains = file.readlines()

for subdomain in subdomains:
    subdomain_list.append(subdomain.strip())

print(subdomain_list)

