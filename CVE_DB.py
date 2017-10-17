CVE_DB = [
('CVE-2012-6657', 'net: guard tcp_set_keepalive() to tcp sockets', 3.04),
('CVE-2012-6689', 'netlink: fix possible spoofing from non-root processes', 3.04),
('CVE-2012-6703', 'ALSA: compress: fix compilation error', 3.04),
('CVE-2012-6704', 'net: cleanups in sock_setsockopt()', 3.04),
('CVE-2013-2015', 'ext4: avoid hang when mounting non-journal filesystems with orphan list', 3.04),
('CVE-2013-4312', 'pipe: limit the per-user amount of pages allocated in pipes', 3.04),
('CVE-2014-0196', 'enrc2b:squash commits from grouper', 3.04),
('CVE-2014-0206', 'aio: fix kernel memory disclosure in io_getevents() introduced in v3.10', 3.04),
('CVE-2014-1739', 'media-device: fix infoleak in ioctl media_enum_entities()', 3.04),
('CVE-2014-2523', 'netfilter: nf_conntrack_dccp: fix skb_header_pointer API usages', 3.04),
('CVE-2014-2706', 'mac80211: fix AP powersave TX vs. wakeup race', 3.04),
('CVE-2014-2851', 'net: ipv4: current group_info should be put after using.', 3.04),
('CVE-2014-3145', 'filter: prevent nla extensions to peek beyond the end of the message', 3.04),
('CVE-2014-4323', 'Validate input arguments from user space', 3.04),
('CVE-2014-4655', 'ALSA: control: Fix replacing user controls', 3.04),
('CVE-2014-4656', 'ALSA: control: Make sure that id->index does not overflow', 3.04),
('CVE-2014-4943', "net/l2tp: don't fall back on UDP [get|set]sockopt", 3.04),
('CVE-2014-5206', 'mnt: Only change user settable mount flags in remount', 3.04),
('CVE-2014-7822', 'splice: Apply generic position and size checks to each write', 3.04),
('CVE-2014-7825', "tracing/syscalls: Ignore numbers outside NR_syscalls' range", 3.04),
('CVE-2014-7826', "tracing/syscalls: Ignore numbers outside NR_syscalls' range", 3.04),
('CVE-2014-7970', 'vfs: new internal helper: mnt_has_parent(mnt)', 3.04),
('CVE-2014-8160', 'netfilter: conntrack: disable generic tracking for known protocols', 3.04),
('CVE-2014-8173', 'mm: Fix NULL pointer dereference in madvise(MADV_WILLNEED) support', 3.04),
('CVE-2014-8709', 'mac80211: fix fragmentation code, particularly for encryption', 3.04),
('CVE-2014-9420', 'isofs: Fix infinite looping over CE entries', 3.04),
('CVE-2014-9529', 'KEYS: close race between key lookup and freeing', 3.04),
('CVE-2014-9683', 'eCryptfs: Remove buggy and unnecessary write in file name decode routine', 3.04),
('CVE-2014-9715', 'netfilter: nf_conntrack: reserve two bytes for nf_ct_ext->len', 3.04),
('CVE-2014-9731', 'udf: Check path length when reading symlink', 3.04),
('CVE-2014-9777', 'PYTHON-CVE : Commit not found'),
('CVE-2014-9778', 'msm: vidc: Validate userspace buffer count', 3.04),
('CVE-2014-9782', 'msm: camera: Fix various small issues in Actuator driver', 3.04),
('CVE-2014-9783', 'msm: camera: Fix various small issues in cci driver', 3.04),
('CVE-2014-9786', 'msm: actuator: fix to prevent kernel heap buffer overflow', 3.04),
('CVE-2014-9787', 'Revert "qseecom: Validate the incoming length from user space"', 3.04),
('CVE-2014-9788', 'ASoC: msm: qdsp6v2: Fix buffer overflow in voice driver', 3.04),
('CVE-2014-9790', 'mmc: core : fix arbitrary read/write to user space', 3.04),
('CVE-2014-9866', 'msm: camera: Bound check num_cid from userspace in csid driver', 3.04),
('CVE-2014-9867', 'msm:camera: Fix multiple bounds check', 3.04),
('CVE-2014-9869', 'msm: camera: isp: Bound check for number stats registers', 3.04),
('CVE-2014-9870', 'ARM: 7735/2: Preserve the user r/w register TPIDRURW on context switch and fork', 3.04),
('CVE-2014-9876', 'diag: Fix possible underflow/overflow issues', 3.04),
('CVE-2014-9878', 'mmc: card: fix arbitrary write via read handler in mmc_block_test', 3.04),
('CVE-2014-9880', 'msm: vidc: Check validity of userspace address', 3.04),
('CVE-2014-9882', 'radio: iris: Use kernel API to copy data from user space', 3.04),
('CVE-2014-9888', "ARM: dma-mapping: don't allow DMA mappings to be marked executable", 3.1),
('CVE-2014-9890', 'msm: camera: Update CCI WR comamnd buffer size to 11 bytes', 3.04),
('CVE-2014-9892', 'ALSA: compress: Memset timestamp structure to zero.', 3.04),
('CVE-2014-9895', 'media: Revert "Init the reserved fields of struct media_link_desc"', 3.04),
('CVE-2014-9900', 'net: Zeroing the structure ethtool_wolinfo in ethtool_get_wol()', 3.1),
('CVE-2014-9903', 'sched: Fix information leak in sys_sched_getattr()', 3.1),
('CVE-2014-9904', 'ALSA: compress: fix compilation error', 3.04),
('CVE-2014-9922', 'msm: vidc: Check validity of userspace address', 3.04),
('CVE-2014-9940', 'regulator: core: Fix regualtor_ena_gpio_free not to access pin after freeing', 3.04),
('CVE-2015-0569', 'wlan: Address buffer overflow due to invalid length', 3.04),
('CVE-2015-0571', 'wlan:Check priviledge permission for SET_THREE_INT_GET_NONE', 3.04),
('CVE-2015-1420', 'vfs: read file_handle only once in handle_to_path', 3.04),
('CVE-2015-1465', 'misc: Revert some changes from SM-G900F kernel source import', 3.04),
('CVE-2015-1534', 'android: drivers: workaround debugfs race in binder', 3.04),
('CVE-2015-1805', 'pipe: iovec: Fix memory corruption when retrying atomic copy as non-atomic', 3.04),
('CVE-2015-2041', 'net: llc: use correct size for sysctl timeout entries', 3.04),
('CVE-2015-2686', 'net: validate the range we feed to iov_iter_init() in sys_sendto/sys_recvfrom', 3.04),
('CVE-2015-2922', "ipv6: Don't reduce hop limit for an interface", 3.04),
('CVE-2015-3288', 'mm: avoid setting up anonymous pages into file mapping', 3.04),
('CVE-2015-3339', 'fs: take i_mutex during prepare_binprm for set[ug]id executables', 3.04),
('CVE-2015-3636', 'ipv4: Missing sk_nulls_node_init() in ping_unhash().', 3.04),
('CVE-2015-4170', 'tty: Fix hang at ldsem_down_read()', 3.1),
('CVE-2015-4177', 'mnt: Fail collect_mounts when applied to unmounted mounts', 3.04),
('CVE-2015-5366', 'udp: fix behavior of wrong checksums', 3.04),
('CVE-2015-5697', 'md: use kzalloc() when bitmap is disabled', 3.04),
('CVE-2015-5707', "sg_start_req(): make sure that there's not too many elements in iovec", 3.04),
('CVE-2015-7509', 'ext4: make orphan functions be no-op in no-journal mode', 3.04),
('CVE-2015-7515', 'isofs: Fix infinite looping over CE entries', 3.04),
('CVE-2015-7550', 'KEYS: Fix race between read and revoke', 3.04),
('CVE-2015-7872', 'KEYS: Fix handling of stored error in a negatively instantiated user key', 3.04),
('CVE-2015-8019', '[stable,<=,3.18] net: add length argument to skb_copy_and_csum_datagram_iovec', 3.04),
('CVE-2015-8215', 'ipv6: addrconf: validate new MTU before applying it', 3.04),
('CVE-2015-8539', 'KEYS: Fix handling of stored error in a negatively instantiated user key', 3.04),
('CVE-2015-8543', 'net: add validation for the socket syscall protocol argument', 3.04),
('CVE-2015-8575', 'Revert "bluetooth: Validate socket address length in sco_sock_bind()."', 3.04),
('CVE-2015-8785', 'fuse: break infinite loop in fuse_fill_write_pages()', 3.04),
('CVE-2015-8830', 'vfs: make AIO use the proper rw_verify_area() area helpers', 3.04),
('CVE-2015-8839', 'fs: ext4: disable support for fallocate FALLOC_FL_PUNCH_HOLE', 3.04),
('CVE-2015-8937', 'diag: Make fixes to diag_switch_logging', 3.1),
('CVE-2015-8940', 'ASoC: q6lsm: Add check for integer overflow', 3.04),
('CVE-2015-8942', 'msm: cpp: Update iommu handling', 3.1),
('CVE-2015-8944', 'kernel: Restrict permissions of /proc/iomem.', 3.04),
('CVE-2015-8951', 'ASoC: msm-lsm-client: free lsm client data in msm_lsm_close', 3.04),
('CVE-2015-8955', 'ARM: perf: reject groups spanning multiple hardware PMUs', 3.04),
('CVE-2015-8962', 'sg: Fix double-free when drives detach during SG_IO', 3.04),
('CVE-2015-8963', 'Revert "perf: Fix race in swevent hash"', 3.04),
('CVE-2015-8964', 'aio: mark AIO pseudo-fs noexec', 3.04),
('CVE-2015-8966', 'Revert "msm8960_jbbl: Build the kernel with gcc-4.9"', 3.04),
('CVE-2015-8967', 'arm64: make sys_call_table const', 3.1),
('CVE-2015-9004', 'perf: Tighten (and fix) the grouping condition', 3.04),
('CVE-2016-0723', 'tty: Fix unsafe ldisc reference via ioctl(TIOCGETD)', 3.04),
('CVE-2016-0728', 'KEYS: Fix keyring ref leak in join_session_keyring()', 3.1),
('CVE-2016-0758', 'KEYS: Fix ASN.1 indefinite length object parsing', 3.1),
('CVE-2016-0774', 'pipe: iovec: Fix OOB read in pipe_read()', 3.04),
('CVE-2016-0805', 'msm: perf: Protect buffer overflow due to malicious user', 3.04),
('CVE-2016-0806', 'wlan:Check priviledge permission for SET_CHANNEL_RANGE', 3.04),
('CVE-2016-0819', 'perf: duplicate deletion of perf event', 3.04),
('CVE-2016-0821', 'include/linux/poison.h: fix LIST_POISON{1,2} offset', 3.04),
('CVE-2016-0823', 'pagemap: do not leak physical addresses to non-privileged userspace', 3.04),
('CVE-2016-10044', 'aio: mark AIO pseudo-fs noexec', 3.04),
('CVE-2016-10088', 'sg_write()/bsg_write() is not fit to be called under KERNEL_DS', 3.04),
('CVE-2016-10153', 'ext4: fix NULL pointer dereference when journal restart fails', 3.04),
('CVE-2016-10200', 'l2tp: fix racy SOCK_ZAPPED flag check in l2tp_ip{,6}_bind()', 3.04),
('CVE-2016-10208', 'ext4: fix fencepost in s_first_meta_bg validation', 3.04),
('CVE-2016-10229', 'udp: properly support MSG_PEEK with truncated buffers', 3.04),
('CVE-2016-10230', 'qcrypto: protect potential integer overflow.', 3.04),
('CVE-2016-10232', 'msm: mdss: Correct the format specifiers in sscanf function', 3.04),
('CVE-2016-10233', 'msm-camera: Addressing possible overflow conditions', 3.04),
('CVE-2016-10234', 'msm: ipa: fix ioctl input param validation', 3.04),
('CVE-2016-10235', 'qcacld-2.0: Fix VHT-80 IBSS stops beaconing', 3.04),
('CVE-2016-10283', 'prima: Trim operation classes to max supported in change station', 3.04),
('CVE-2016-10285', 'msm: mdss: handle synchronization issues during DSI debugfs read/write', 3.18),
('CVE-2016-10286', 'msm: mdss: avoid removing wrong multirect on validate failures', 3.18),
('CVE-2016-10287', 'ASoC: msm: qdsp6v2: completely deallocate on cal block creation failure', 3.1),
('CVE-2016-10288', 'leds: qpnp-flash: Fix Use-after-free(UAF) for debugfs', 3.18),
('CVE-2016-10289', 'crypto: msm: check length before copying to buf in _debug_stats_read', 3.04),
('CVE-2016-10290', 'uio: fix potential use after free issue when accessing debug_buffer [2/2]', 3.1),
('CVE-2016-10294', 'power: qpnp-fg: Fix possible race condition in FG debugfs', 3.1),
('CVE-2016-10295', 'leds: qpnp-flash: Fix possible race condition in debugfs', 3.18),
('CVE-2016-1583', 'ecryptfs: forbid opening files without mmap handler', 3.04),
('CVE-2016-2053', 'ASN.1: Fix non-match detection failure on data overrun', 3.04),
('CVE-2016-2059', 'ashmem: Validate ashmem memory with fops pointer', 3.04),
('CVE-2016-2061', 'msm: camera: isp: Fix warning and errors based on static analysis', 3.04),
('CVE-2016-2066', 'ASoC: msm: audio-effects: fix stack overread and heap overwrite', 3.04),
('CVE-2016-2068', 'ASoC: msm: audio-effects: misc fixes in h/w accelerated effect', 3.04),
('CVE-2016-2184', 'ALSA: usb-audio: Fix double-free in error paths after snd_usb_add_audio_stream() call', 3.04),
('CVE-2016-2185', 'Input: ati_remote2 - fix crashes on detecting device with invalid descriptor', 3.04),
('CVE-2016-2186', 'Input: powermate - fix oops with malicious USB descriptors', 3.04),
('CVE-2016-2187', 'Input: gtco - fix crash on detecting device without endpoints', 3.04),
('CVE-2016-2188', 'USB: iowarrior: fix oops with malicious USB descriptors', 3.04),
('CVE-2016-2384', 'ALSA: usb-audio: avoid freeing umidi object twice', 3.04),
('CVE-2016-2465', 'msm: mdss: fix possible out-of-bounds and overflow issue in mdp debugfs', 3.04),
('CVE-2016-2468', 'msm: kgsl: Add missing checks for alloc size and sglen', 3.04),
('CVE-2016-2475', 'net: wireless: bcmdhd: check privilege on priv cmd', 3.04),
('CVE-2016-2488', 'Revert "msm: camera: ispif: Validate VFE num input during reset"', 3.04),
('CVE-2016-2503', 'msm: kgsl: Avoid race condition in ioctl_syncsource_destroy', 3.04),
('CVE-2016-2504', 'msm: kgsl: Avoid race condition in ioctl_syncsource_destroy', 3.04),
('CVE-2016-2544', 'ALSA: seq: Fix race at timer setup and close', 3.04),
('CVE-2016-2545', 'ALSA: timer: Fix double unlink of active_list', 3.04),
('CVE-2016-2546', 'ALSA: timer: Fix race among timer ioctls', 3.04),
('CVE-2016-2547', 'ALSA: timer: Harden slave timer list handling', 3.04),
('CVE-2016-2549', 'ALSA: hrtimer: Fix stall by hrtimer_cancel()', 3.04),
('CVE-2016-2847', 'pipe: limit the per-user amount of pages allocated in pipes', 3.04),
('CVE-2016-3070', 'netfilter: x_tables: check for size overflow', 3.04),
('CVE-2016-3134', 'netfilter: x_tables: fix unconditional helper', 3.04),
('CVE-2016-3135', 'netfilter: x_tables: check for size overflow', 3.04),
('CVE-2016-3136', 'USB: mct_u232: add sanity checking in probe', 3.04),
('CVE-2016-3137', 'USB: cypress_m8: add endpoint sanity check', 3.04),
('CVE-2016-3138', 'USB: cdc-acm: more sanity checking', 3.04),
('CVE-2016-3140', 'USB: digi_acceleport: do sanity checking for the number of ports', 3.04),
('CVE-2016-3156', "ipv4: Don't do expensive useless work during inetdev destroy.", 3.04),
('CVE-2016-3689', 'Input: ims-pcu - sanity check against missing interfaces', 3.1),
('CVE-2016-3768', 'msm: perf: Do not allocate new hw_event if event is duplicate.', 3.04),
('CVE-2016-3775', 'PYTHON-CVE : Commit not found'),
('CVE-2016-3809', 'Replace %p with %pK to prevent leaking kernel address', 3.04),
('CVE-2016-3813', 'USB: dwc3: debugfs: Add boundary check in dwc3_store_ep_num()', 3.04),
('CVE-2016-3843', 'oneplus2: defconfig: Enable CONFIG_SECURITY_PERF_EVENTS_RESTRICT', 3.04),
('CVE-2016-3857', 'arm: oabi compat: add missing access checks', 3.04),
('CVE-2016-3859', 'Adds bound check on reg_cfg_cmd->u.dmi_info.hi_tbl_offset.', 3.04),
('CVE-2016-3865', 'input: synaptics: allocate heap memory for temp buf', 3.04),
('CVE-2016-3866', 'ASoC: msm: qdsp6v2: check param length for EAC3 format (CVE-2016-3866)', 3.04),
('CVE-2016-3867', 'msm: ipa: fix potential race condition ioctls', 3.04),
('CVE-2016-3893', 'ASoC: wcd9xxx: Fix unprotected userspace access', 3.04),
('CVE-2016-3894', 'msm : dma_test: Initialize newly allocated memory', 3.04),
('CVE-2016-3902', 'msm: ipa: handle information leak on ADD_FLT_RULE_INDEX ioctl', 3.1),
('CVE-2016-3903', 'msm: camera: sensor: Fix use after free condition', 3.04),
('CVE-2016-3904', 'msm: msm_bus: limit max chars read by sscanf', 3.18),
('CVE-2016-3906', 'msm-core: debug: Update the number of supported pstates.', 3.1),
('CVE-2016-3907', 'misc: qcom: qdsp6v2: initialize wma_config_32', 3.1),
('CVE-2016-3931', 'qseecom: validate the inputs of __qseecom_send_modfd_resp', 3.04),
('CVE-2016-3934', 'msm: camera: restructure data handling to be more robust', 3.04),
('CVE-2016-3935', 'msm: crypto: Fix integer over flow check in qcedev driver', 3.04),
('CVE-2016-3951', 'usbnet: cleanup after bind() in probe()', 3.04),
('CVE-2016-4470', 'KEYS: potential uninitialized variable', 3.04),
('CVE-2016-4482', 'USB: usbfs: fix potential infoleak in devio', 3.04),
('CVE-2016-4486', 'fix infoleak in rtnetlink', 3.04),
('CVE-2016-4569', 'ALSA: timer: Fix leak in SNDRV_TIMER_IOCTL_PARAMS', 3.04),
('CVE-2016-4578', 'ALSA: timer: Fix leak in events via snd_timer_user_ccallback', 3.04),
('CVE-2016-4794', 'percpu: fix synchronization between chunk->map_extend_work and chunk destruction', 3.18),
('CVE-2016-4805', 'ppp: defer netns reference release for ppp channel', 3.04),
('CVE-2016-4998', 'netfilter: x_tables: validate e->target_offset early', 3.04),
('CVE-2016-5195', 'mm: remove gup_flags FOLL_WRITE games from __get_user_pages()', 3.04),
('CVE-2016-5340', 'ashmem: Validate ashmem memory with fops pointer', 3.04),
('CVE-2016-5342', 'wcnss: Avoid user buffer overloading for write cal data', 3.04),
('CVE-2016-5343', 'drivers: soc: Add buffer overflow check for svc send request', 3.04),
('CVE-2016-5345', 'radio-iris: check argument values before copying the data', 3.1),
('CVE-2016-5346', 'net: ipc_router: fix NULL pointer de-reference issue', 3.04),
('CVE-2016-5347', 'ASoC: soc: msm: initialize buffer to prevent kernel data leakage', 3.04),
('CVE-2016-5829', 'HID: hiddev: validate num_values for HIDIOCGUSAGES, HIDIOCSUSAGES commands', 3.04),
('CVE-2016-5853', 'ASoC: msm: qdsp6v2: DAP: Add check to validate param length', 3.1),
('CVE-2016-5856', 'spcom: check buf_size validity for user send command', 3.18),
('CVE-2016-5857', 'spcom: check buf size for send modified command', 3.18),
('CVE-2016-5858', 'ASoC: wcd9330: Fix out of bounds for mad input value', 3.04),
('CVE-2016-5859', 'ASoC: msm: qdsp6v2: DAP: Add check to validate param length', 3.04),
('CVE-2016-5860', 'drivers: soc: qcom: Add overflow check for sound model size', 3.18),
('CVE-2016-5861', 'msm: mdss: Add sanity check for Gamut LUT size', 3.1),
('CVE-2016-5863', 'hid: usbhid: Changes to prevent buffer overflow', 3.04),
('CVE-2016-5867', 'ASoC: msm: qdsp6v2: DAP: Add check to validate param length', 3.04),
('CVE-2016-5868', 'msm: rndis_ipa: Remove rndis_ipa loopback functionality', 3.1),
('CVE-2016-5870', 'net: ipc_router: fix NULL pointer de-reference issue', 3.04),
('CVE-2016-6136', 'audit: fix a double fetch in audit_log_single_execve_arg()', 3.04),
('CVE-2016-6672', 'synaptics: elevation of privilege vulnerability', 3.04),
('CVE-2016-6679', 'wlan: Remove the support for setwpaie ioctl', 3.04),
('CVE-2016-6680', 'qcacld-2.0: Remove the support for iw_set_priv ioctl', 3.04),
('CVE-2016-6683', 'ANDROID: binder: Clear binder and cookie when setting handle in flat binder struct', 3.04),
('CVE-2016-6698', 'misc: qcom: qdsp6v2: initialize config_32', 3.1),
('CVE-2016-6725', 'msm: crypto: Fix integer over flow check in qcrypto driver', 3.04),
('CVE-2016-6728', 'ion: disable system contig heap', 3.04),
('CVE-2016-6738', 'qcedev: Validate Source and Destination addresses', 3.04),
('CVE-2016-6740', 'msm: sensor: Avoid potential stack overflow', 3.04),
('CVE-2016-6741', 'Add I2C_REG_DATA_MAX for size param validation', 3.04),
('CVE-2016-6742', 'input: synaptics: Do not allow sysfs to run in suspend', 3.04),
('CVE-2016-6745', 'input: synaptics: prevent sysfs races', 3.04),
('CVE-2016-6748', 'msm: vidc: use %pK instead of %p which respects kptr_restrict sysctl', 3.04),
('CVE-2016-6749', 'msm: kgsl: Check the address range before mapping to GPU', 3.04),
('CVE-2016-6750', 'Revert "soc: qcom: smp2p: Fix kernel address leak"', 3.04),
('CVE-2016-6751', 'ASoC: msm: initialize the params array before using it', 3.04),
('CVE-2016-6752', 'qseecom: Change format specifier %p to %pK', 3.04),
('CVE-2016-6753', 'cgroup: prefer %pK to %p', 3.04),
('CVE-2016-6755', 'Revert erroneous "staging/android/ion: fix a race condition in the ion driver"', 3.04),
('CVE-2016-6756', 'msm: camera: cpp: Add validation for v4l2 ioctl arguments', 3.04),
('CVE-2016-6757', 'msm: mdss: hide kernel addresses from unprevileged users', 3.04),
('CVE-2016-6786', "lockdep: Silence warning if CONFIG_LOCKDEP isn't set", 3.04),
('CVE-2016-6787', 'perf: protect group_leader from races that cause ctx double-free', 3.04),
('CVE-2016-6791', 'ASoC: msm: lock read/write when add/free audio ion memory', 3.04),
('CVE-2016-6828', 'tcp: fix use after free in tcp_xmit_retransmit_queue()', 3.04),
('CVE-2016-7042', 'KEYS: Fix short sprintf buffer in /proc/keys show function', 3.04),
('CVE-2016-7097', 'tmpfs: clear S_ISGID when setting posix ACLs', 3.04),
('CVE-2016-7117', 'net: Fix use after free in the recvmmsg exit path', 3.04),
('CVE-2016-7910', 'block: fix use-after-free in seq file', 3.04),
('CVE-2016-7911', 'block: fix use-after-free in sys_ioprio_get()', 3.04),
('CVE-2016-7914', "assoc_array: don't call compare_object() on a node", 3.04),
('CVE-2016-7915', 'HID: core: prevent out-of-bound readings', 3.04),
('CVE-2016-7916', "proc: prevent accessing /proc/<PID>/environ until it's ready", 3.04),
('CVE-2016-7917', 'netfilter: nfnetlink: correctly validate length of batch messages', 3.18),
('CVE-2016-8391', 'ASoC: msm: lock read/write when add/free audio ion memory', 3.04),
('CVE-2016-8393', 'input: synaptics: add bounds checks for firmware id', 3.04),
('CVE-2016-8399', 'net: ping: check minimum size on ICMP header length', 3.04),
('CVE-2016-8403', 'Squashed merge of %p -> %pK fixes', 3.04),
('CVE-2016-8405', 'fbcmap: Remove unnecessary condition check', 3.04),
('CVE-2016-8410', 'qdsp6v2: blacklist %p kptr_restrict', 3.04),
('CVE-2016-8412', 'Adding mutex for actuator power down operations', 3.1),
('CVE-2016-8413', 'msm: cpp: Fix for buffer overflow in cpp.', 3.04),
('CVE-2016-8414', 'qcom: scm: remove printing input arguments', 3.1),
('CVE-2016-8417', 'msm: camera: fix bound check of offset to avoid overread overwrite', 3.04),
('CVE-2016-8418', 'msm: crypto: Fix integer over flow check in qce driver', 3.04),
('CVE-2016-8434', 'Revert "msm: kgsl: fix sync file error handling"', 3.04),
('CVE-2016-8436', 'ASoC: msm: set pointers to NULL after kfree', 3.04),
('CVE-2016-8450', 'ASoC: msm: set pointers to NULL after kfree', 3.04),
('CVE-2016-8452', 'qcacld-2.0: Use heap memory for station_info instead of stack', 3.04),
('CVE-2016-8453', 'net: wireless: bcmdhd: remove unnecessary PCIe memory access when BUS down.', 3.1),
('CVE-2016-8458', 'input: synaptics_dsx: add update bounds checks.', 3.04),
('CVE-2016-8476', 'qcacld-2.0: Validate "set passpoint list" network count', 3.1),
('CVE-2016-8477', 'msm: camera: sensor: Validate eeprom_name string length', 3.04),
('CVE-2016-8479', "msm: kgsl: Reserve a context ID slot but don't populate immediately", 3.04),
('CVE-2016-8480', 'qseecom: remove entry from qseecom_registered_app_list', 3.04),
('CVE-2016-8483', 'msm-core: use get_user() API to read userspace data/settings', 3.1),
('CVE-2016-8650', '[DO NOT SUBMIT] angler: Squash of March kernel updates for testing', 3.04),
('CVE-2016-8655', 'packet: fix race condition in packet_set_ring', 3.04),
('CVE-2016-9191', 'sysctl: Drop reference added by grab_header in proc_sys_readdir', 3.18),
('CVE-2016-9555', 'sctp: validate chunk len before actually using it', 3.04),
('CVE-2016-9576', 'splice: introduce FMODE_SPLICE_READ and FMODE_SPLICE_WRITE', 3.04),
('CVE-2016-9604', "KEYS: Disallow keyrings beginning with '.' to be joined as session keyrings", 3.04),
('CVE-2016-9754', 'ring-buffer: Prevent overflow of size in ring_buffer_resize()', 3.04),
('CVE-2016-9793', 'net: cleanups in sock_setsockopt()', 3.04),
('CVE-2016-9794', 'ALSA: pcm : Call kill_fasync() in stream lock', 3.04),
('CVE-2016-9806', 'netlink: add reference of module in netlink_dump_start', 3.04),
('CVE-2017-0403', "perf: don't leave group_entry on sibling list (use-after-free)", 3.04),
('CVE-2017-0404', 'ALSA: info: Check for integer overflow in snd_info_entry_write()', 3.04),
('CVE-2017-0427', 'fs/proc/array.c: make safe access to group_leader', 3.04),
('CVE-2017-0430', 'Revert "net: wireless: bcmdhd: fix use-after-free in _dhd_pno_get_for_batch()"', 3.04),
('CVE-2017-0434', 'input: synaptics_dsx: reallocate buffer under lock.', 3.18),
('CVE-2017-0435', 'drivers: qcom: ultrasound: Lock async driver calls', 3.04),
('CVE-2017-0436', 'drivers: qcom: ultrasound: Lock async driver calls', 3.04),
('CVE-2017-0451', 'drivers: soc: add size checks and update log messages', 3.04),
('CVE-2017-0452', 'msm: vidc: WARN_ON() reveals fuction addresses', 3.1),
('CVE-2017-0453', 'qcacld-2.0: Add buf len check in wlan_hdd_cfg80211_testmode', 3.04),
('CVE-2017-0457', 'msm: ADSPRPC: Buffer length to be copied is truncated', 3.04),
('CVE-2017-0460', 'net: rmnet_data: Fix incorrect netlink handling', 3.04),
('CVE-2017-0461', 'prima: Fix array out-of-bounds & integer underflow in _iw_set_genie', 3.04),
('CVE-2017-0463', 'net: ipc_router: Register services only on client port', 3.04),
('CVE-2017-0464', 'qcacld-2.0: Remove obsolete set/reset ssid hotlist', 3.1),
('CVE-2017-0465', 'msm: ADSPRPC: Check for buffer overflow condition', 3.1),
('CVE-2017-0507', 'ANDROID: ion: check for kref overflow', 3.04),
('CVE-2017-0509', 'net: wireless: bcmdhd: remove unsed WEXT file.', 3.04),
('CVE-2017-0510', 'android: fiq_debugger: restrict access to critical commands.', 3.04),
('CVE-2017-0516', 'input: misc: fix heap overflow issue in hbtp_input.c', 3.04),
('CVE-2017-0518', 'PYTHON-CVE : Commit not found'),
('CVE-2017-0519', 'PYTHON-CVE : Commit not found'),
('CVE-2017-0520', 'msm: crypto: fix issues on digest buf and copy_from_user in qcedev.c', 3.04),
('CVE-2017-0521', 'msm: cpp: Fix for integer overflow in cpp', 3.04),
('CVE-2017-0524', 'input: synaptics: put offset checks under mutex.', 3.04),
('CVE-2017-0525', 'apq8084: ipa: remove redundant NULL pointer check', 3.04),
('CVE-2017-0531', 'ASoC: msm-lsm-client: cleanup ioctl functions', 3.1),
('CVE-2017-0536', 'input: synaptics: put offset checks under mutex.', 3.04),
('CVE-2017-0564', 'ion: blacklist %p kptr_restrict', 3.04),
('CVE-2017-0574', 'PYTHON-CVE : Commit not found'),
('CVE-2017-0575', 'PYTHON-CVE : Commit not found'),
('CVE-2017-0576', 'crypto: msm: check integer overflow on total data len in qcedev.c', 3.04),
('CVE-2017-0583', 'ARM64: configs: Disable unwanted configs', 3.04),
('CVE-2017-0584', 'qcacld-2.0: Do not copy buffer to user-space if diag read fails', 3.1),
('CVE-2017-0586', 'ASoC: msm: qdsp6v2: Fix out-of-bounds access in put functions', 3.04),
('CVE-2017-0604', 'bcl: fix allocation for BCL attribute', 3.1),
('CVE-2017-0605', 'trace: resolve stack corruption due to string copy', 3.04),
('CVE-2017-0606', 'drivers: soc: add mutex to prevent response being processed twice', 3.04),
('CVE-2017-0607', 'ASoC: msm: q6dspv2: use correct variable type to store ION buff size', 3.04),
('CVE-2017-0608', 'ASoC: msm: qdsp6v2: Add range checking in msm_dai_q6_set_channel_map', 3.04),
('CVE-2017-0609', 'ASoC: msm-cpe-lsm: cleanup ioctl functions', 3.1),
('CVE-2017-0610', 'ASoC: msm: qdsp6: return error when copy from userspace fails', 3.04),
('CVE-2017-0613', 'qseecom: improve input validatation for qseecom_send_service_cmd', 3.04),
('CVE-2017-0614', 'qseecom: check buffer size when loading firmware images', 3.04),
('CVE-2017-0620', 'soc: qcom: scm: add check to avoid buffer overflow', 3.04),
('CVE-2017-0621', 'msm: camera: sensor: Fix the improper pointer dereference', 3.1),
('CVE-2017-0622', 'input: touchscreen: gt9xx: fix memory corruption in Goodix driver', 3.04),
('CVE-2017-0626', 'msm: crypto: set CLR_CNTXT bit for crypto operations', 3.04),
('CVE-2017-0627', 'Prevent heap overflow in uvc driver', 3.1),
('CVE-2017-0628', 'msm: camera: sensor: Validate i2c_frq_mode in msm_cci_get_clk_rates', 3.18),
('CVE-2017-0631', 'msm: camera: flash: Validate the power setting size', 3.1),
('CVE-2017-0632', 'ASoC: msm8x10-wcd: prevent out of bounds access', 3.04),
('CVE-2017-0633', 'net: wireless: bcmdhd: fix for IOVAR GET failed', 3.04),
('CVE-2017-0636', 'PYTHON-CVE : Commit not found'),
('CVE-2017-0650', 'input: touchscreen: validate bounds of intr_reg_num', 3.04),
('CVE-2017-0705', 'net: wireless: bcmdhd: adding bssid count NL attribute in SWC config', 3.04),
('CVE-2017-0706', 'net: wireless: bcmdhd: adding boundary check in wl_cfg80211_mgmt_tx', 3.04),
('CVE-2017-0710', 'Revert "proc: smaps: Allow smaps access for CAP_SYS_RESOURCE"', 3.04),
('CVE-2017-0746', 'msm: ipa: Fix for missing int overflow check in the refcount library', 3.04),
('CVE-2017-0748', 'ASoC: msm: qdspv2: add result check when audio process fail', 3.1),
('CVE-2017-0749', 'tracing: fix race condition reading saved tgids', 3.18),
('CVE-2017-0750', 'f2fs: sanity check log_blocks_per_seg', 3.04),
('CVE-2017-0751', 'qcdev: Check the digest length during the SHA operations', 3.04),
('CVE-2017-0786', 'net: wireless: bcmdhd: adding boudary check in wl_escan_handler', 3.04),
('CVE-2017-0787', 'net: wireless: bcmdhd: adding boundary check for pfn events', 3.1),
('CVE-2017-0788', 'net: wireless: bcmdhd: adding boundary check for pfn events', 3.1),
('CVE-2017-0789', 'net: wireless: bcmdhd: Remove "dhd_handle_swc_evt" from dhd.', 3.1),
('CVE-2017-0790', 'net: wireless: bcmdhd: add boundary check in GSCAN full result handler', 3.1),
('CVE-2017-0791', 'net: wireless: bcmdhd: adding boundary check in wl_notify_rx_mgmt_frame', 3.04),
('CVE-2017-0792', 'net: wireless: bcmdhd: add boundary check in dhd_rtt_event_handler', 3.1),
('CVE-2017-0794', 'Prevent potential double frees in sg driver', 3.04),
('CVE-2017-0824', 'net: wireless: bcmdhd: remove SDIO debug IOVARs causing out of bounds', 3.04),
('CVE-2017-0825', 'net: wireless: bcmdhd: add log trace event length check', 3.1),
('CVE-2017-1000251', 'Bluetooth: Properly check L2CAP config option output buffer length', 3.04),
('CVE-2017-1000364', 'flo: regen defconfig', 3.04),
('CVE-2017-1000365', 'fs/exec.c: account for argv/envp pointers', 3.04),
('CVE-2017-1000380', 'ALSA: timer: Fix missing queue indices reset at SNDRV_TIMER_IOCTL_SELECT', 3.04),
('CVE-2017-10661', 'timerfd: Protect the might cancel mechanism proper', 3.04),
('CVE-2017-10662', 'f2fs: sanity check checkpoint segno and blkoff', 3.04),
('CVE-2017-10663', 'f2fs: sanity check checkpoint segno and blkoff', 3.04),
('CVE-2017-10996', 'arm64: Fix out of bound access to compat_hwcap_str', 3.1),
('CVE-2017-10997', 'msm: pcie: add bounds check for debugfs register write', 3.1),
('CVE-2017-10998', 'ASoC: msm: qdsp6v2: extend validation of virtual address', 3.04),
('CVE-2017-10999', 'msm: ipa: fix security issues in ipa wan driver', 3.1),
('CVE-2017-11000', 'msm: camera: fix off-by-one overflow in msm_isp_get_bufq', 3.04),
('CVE-2017-11001', 'qcacld-2.0: Fix out of bound read issue in get link properties', 3.1),
('CVE-2017-11002', 'qcacld-2.0: Avoid concurrent matrix max param overread', 3.1),
('CVE-2017-11040', 'PYTHON-CVE : Commit not found'),
('CVE-2017-11046', 'ASoC: msm: qdsp6v2: add size check to fix out of bounds issue', 3.1),
('CVE-2017-11048', 'msm: mdss: Increase fbmem buf ref count before use', 3.1),
('CVE-2017-11050', 'qcacld-2.0: Restrict max/min pktlog buffer size using pktlogconf tool', 3.1),
('CVE-2017-11051', 'qcacld-2.0: Fix Uninitialized memory issue', 3.1),
('CVE-2017-11052', 'qcacld-2.0: Properly validate QCA_WLAN_VENDOR_ATTR_NDP_IFACE_STR', 3.1),
('CVE-2017-11053', 'qcacld-2.0: Fix kernel memory corruption', 3.1),
('CVE-2017-11054', 'qcacld-2.0: Avoid overread when configuring MAC addresses', 3.1),
('CVE-2017-11055', 'qcacld-2.0: Apply policy to fine time measurement', 3.1),
('CVE-2017-11056', 'compat_qcedev: Fix accessing userspace memory in kernel space', 3.1),
('CVE-2017-11057', 'msm: camera: sensor:validating the flash initialization parameters', 3.1),
('CVE-2017-11059', 'crypto: msm: Fix several race condition issues in crypto drivers', 3.04),
('CVE-2017-11060', 'qcacld-2.0: Avoid buffer overread when parsing PNO commands', 3.1),
('CVE-2017-11061', 'qcacld-2.0: Validate vendor set roaming params command', 3.1),
('CVE-2017-11062', 'qcacld-2.0: Validate vendor command do_acs', 3.1),
('CVE-2017-11064', 'qcacld-2.0: Add an attribute to represent PNO/EPNO Request ID', 3.1),
('CVE-2017-11067', 'qcacld-2.0: Check target address boundary before access', 3.1),
('CVE-2017-11600', 'xfrm: policy: check policy direction value', 3.04),
('CVE-2017-12146', 'driver core: platform: fix race condition with driver_override', 3.1),
('CVE-2017-12153', 'nl80211: check for the required netlink attributes presence', 3.04),
('CVE-2017-2618', 'selinux: fix off-by-one in setprocattr', 3.04),
('CVE-2017-2636', 'tty: n_hdlc: get rid of racy n_hdlc.tbuf', 3.04),
('CVE-2017-2671', 'ping: implement proper locking', 3.04),
('CVE-2017-5551', 'Revert "tmpfs: clear S_ISGID when setting posix ACLs"', 3.04),
('CVE-2017-5669', 'ipc/shm: Fix shmat mmap nil-page protection The issue is described here, with a nice testcase:', 3.04),
('CVE-2017-5897', 'ip6_gre: fix ip6gre_err() invalid reads', 3.1),
('CVE-2017-5967', 'kingdom: remove TIMER_STATS', 3.04),
('CVE-2017-5970', 'dccp: fix freeing skb too early for IPV6_RECVPKTINFO', 3.04),
('CVE-2017-5972', 'tcp: remove BUG_ON() in tcp_check_req()', 3.04),
('CVE-2017-5986', 'dccp: fix freeing skb too early for IPV6_RECVPKTINFO', 3.04),
('CVE-2017-6001', 'perf: Do not double free', 3.04),
('CVE-2017-6074', 'dccp: fix freeing skb too early for IPV6_RECVPKTINFO', 3.04),
('CVE-2017-6214', 'tcp: avoid infinite loop in tcp_splice_read()', 3.04),
('CVE-2017-6247', 'PYTHON-CVE : Commit not found'),
('CVE-2017-6345', 'net/llc: avoid BUG_ON() in skb_orphan()', 3.04),
('CVE-2017-6346', 'packet: fix races in fanout_add()', 3.04),
('CVE-2017-6348', 'irda: Fix lockdep annotations in hashbin_delete().', 3.04),
('CVE-2017-6353', 'sctp: deny peeloff operation on asocs with threads sleeping on it', 3.04),
('CVE-2017-6421', 'input: touchscreen: remove msg21xx mstar touch driver', 3.1),
('CVE-2017-6423', 'soc: qcom: make debugfs support configurable for kryo l2 accessors driver', 3.18),
('CVE-2017-6424', 'qcacld-2.0: Fix buffer overflow in WLANSAP_Set_WPARSNIes()', 3.04),
('CVE-2017-6426', 'platform: msm: spmi: Fix possible race condition in debugfs', 3.04),
('CVE-2017-6951', 'keys: Guard against null match function in keyring_search_aux()', 3.04),
('CVE-2017-7184', 'xfrm_user: validate XFRM_MSG_NEWAE incoming ESN size harder', 3.04),
('CVE-2017-7187', 'Release 4.4.23.21', 3.04),
('CVE-2017-7308', 'packet: handle too big packets for PACKET_V3', 3.04),
('CVE-2017-7366', 'msm: kgsl: Fix pagetable member of struct kgsl_memdesc', 3.18),
('CVE-2017-7368', 'ASoC: msm: acquire lock in ioctl', 3.04),
('CVE-2017-7369', 'ASoC: Add backend user count checking', 3.1),
('CVE-2017-7370', 'msm: mdss: Add lock to avoid release of active session in rotator', 3.18),
('CVE-2017-7371', 'bluetooth: Fix free data pointer routine', 3.18),
('CVE-2017-7372', 'msm: ba: Fix race conditions in debug writes', 3.18),
('CVE-2017-7373', 'msm: mdss: Fix invalid dma attachment during fb shutdown', 3.04),
('CVE-2017-7374', 'fscrypt: remove broken support for detecting keyring key revocation', 3.04),
('CVE-2017-7472', 'KEYS: fix keyctl_set_reqkey_keyring() to not leak thread keyrings', 3.04),
('CVE-2017-7487', 'ipx: call ipxitf_put() in ioctl error path', 3.04),
('CVE-2017-7495', 'ext4: fix deadlock during page writeback', 3.1),
('CVE-2017-7616', 'mm/mempolicy.c: fix error handling in set_mempolicy and mbind.', 3.04),
('CVE-2017-7618', 'crypto: hash - Add real ahash walk interface', 3.04),
('CVE-2017-7889', 'ALSA: pcm : Call kill_fasync() in stream lock', 3.04),
('CVE-2017-8233', 'msm: camera: cpp: Fixing Heap overflow in output buffer', 3.18),
('CVE-2017-8236', 'msm: IPA: add the check on intf query', 3.04),
('CVE-2017-8237', 'msm: ipa3: Validate IPA and GSI firmwares before loading', 3.18),
('CVE-2017-8239', 'msm: sensor: validating the flash initialization parameters', 3.1),
('CVE-2017-8241', 'qcacld-2.0: Update correct msg length in oemData_SendMBOemDataReq API', 3.1),
('CVE-2017-8242', 'qseecom: add mutex around qseecom_set_client_mem_param', 3.04),
('CVE-2017-8244', 'msm: vidc: Protect debug_buffer access in core_info_read with lock.', 3.04),
('CVE-2017-8245', 'drivers: soc: add size check', 3.1),
('CVE-2017-8247', 'msm: camera: Allow driver file to be opend only once.', 3.04),
('CVE-2017-8250', 'PYTHON-CVE : Commit not found'),
('CVE-2017-8251', 'msm: camera: isp: fix for out of bound access array', 3.04),
('CVE-2017-8253', 'msm: camera: sensor: Add boundary check for cci master', 3.04),
('CVE-2017-8254', 'ASoC: msm: qdsp6: check audio client pointer before accessing', 3.04),
('CVE-2017-8256', 'qcacld-2.0: Add bounday check for multicastAddr array', 3.1),
('CVE-2017-8260', "msm: camera: don't cut to 8bits for validating enum variable", 3.04),
('CVE-2017-8262', 'msm: kgsl: Fix kgsl memory allocation and free race condition', 3.04),
('CVE-2017-8263', 'ashmem: remove cache maintenance support', 3.04),
('CVE-2017-8264', 'msm: camera: Add regulator enable and disable independent of CSID', 3.04),
('CVE-2017-8265', 'msm-vidc: Allocate bus vote data during initialization', 3.1),
('CVE-2017-8267', 'ashmem: remove cache maintenance support', 3.04),
('CVE-2017-8277', 'PYTHON-CVE : Commit not found'),
('CVE-2017-8280', 'wcnss: fix the potential memory leak and heap overflow', 3.04),
('CVE-2017-8281', 'diag: dci: Add protection while querying event status', 3.04),
('CVE-2017-8890', 'dccp/tcp: do not inherit mc_list from parent', 3.04),
('CVE-2017-9074', 'ipv6: Check ip6_find_1stfragopt() return value properly.', 3.04),
('CVE-2017-9075', 'sctp: do not inherit ipv6_{mc|ac|fl}_list from parent SCTP needs fixes similar to 83eaddab4378 ("ipv6/dccp: do not inherit ipv6_mc_list from parent"), otherwise bad things can happen.', 3.04),
('CVE-2017-9076', 'sctp: do not inherit ipv6_{mc|ac|fl}_list from parent', 3.04),
('CVE-2017-9077', 'ipv6/dccp: do not inherit ipv6_mc_list from parent', 3.04),
('CVE-2017-9150', "bpf: don't let ldimm64 leak map addresses on unprivileged", 3.18),
('CVE-2017-9242', 'ipv6: fix out of bound writes in __ip6_append_data()', 3.04),
('CVE-2017-9676', 'soc: qcom: msm_bus: add mutex lock for cllist data', 3.04),
('CVE-2017-9677', 'ASoC: msm: remove unused msm-compr-q6-v2', 3.04),
('CVE-2017-9682', 'msm: kgsl: Fix the race between context create and destroy', 3.04),
('CVE-2017-9684', 'usb: gadget: qc_rndis: Properly handle rndis_ipa_init failure', 3.04),
('CVE-2017-9686', 'Revert "Revert "msm: sps: Fix race condition in SPS debugfs APIs""', 3.04),
('CVE-2017-9687', 'PYTHON-CVE : Commit not found'),
('CVE-2017-9691', 'msm: gud: Remove gud driver', 3.04),
('CVE-2017-9693', 'prima: Trim extn capability to max supported in change station', 3.04),
('CVE-2017-9694', 'qcacld-2.0: Add lost AP sample size entry to nla policy', 3.1),
('CVE-2017-9697', 'diag: Synchronize command registration table access', 3.04),
('CVE-2017-9706', 'msm: mdss: Buffer overflow while processing gamut table data', 3.04),
('CVE-2017-9714', 'prima: Drop assoc request if RSNIE/WPAIE parsing fail', 3.04),
('CVE-2017-9715', 'qcacld-2.0: Avoid extscan bucket spec overread', 3.1),
('CVE-2017-9717', 'qcacld-2.0: Add get valid channels entry to NLA policy', 3.1),
('CVE-2017-9720', 'msm:camera: correct stats query out of boundary', 3.1),
('CVE-2017-9724', 'ion: Fix unprotected userspace access', 3.1),
('CVE-2017-9725', 'mm: Fix incorrect type conversion for size during dma allocation', 3.04),
('LVT-2017-0002', 'kernel: Fix potential refcount leak in su check', 3.04),
('LVT-2017-0003', 'fs: readdir: Fix su hide patch for non-iterate filesystems', 3.1),
('LVT-2017-0004', 'fs/exec: fix use after free in execve', 3.04),
]
