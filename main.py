import portscanner

targets_ip = input('[+] * Enter Target: ')
port_num = int(input('[+] How many ports will you scan (1 - 500): '))
vulnv_file = ("vul_banners.txt")
print('\n')

target = portscanner.PortScan(targets_ip, port_num)
target.scan()

with open(vulnv_file, 'r') as file:
	count = 0
	for banner in target.banners:
	 	file.seek(0)
	 	for line in file.readlines():
	 		if line.strip() in banner:
	 			print('[!!] Vulnerable banner: "' + banner + '" On port: ' + str(target.open_ports[count]))
	 	count += 1