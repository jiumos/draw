# coding: utf-8
"""
author: danqing
date: 2022-09-15
desc: 脚本公共配置变量区域。
"""

# ------ Host Parameter Definition Area ------------
df_env_uuid = ''
df_evns_fixed_uid = 'daily_fixed'
pytest_uuid = ''
teardownsleep = 0
current_timestamp = 0
#Development environment for debugging scripts
df_ce_mgt_ip = '10.1.19.21'
df_ce_port = 22
df_ce_api_port = 30417
ext_dns_server = '114.114.114.114'
debug = 0
#Automation generic username and password
ssh_port_default = 22
ssh_username_default = 'root'
ssh_password_default = 'Yunshan3302!'
ssh_password_common = 'yunshan3302'
ssh_parameter_default  = (ssh_port_default, ssh_username_default, ssh_password_default)
# resource
domain_agent_sync_name_default = 'agent_sync'
# Nexus.yunshan.net相关
deepflow_agent_rpm_lastest_url = 'https://deepflow-ce.oss-cn-beijing.aliyuncs.com/rpm/agent/latest/linux/amd64/deepflow-agent-rpm.zip'
deepflow_agent_deb_lastest_url = 'https://deepflow-ce.oss-cn-beijing.aliyuncs.com/deb/agent/latest/linux/amd64/deepflow-agent-deb.zip'
nexus_trident_lastest_url = 'http://nexus.yunshan.net/repository/platform/trident/master/x86_64/artifacts.zip'
kube_proxy_port_default = '8001'
# deepflow-ce mysql info
deepflow_ce_mysql_user = 'root'
deepflow_ce_mysql_passwd = 'deepflow'
deepflow_ce_mysql_db = 'deepflow'
# ce demo influxdb
ce_demo_influxdb_user = 'root'
ce_demo_influxdb_passwd = 'Yunshan3302!'
ce_demo_influxdb_url = 'cloud.deepflow.yunshan.net'
ce_demo_influxdb_port = 31840
# logger
test_logger_prefix = ""

# ------ Aliyun Public Cloud------------
# Common Variable Definition
ali_dns_ip = '10.1.0.1'
ali_name_default = 'aliyun'
ali_vpc_name_default = 'infrastructure'
ali_az_bj_default = 'cn-beijing-a'
ali_security_group_default = 'sg-2zegvk5suvkrfo6qcd6r'
ali_instance_type_n1_medium = 'ecs.n1.medium'
ali_instance_type_c1m2_large = 'ecs.t5-lc1m2.large'
ali_instance_type_c1m2_xlarge = 'ecs.t5-c1m2.2xlarge'
ali_instance_type_g6r_large = 'ecs.g6r.large'
ali_instance_type_g6r_xlarge = 'ecs.g6r.xlarge'
ali_instance_type_c6_2x_large = 'ecs.c6.2xlarge'
ali_instance_type_c6_x_large = 'ecs.c6.xlarge'
ali_system_disk_categroy_default = 'cloud_efficiency'
ali_image_centos7_id_default = 'centos_7_9_x64_20G_alibase_20211227.vhd'
ali_image_centos6_id_default = 'centos_6_10_x64_20G_alibase_20201120.vhd'
ali_image_ubuntu14_id_default = 'ubuntu_14_0405_64_20G_alibase_20170824.vhd'
ali_image_ubuntu14_415_id = 'm-2zea09q16pyg0fvt4pae'
ali_image_ubuntu16_415_id = 'm-2zegw45kzdb1c7tau707'
ali_image_centos7_419_id = 'm-2zec520yiix6ihla0r7b'
ali_image_centos7_performance_id = 'm-2zeioytvveg36neb25y0'
ali_image_anolis_performance_id = 'm-2ze5tr4n5xe55lw1c0kg'
ali_image_centos7_deepflow_id = 'm-2ze9zy6izp9sgb44k31u'
ali_image_centos7_deepflow_private_id = 'm-2ze7cqrnq0ib485z0x09'
ali_image_ubuntu16_id_default = 'ubuntu_16_04_x64_20G_alibase_20211028.vhd'
ali_image_ubuntu18_id_default = 'ubuntu_18_04_x64_20G_alibase_20220727.vhd'
ali_image_ubuntu20_id_default = 'ubuntu_20_04_x64_20G_alibase_20220727.vhd'
ali_image_debian11_id_default = 'debian_11_5_x64_20G_alibase_20221107.vhd'
ali_image_anolisos_84_arm64_id_default = 'm-2zehml6llb4r5kjl0f9d'
ali_image_centos7_agent_performance_nginx = 'm-2ze04udh1zzjc6813fep'
ali_image_centos7_agent_performance_nginx_https = 'm-2ze1kjcqsabaf2k95ctl'
ali_image_centos7_agent_performance_istio = 'm-2ze04udh1zzjc6813fep'
ali_image_centos7_agent_performance_gochi = 'm-2zefp1362nzulfr5b7zt'
ali_image_centos7_agent_performance_goserver = 'm-2ze1fpbidqrtxtgbtoij'
ali_image_ubuntu20_agent_performance_h2load = 'm-2ze90c11tzn4p9vv30xu'
ali_image_ubuntu20_agent_performance_memtier = 'm-2zehweoiocguj2vjyx0z'
ali_resource_group_ie_ee = 'rg-aekzm564q2edrsi'
ali_switch_id_default = 'vsw-2zesbggx0gxti4bs53qga'
ali_switch_id_arm = 'vsw-2zeh3cgrhmn0kmhudu1wl'
ali_vm_password_default = 'Yunshan3302!'
ali_zone_id_default = 'cn-beijing-a'
ali_zone_id_beijing_k = 'cn-beijing-k'
ali_key_pair_name = 'automation'
ali_id_rsa = ''

# ------ TCE Public Cloud ------------
# Common Variable Definition
tce_az_bj_default = 'ap-beijing-3'
tce_security_group_default = 'sg-llvqubqp'
tce_instance_type_s5_medium4 = 'S5.MEDIUM4'
tce_image_centos7_id_default = 'img-l8og963d'
tce_disk_type_default = 'CLOUD_PREMIUM'
tce_vpc_id_default = 'vpc-paiqfy80'
tce_subnet_id_default = 'subnet-41ci6zqz'
tce_vm_password_default = 'Yunshan3302!'

# performance metrics
HPING3_FLOOD_PPS = 100  #15Kpps
HPING3_FASTER_PPS = 100  #9Kpps

UDP_PERFORMANCE_PPS = 600  # 600Kpps
TCP_PERFORMANCE_K8S_BPS = 20  # 10Gbps
TCP_PERFORMANCE_WORKLOADV_BPS = 20  #20Gbps'

AGENT_PERFORMANCE_MEMORY = 15622000

# deepflowee performance metrics
DFEE_PERFORMANCE_WORKLOADV_TCP_BPS = 1  #1Gbps
DFEE_IP = '10.1.19.117'
DFEE_PERFORMANCE_DISTRIBUTE = 1

# test plugins
RUNNER_PLUGINS = []
