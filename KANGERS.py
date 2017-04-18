import sys
import os
import hashlib
import os

targets = ['app/imssettings/imssettings.apk',
'bin/ims_rtp_daemon',
'bin/imscmservice',
'bin/imsdatadaemon',
'bin/imsqmidaemon',
'etc/permissions/imscm.xml',
'etc/permissions/qti_permissions.xml',
'framework/imscmlibrary.jar',
'priv-app/ims/ims.apk',
'vendor/app/ims/ims.apk',
'vendor/lib64/lib-dplmedia.so',
'vendor/lib64/lib-imscamera.so',
'vendor/lib64/lib-imsdpl.so',
'vendor/lib64/lib-imsqimf.so',
'vendor/lib64/lib-imsrcs.so',
'vendor/lib64/lib-imsrcscm.so',
'vendor/lib64/lib-imsrcscmclient.so',
'vendor/lib64/lib-imsrcscmservice.so',
'vendor/lib64/lib-imss.so',
'vendor/lib64/lib-imsSDP.so',
'vendor/lib64/lib-imsvt.so',
'vendor/lib64/lib-imsxml.so',
'vendor/lib64/lib-rcsimssjni.so',
'vendor/lib64/lib-rcsjni.so',
'vendor/lib64/lib-rtpcommon.so',
'vendor/lib64/lib-rtpcore.so',
'vendor/lib64/lib-rtpdaemoninterface.so',
'vendor/lib64/lib-rtpsl.so',
'vendor/lib64/libimscamera_jni.so',
'vendor/lib64/libimsmedia_jni.so',
'vendor/lib64/libvcel.so',
'vendor/lib64/libvoice-svc.so',
'vendor/lib/lib-dplmedia.so',
'vendor/lib/lib-imscamera.so',
'vendor/lib/lib-imsdpl.so',
'vendor/lib/lib-imsqimf.so',
'vendor/lib/lib-imsrcs.so',
'vendor/lib/lib-imsrcscm.so',
'vendor/lib/lib-imsrcscmclient.so',
'vendor/lib/lib-imsrcscmservice.so',
'vendor/lib/lib-imss.so',
'vendor/lib/lib-imsSDP.so',
'vendor/lib/lib-imsvt.so',
'vendor/lib/lib-imsxml.so',
'vendor/lib/lib-rcsimssjni.so',
'vendor/lib/lib-rcsjni.so',
'vendor/lib/lib-rtpcommon.so',
'vendor/lib/lib-rtpcore.so',
'vendor/lib/lib-rtpdaemoninterface.so',
'vendor/lib/lib-rtpsl.so',
'vendor/lib/libimscamera_jni.so',
'vendor/lib/libimsmedia_jni.so',
'vendor/lib/libvcel.so',
'vendor/lib/libvoice-svc.so']
reference = ['9724cb142a363e10bf6d181ec4b51925', 'eda77940bb2249cd0415af3a7645e396', 'da92898bc7514cd87ce39970956b6e9d', '8cd026f97c52f07107515a86f421d5b4', 'e1ce57270df593d7b016765fba9d0705', '19d845ccdd11b3c48e04c39b3b5824c0', '29dbda7bf16753334925d2a86a7947f2', '8496eb98e6a729aaa6d09ffbfbbfff87', '975df0833e8f3beed75fd7cae773cec9', '73e5967464e024bfbb965671857a40c0', '0f608f75474e7d35cd61b43ebcf0b297', '4e8e211ea14b16bcb8ada3b58fc8608b', '38ca480857d261f706f7e891260f0c25', '32d31f72c61295d04437ef28f4f2ac54', 'a515a66c3d14374cbe5f9592f4804f2b', '65a378a0e096e2b06ebc1d1920aa42ca', 'acb45dc8e586264d9793c092fedd1a0b', '5f13c1cb6200f6c3cf96e75c577f8c19', '552f77848c93df710b890504c1e668e8', '5c1f9b4cfe941be7d9972eca6991b8cd', '39c208457bae6a1270c441dc22486d71', 'bc67c160af04c15a1f59b6e5c8885963', 'fe8165e012d3f490eabe020c5198fa26', 'fc69cf332d9e56e4f2a7a000cb12b3d7', 'f059f4611f18cf48b25506bc888af333', '74d32aec3a9b39ae3a2d455497894287', '89530addc26ec1482a0345662f3949be', 'e73c719f3c96e66cb0210179e58e0eed', '7fdc1191501cf0fdc4e6149e34c8ac90', '80841e57b2adbc13e749a00999a6d6ac']
reference += ['9724cb142a363e10bf6d181ec4b51925', 'dd91c6503a140a7a8bc3a397fc9a4df7', 'b9b172533a99c6cca6314bbc4a1a5853', '0f7fe6886b729c2d385bf11689ce6f64', 'c83847ab24116df53b0c6d94ca1c3290', '19d845ccdd11b3c48e04c39b3b5824c0', '29dbda7bf16753334925d2a86a7947f2', '47be2e5a0af1e991a6e926120fe1eb3f', '1ec3c548855aec3229da8aebf4e8e0e1', '1e79b43b44248c5dcf330c393b9bd448', 'f9e135f6129c5c31b71af491b75fdb7c', 'd200b25a11780b826e74f54d5e463a3d', '338f76293d6b8252f8c9c43fd757e0e0', '0d6deb8547ae8ff64afc3fe6cd10830f', '943fcba52eee15cfb7eb2c8377540aa5', '3df476d7b8b1cd0ffb10fafd1e2dd0cb', '81378af95d8375dd8f5766aed0654402', 'd8119e00e38cdf52016cc09ad69cfc4d', 'c7f2295197ea36bc3b23f9260bf95e05', 'b61f752f68ac25a9c613d29637adc7d5', '8c3768233e0fe90b966b1ce60e6fc040', '0b77b9fabba47d507560d0add5f0ad40', '295ef05e9f1add79c58faa715d885c44', 'acbb0288f6e30c5d80be0ba93613262c', '1004a90c10ec67358027c1b065ac270c', '163526a928cc017976ef964228bab79b', '6d5b7a1221fbddbf9fb01208e6da467f', 'c4aaaa25f3eef3e5b1d4d4eb0e915dff', '65bef3f8a705e3a63e11072505d5de7e', 'ea7c3b0cc41dd304f1d2f46a0620908f']
reference += ['9724cb142a363e10bf6d181ec4b51925', 'feb431637d128ed10b03659c0acdc1f3', 'ec4dd1408a5db32b3f525db6e4635e33', 'ef1085c45ed1ea697e8b7de37441ca70', '5545acdb5b952f3a170451c22af6ab8b', '19d845ccdd11b3c48e04c39b3b5824c0', '29dbda7bf16753334925d2a86a7947f2', '0591d3bf75a3761bb6c0de2ebdaf29f1', '294cce605fac471ac6a4cb98d7dd1501', '1b6911d2607be9f0a8aea6e70e20b993', '8a5bd1d0f2d642344085952bf4669701', '7f89fe51aa46dff2939722bd5b468b98', 'ea1837ea021e51d95154ce6aed34c393', '18010913e23773411fe2e1faee65e3f6', 'eb5f61e625a4e42bc635841e9901a390', 'c9b7ffcc075b04f468bf1835605a8f64', 'a38396f4bc1c8bcecd8486652a1610aa', '41d19fa399e7eb7383bbde03a74544e1', '433e8118659945f3420e4811a2acc7fd', '0e10eb5fa0629678e281eca2d1697276', 'e296882d11028c7cce860360bf9aa8e6', '3cf93a11563d4cdb21c288bc59c83aaf', '9d4ef7747da755e960151a549f231e1a', 'c2869fc63309813e34d6c4fa0eaea953', 'fab355703cf69ff867d786a982ac82ec', '16aa19e96688da8bdd111e2071def88c', '8089217282b6e3978730e5ef70ac075d', '7e5277fca908059223b59403c9d8fa9e', '46550f50f04a95c660a2b6dd88adf870', '6d907b45d0d9dfb97adf518a0c967c47']

def getmd5(filename):
    return hashlib.md5(open(filename,'rb').read()).hexdigest()

def list_md5(folder):
	md5list = []
	for filename in targets:
		path = folder + '/' + filename
		print path
		if os.path.isfile(path) : md5list.append(getmd5(path))
	return md5list

def compare(folder):
	for filename in targets:
		path = folder + '/' + filename
		if os.path.isfile(path) and getmd5(path) in reference : print 'Kang on ' + path + ' with ' + getmd5(path)

def exract(argv):
	extract_path = str(sys.argv[1]).replace('.zip','')
	os.popen('unzip ' + str(sys.argv[1]) + '-d ' + extract_path)
	os.popen('python sdat2img.py ' + extract_path + '/system.transfer.list ' + extract_path + '/system.new.dat ' + extract_path + '/system.img')
	os.popen('mkdir ' + extract_path + '/sys')
	os.popen('sudo mount -o loop ' + extract_path + '/system.img ' + extract_path + '/sys')
	compare(extract_path)

if __name__ == '__main__':
    extract(sys.argv)
