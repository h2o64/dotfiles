import os

# Characterize each dump
def getBufSign(buf):
	begin = 0
	end = 0
	for i in range(len(buf)):
		if buf[i:i+21] == "kernel/xiaomi/msm8996":
			begin = i
		if (begin > 0) and (buf[i:i+1] == "\n"):
			return buf[begin:i]

# Open all dmesg
file_list = os.popen("ls").readlines()
dmesg_list = []
for i in file_list:
	if "dmesg" in i: dmesg_list.append(open(i[:-1]))

# Read all dmesg
ret = []
sign = []
buf = ''
for dmesg in dmesg_list:
	tmp = dmesg.readlines()
	tmp_bool = False
	for line in tmp:
		if "------------[ cut here ]------------" in line: tmp_bool = True
		if "---[ end trace" in line:
			sign.append(getBufSign(buf))
			buf += "-----------[ end trace ]-----------\n"
			ret.append(buf)
			buf = ''
			tmp_bool = False
		if tmp_bool: buf += line[15:] # Get line without timestamp

# Close all the dmesg
for dmesg in dmesg_list:
	dmesg.close()

# Filter the data and print
seen = []
for log in range(len(ret)):
	cur = sign[log]
	if cur not in seen:
		print ret[log]
		seen.append(cur)
