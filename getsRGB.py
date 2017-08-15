import os

# Convert their wierd format
def hexToDec(hexa):
	ret = ''
	for i in range(2,len(hexa)-1,2):
		ret += hexa[i] + hexa[i+1] + " "
	if not (len(hexa)%2 == 0): ret += hexa[-1] + "0 "
	return ret.replace("  ","")

# Indentify and convert to decimal
def convertToDecimal(string):
	begin = -1
	first = True
	backup = ''
	tmp = []
	for i in range(len(string)-1):
		if string[i:i+2] == "0x":
			begin = i
			if first:
				backup = string[:i]
				first = False
		if (begin > 0) and (string[i] == " "):
			end = i
			tmp.append(hexToDec(string[begin:end])) # Convert to decimal
			begin = 1
			end = -1
	for j in tmp:
		backup += j + ' '
	return (backup + '];').replace("<","[")

# Get all the DT available
dt_files = os.popen('find DTS/ -follow -type f | grep "dts"').readlines()

# Get all the nodes
srgb_on = 'qcom,mdss-dsi-dispparam-srgb-command'
cm_srgb_on = 'cm,mdss-livedisplay-srgb-on-cmd'
avoid = ['mdss-dsi-dispparam-srgb-command-state','qcom,mdss_dsi_ctrl','qcom,mdss_dsi_pll','@'] # Just to feel safe
panel_name = 'qcom,mdss_dsi_'
nodes = []
for dt in dt_files:
	tmp = open(dt[:-1])
	lines = tmp.readlines()
	for line in lines:
		if any(x in line for x in avoid): continue
		if (panel_name in line) and ("{" in line): nodes.append(line)
		if (srgb_on in line) : nodes.append(line)
	tmp.close()

# Convert HEX to Decimal
ret = []
for i in nodes:
	if "0x" in i: ret.append(convertToDecimal(i))
	else: ret.append(i)

# Print
seen = []
panels = []
for k in range(len(ret)):
	if (panel_name in ret[k]) and (srgb_on in ret[k+1]) and not (ret[k] in seen):
		print "****************"
		print ret[k][2:-2]
		print (ret[k+1][3:-1]).replace(srgb_on,cm_srgb_on)
		seen.append(ret[k])

# Panels
for l in seen: print l[:-2]
