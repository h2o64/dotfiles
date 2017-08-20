import os

# Xiaomi DTs
xiaomi_dt = [
'qcom,mdss_dsi_auo_fte716_1080p_video',
'qcom,mdss_dsi_jdi_fhd_r63452_cmd',
'qcom,mdss_dsi_jdi_fhd_r63452_j1_cmd',
'qcom,mdss_dsi_jdi_fhd_r63452_j1_pro_cmd',
'qcom,mdss_dsi_jdi_fhd_r63452_pro_cmd',
'qcom,mdss_dsi_jdi_fhd_r63452_video',
'qcom,mdss_dsi_jdi_fhd_r63452_xcmd',
'qcom,mdss_dsi_lgd_fhd_td4322_cmd',
'qcom,mdss_dsi_lgd_fhd_td4722_cmd',
'qcom,mdss_dsi_lgd_sw43101_fhd_video',
'qcom,mdss_dsi_lgd_sw43101_p2_fhd_video',
'qcom,mdss_dsi_samsung_Qhd_command',
'qcom,mdss_dsi_samsung_youm_Qhd_command',
'qcom,mdss_dsi_sharp_fhd_nt35695_cmd',
'qcom,mdss_dsi_sharp_fhd_nt35695_video',
'qcom,mdss_dsi_sharp_fhd_td4722_xcmd',
'qcom,mdss_dsi_sharp_fte716_1080p_video',
'qcom,capricorn_atl',
'qcom,capricorn_sdi',
'qcom,a1_atl_3000mah',
'qcom,a1_sdi_3000mah',
'qcom,a8_atl',
'qcom,natrium_atl_3840mah',
'qcom,b7_lg_3840mah',
'qcom,a4_atl',
'qcom,scorpio_coslight']

hex_blacklist = ['qcom,mdss-dsi-underflow-color','qcom,mdss-dsi-t-clk-post','qcom,mdss-dsi-t-clk-pre','qcom,mdss-dsi-wr-mem-start','qcom,mdss-dsi-wr-mem-continue','qcom,chg-rslow-comp-thr','qcom,checksum']
blacklist = ["phandle","qcom,config-select","qcom,mdss-dsi-displayo","qcom,mdss-night-brightness","qcom,panel-supply-entries","qcom,mdss-dsi-panel-model","qcom,video-panel-esd-te-check","qcom,mdss-panel-on-dimming-delay","qcom,esd-err-irq-gpio",'qcom,mdss-dsi-dispparam-cabcguion-command','qcom,mdss-dsi-dispparam-cabcmovieon-command','qcom,mdss-dsi-dispparam-cabcstillon-command', 'qcom,mdss-dsi-dispparam-srgb-command-state']

# Get dt number
def getDTNum(dt):
	for x in range(len(xiaomi_dt)):
		if dt in xiaomi_dt[x]: return x
	# print "DT num can't be found : " + dt

# Convert their wierd format
def hexToDec(hexa, battery):
	raw_buf = ''
	# Make each hex 10 characters longs
	for i in hexa:
		raw_buf += "0x"
		if len(i) != 10:
			for j in range(10-len(i)): raw_buf += "0"
		raw_buf += i[2:]
	# Make the spaces
	buf = ''
	tmp = raw_buf.replace("0x","")
	for k in range(len(tmp)):
		if k%2 == 0: buf += " "
		buf += tmp[k]
	return indentBytes(buf[1:], battery)

# Make indentation
def indentBytes(string, battery):
	# Add `\t` and `\n`
	buf = ''
	started = False
	count = 0
	if battery: limit = 4
	else: limit = 9
	for j in range(len(string)):
		if count == limit:
			buf += "\n\t\t\t\t"
			count = 0
		buf += string[j]
		if string[j] == " ": count += 1
	return buf.upper()

# Get the value between <**>
def getValues(string):
	ret = []
	begin = -1
	for i in range(len(string)-1):
		if string[i:i+2] == "0x": begin = i
		elif (begin > 0) and (string[i] == '>'):
			ret.append(string[begin:i])
			begin = -1
			return ret
		elif (begin > 0) and (string[i] == ' '):
			ret.append(string[begin:i])
			begin = -1
	return ret # Worst case scenario

# Convert reset-seq to right format
def formatReset(string):
	values = getValues(string)
	ret = ''
	for i in range(len(values)):
		if i%2 == 0: ret += '<'
		ret += str(int(values[i],16))
		if i%2 == 0: ret += ' '
		else: ret += '>, '
	return ret[:-2] + ';'

# Indentify and convert to right format
def convertToDecimal(entry):
	# Empty value
	if (entry[1] == ''): return "\t\t" + entry[0]
	# Regular string || Display ON/OFF CMD
	elif ('"' in entry[1]) or ('[' in entry[1]) or (entry[0] in hex_blacklist): return "\t\t" + entry[0] + " = " + entry[1]
	# HEX-ed display CMD/Timing
	elif ("-command" in entry[0]) or ("-cmd" in entry[0]) or ("-timings" in entry[0]) or ("fg-profile-data" in entry[0]):
		values = getValues(entry[1])
		buf = "\t\t" + entry[0] + ' = [\n\t\t\t\t'
		if not "fg-profile-data" in entry[0]:
			buf += hexToDec(values, False)
		else:
			buf += hexToDec(values, True)
		return buf + '];'
	# Reset sequence
	elif ("qcom,mdss-dsi-reset-sequence" in entry[0]):
		return "\t\t" + entry[0] + " = " + formatReset(entry[1])
	# Hex to int
	else:
		values = getValues(entry[1])
		buf = entry[0] + ' = <'
		for i in values: buf += str(int(i,16)) + ' '
		return "\t\t" + buf[:-1] + '>;'

# Get all the DT available
dt_miui_files = os.popen('find DTS/ -follow -type f | grep "dts"').readlines()
dt_la_files = os.popen('find DTS_LA/ -follow -type f | grep "dts"').readlines()

# Get dt name (qcom,*)
def getDTName(string):
	for i in range(len(string)):
		if string[i] == ',': return string[i-4:-3]

# Get the entry tuple
def getEntryTuple(entry):
	for i in range(len(entry)):
		if entry[i] == '=': return (entry[2:i-1],entry[i+2:-1])
	return (entry[2:-1],'')

# Replace with correct name
def replaceName(name):
	tmp = name
	old_timing = "qcom,mdss-dsi-panel-timings-8996"
	new_timing = "qcom,mdss-dsi-panel-timings-phy-v2"
	old_srgb = "qcom,mdss-dsi-dispparam-srgb-command"
	new_srgb = "cm,mdss-livedisplay-srgb-on-cmd"
	old_cabc_on = "qcom,mdss-dsi-dispparam-cabcon-command"
	old_cabc_off = "qcom,mdss-dsi-dispparam-cabcoff-command"
	new_cabc_on = "cm,mdss-livedisplay-cabc-cmd"
	new_cabc_off = "cm,mdss-livedisplay-cabc-post-cmd"
	old_cabc_sate = "qcom,mdss-dsi-dispparam-cabcon-command-state"
	old_cabc_sate_bis = "qcom,mdss-dsi-dispparam-cabcoff-command-state"
	new_cabc_state = "cm,mdss-livedisplay-command-state"
	state = ("state" in name) # We don't want dual link state
	if old_cabc_sate in name:
		return tmp.replace(old_cabc_sate,new_cabc_state)
	elif old_cabc_sate_bis in name:
		return tmp.replace(old_cabc_sate_bis,new_cabc_state)
	elif old_timing in name:
		return tmp.replace(old_timing,new_timing)
	elif (old_srgb in name) and not state:
		return tmp.replace(old_srgb,new_srgb)
	elif old_cabc_on in name and not state:
		return tmp.replace(old_cabc_on,new_cabc_on)
	elif old_cabc_off in name and not state:
		return tmp.replace(old_cabc_off,new_cabc_off)
	else: return name

# Make the dt recap struct
def getDTStruct(files):
	dt_seen = []
	ret = [x for x in range(len(xiaomi_dt))]
	for dt_file in files:
		cur_file = open(dt_file[:-1])
		lines = cur_file.readlines()
		cur_dt_seen = []
		cur_dt_buf = []
		cur_dt = -1
		dt_bool = False
		for line in lines:
			if dt_bool and ("}" in line): # Reset all dt data
				ret[cur_dt] = cur_dt_buf # Push buf to main struct
				cur_dt_seen = []
				cur_dt_buf = []
				cur_dt = -1
				dt_bool = False
			if any(x in line for x in xiaomi_dt) and ('{' in line) and ("@" not in line) and (getDTName(line) not in dt_seen): # Get cur dt
				tmp = getDTName(line)
				if tmp in xiaomi_dt:
					dt_bool = True
					cur_dt = getDTNum(tmp)
				dt_seen.append(tmp)
			elif (cur_dt != -1) and (dt_bool) and not any(x in line for x in blacklist): # Add entry
				if not any(x in line for x in ["cabc","srgb"]) and any(x in line for x in ["dispparam"]): continue
				tmp = getEntryTuple(line)
				if tmp[0] not in cur_dt_seen:
					cur_dt_buf.append((replaceName(tmp[0]).replace("\t",""),tmp[1]))
					cur_dt_seen.append(tmp[0])
		cur_file.close()
	return ret

# Get dt in a struct
def getDTsInStruct(struct, ind):
	for i in struct[ind]:
		if "qcom,mdss-dsi-dt-name" in i[0]: print i

# Print the structure
def printDTStruct(struct):
	for i in range(len(struct)):
		print "******* DT = " + xiaomi_dt[i] + " *******"
		for j in struct[i]:
			print convertToDecimal(j)

# Print a list verticaly
def printVerticaly(liste):
	for i in liste:
		if type(i) == tuple:
			print convertToDecimal(i)
		else:
			print i

# Get the sRGB OFF command
def getsRGBOff(dt,struct):
	on_cmd = 'qcom,mdss-dsi-on-command'
	cmd = '\t\tcm,mdss-livedisplay-srgb-off-cmd = [\n\t\t\t\t'
	for i in struct[dt]:
		if ("qcom,mdss-dsi-on-command" in i[0]) and ("state" not in i[0]): # We don't want state
			buf = i
			break
	tmp = convertToDecimal(buf)
	cmd += tmp[-136:] # Take 5 last lines (5*9 bytes)
	return cmd

# Returns if value exists
def isInStruct(dt,struct,entry):
		for i in struct[dt]:
			if entry in i[0]: return True
		return False

# Compare struct (struct1..struct2 with git syntax)
def compareDTStruct(struct1,struct2):
	cabc_ui = "cm,mdss-livedisplay-cabc-ui-value"
	cabc_image = "cm,mdss-livedisplay-cabc-image-value"
	cabc_video = "cm,mdss-livedisplay-cabc-video-value"
	print "**************** COMPARE STARTS ****************"
	for i in range(len(struct1)): # Both structs are same length
		# Reset entries
		entries1 = []
		entries2 = []
		diff_changed = []
		chk_diff_changed = []
		entries1 = [x for x in struct1[i]]
		entries2 = [x for x in struct2[i]]
		diff_changed = sorted(list(set(entries2) - set(entries1))) # Changed entries
		# Check blacklist
		for j in diff_changed:
			if not any(x in j[0] for x in blacklist):
					chk_diff_changed.append(j)
		if chk_diff_changed != []:
			print " **** DT = " + xiaomi_dt[i] + " *****"
			print "Changed/Missing"
			if not isInStruct(i,struct1,cabc_ui): print "\t\t" + cabc_ui + '= <0x01>;'
			if not isInStruct(i,struct1,cabc_image): print "\t\t" + cabc_image + '= <0x02>;'
			if not isInStruct(i,struct1,cabc_video): print "\t\t" + cabc_video + '= <0x03>;'
			if any("srgb" in x[0] for x in chk_diff_changed):
				if not isInStruct(i,struct1,"cm,mdss-livedisplay-srgb-off-cmd"): print getsRGBOff(i,struct1)
			printVerticaly(chk_diff_changed)

miui_struct = getDTStruct(dt_miui_files)
la_struct = getDTStruct(dt_la_files)
compareDTStruct(la_struct,miui_struct)
