import os

# Xiaomi Panels
xiaomi_panels = [
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
'qcom,mdss_dsi_sharp_fte716_1080p_video']

# Get panel number
def getPanelNum(panel):
	for x in range(len(xiaomi_panels)):
		if panel in xiaomi_panels[x]: return x
	# print "Panel num can't be found : " + panel

# Convert their wierd format
def hexToDec(hexa):
	buf = ''
	count = 0
	# Remove "0x"
	for i in hexa:
		if count%2 == 0: buf += i.replace("0x","")
		else: buf += i.replace("0x","0")
		count += 1
	# Reset
	tmp = buf
	buf = ''
	# Filter
	for j in range(len(tmp)):
		if j%2 == 0: buf += " "
		buf += tmp[j]
	return buf[1:]

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
	hex_blacklist = ['qcom,mdss-dsi-underflow-color','qcom,mdss-dsi-t-clk-post','qcom,mdss-dsi-t-clk-pre','qcom,mdss-dsi-wr-mem-start','qcom,mdss-dsi-wr-mem-continue']
	# Empty value
	if (entry[1] == ''): return entry[0]
	# Regular string || Display ON/OFF CMD
	elif ('"' in entry[1]) or ('[' in entry[1]) or (entry[0] in hex_blacklist): return entry[0] + " = " + entry[1]
	# HEX-ed display CMD/Timing
	elif ("-command" in entry[0]) or ("-timings" in entry[0]):
		values = getValues(entry[1])
		buf = entry[0] + ' = ['
		buf += hexToDec(values)
		return buf + '];'
	# Reset sequence
	elif ("qcom,mdss-dsi-reset-sequence" in entry[0]):
		return entry[0] + " = " + formatReset(entry[1])
	# Hex to int
	else:
		values = getValues(entry[1])
		buf = entry[0] + ' = <'
		for i in values: buf += str(int(i,16)) + ' '
		return buf[:-1] + '>;'

# Get all the DT available
dt_miui_files = os.popen('find DTS/ -follow -type f | grep "dts"').readlines()
dt_la_files = os.popen('find DTS_LA/ -follow -type f | grep "dts"').readlines()

# Get panel name (qcom,*)
panel_entry = 'qcom,mdss_dsi_'
def getPanelName(string):
	for i in range(len(string)):
		if string[i] == ',': return string[i-4:-3]

# Get the entry tuple
def getEntryTuple(entry):
	for i in range(len(entry)):
		if entry[i] == '=': return (entry[2:i-1],entry[i+2:-1])
	return (entry[2:-1],'')

# Replace with correct name
def replaceName(name):
	old_timing = "qcom,mdss-dsi-panel-timings-8996"
	new_timing = "qcom,mdss-dsi-panel-timings-phy-v2"
	if old_timing in name:
		return new_timing
	else: return name

# Make the panel recap struct
def getPanelStruct(files):
	panel_seen = []
	ret = [x for x in range(len(xiaomi_panels))]
	blacklist = ["phandle","dispparam","qcom,config-select","qcom,mdss-dsi-displayo","qcom,mdss-night-brightness","qcom,panel-supply-entries","qcom,mdss-dsi-panel-model","qcom,video-panel-esd-te-check","qcom,mdss-panel-on-dimming-delay","qcom,esd-err-irq-gpio"]
	for dt_file in files:
		cur_dt = open(dt_file[:-1])
		lines = cur_dt.readlines()
		cur_panel_seen = []
		cur_panel_buf = []
		cur_panel = -1
		panel_bool = False
		for line in lines:
			if panel_bool and ("}" in line): # Reset all panel data
				ret[cur_panel] = cur_panel_buf # Push buf to main struct
				cur_panel_seen = []
				cur_panel_buf = []
				cur_panel = -1
				panel_bool = False
			if (panel_entry in line) and ('{' in line) and ("@" not in line) and (getPanelName(line) not in panel_seen): # Get cur panel
				tmp = getPanelName(line)
				if tmp in xiaomi_panels:
					panel_bool = True
					cur_panel = getPanelNum(tmp)
				panel_seen.append(tmp)
			elif (cur_panel != -1) and (panel_bool) and not any(x in line for x in blacklist): # Add entry
				tmp = getEntryTuple(line)
				if tmp[0] not in cur_panel_seen:
					cur_panel_buf.append((replaceName(tmp[0]),tmp[1]))
					cur_panel_seen.append(tmp[0])
		cur_dt.close()
	return ret

# Get panels in a struct
def getPanelsInStruct(struct, ind):
	for i in struct[ind]:
		if "qcom,mdss-dsi-panel-name" in i[0]: print i

# Print the structure
def printPanelStruct(struct):
	for i in range(len(struct)):
		print "******* Panel = " + xiaomi_panels[i] + " *******"
		for j in struct[i]:
			print convertToDecimal(j).replace("\t","")

# Print a list verticaly
def printVerticaly(liste):
	for i in liste:
		if type(i) == tuple:
			print convertToDecimal(i).replace("\t","")
		else:
			print i

# Compare struct (struct1..struct2 with git syntax)
def comparePanelStruct(struct1,struct2):
	print "**************** COMPARE STARTS ****************"
	for i in range(len(struct1)): # Both structs are same length
		# Reset entries
		entries1 = []
		entries2 = []
		names1 = []
		names2 = []
		diff_added = []
		diff_changed = []
		print " **** Panel = " + xiaomi_panels[i] + " *****"
		entries1 = [x for x in struct1[i]]
		entries2 = [x for x in struct2[i]]
		names1 = sorted(list(set([tmp[0] for tmp in entries1])))
		names2 = sorted(list(set([tmp[0] for tmp in entries2])))
		diff_added = sorted(list(set(names1) - set(names2))) # Added entries
		diff_changed = sorted(list(set(entries2) - set(entries1))) # Changed entries
		if diff_added != []:
			print "Added ++ (1..2)"
			printVerticaly(diff_added)
		if diff_changed != []:
			print "Changed/Missing"
			printVerticaly(diff_changed)


miui_struct = getPanelStruct(dt_miui_files)
la_struct = getPanelStruct(dt_la_files)
comparePanelStruct(la_struct,miui_struct)







#
