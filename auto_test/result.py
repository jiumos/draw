# coding: utf-8
import requests
import copy
from common import common_config
from urllib.parse import urlencode
from common.utils import CommonUtils
from common.ssh import ssh_pool


class Result(object):

    def __init__(self, vtap_ip, common_utils: CommonUtils):
        self.df_mgt_ip = common_utils.df_mgt_ip
        self.vtap_ip = vtap_ip
        self.common_utils = common_utils
        self.df_controller_port = common_utils.df_server_controller_port
        self.df_query_port = common_utils.df_server_query_port
        self.vtap_full_name = None

    @property
    def property_vtap_full_name(self):
        if self.vtap_full_name is None:
            self.vtap_full_name = self.common_utils.get_vtaps_full_name_by_ip(
                self.vtap_ip
            )
        return self.vtap_full_name

    def get_agent_commit_id(
        self, is_pod=True, ssh_port=common_config.ssh_port_default,
        username=common_config.ssh_username_default,
        password=common_config.ssh_password_default
    ):
        vm_ip = self.vtap_ip
        if is_pod:
            cmd = "kubectl exec -it $(kubectl get pod -n deepflow|grep agent|awk '{print $1}') -n deepflow -- deepflow-agent -v|grep CommitId| awk '{print $2}'"
        else:
            cmd = "deepflow-agent -v|grep CommitId| awk '{print $2}'"
        log.info(f"exec get_agent_commit_id: {cmd}")
        ssh = ssh_pool.get(vm_ip, ssh_port, username, password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        res = stdout.readlines()
        log.info(res)
        if not res:
            err = stderr.readlines()
            log.error(f"get commit id error: {err}")
            return ""
        return res[-1].strip('\n')[:7]

    def get_vtaps_max_cpu_usage(self, start_time, end_time):
        '''Maximum CPU usage of the agent on DF by API. Parameter description:
        vtaps_name; required field, Name of vtaps
        start_time; required field, Start time for filtering data
        end_time; required field, End time for filtering data
        '''
        vtaps_name = self.property_vtap_full_name
        max_cpu_list = list()
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        sql = '''select Max(`metrics.cpu_percent`) AS RSS, `tag.host` from \
                deepflow_agent_monitor where `tag.host` IN ('%s') AND time>=%s \
                AND time<=%s group by `tag.host` limit 100''' % (
            vtaps_name, start_time, end_time
        )
        data = {'db': 'deepflow_system', 'sql': sql}
        data = urlencode(data, encoding='gb2312')
        res = requests.post(
            url='http://%s:%s/v1/query/' %
            (self.df_mgt_ip, self.df_query_port), headers=headers, data=data
        )
        log.info(f"get_vtaps_max_cpu_usage:: sql:{sql} res: {res.content}")
        if res.json()['result'] is None:
            assert False
        if res.json()['result']['values'] is None:
            assert False
        for i in res.json()['result']['values']:
            max_cpu_list.append(i[-1])
        return max(max_cpu_list)

    def get_vtaps_max_mem_usage(self, start_time, end_time):
        '''Maximum memory usage of the agent on DF by API. Parameter description:
        vtaps_name; required field, Name of vtaps
        start_time; required field, Start time for filtering data
        end_time; required field, End time for filtering data
        '''
        vtaps_name = self.property_vtap_full_name
        max_mem_list = list()
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        sql = '''select Max(`metrics.memory`) AS RSS, `tag.host` from \
                deepflow_agent_monitor where `tag.host` IN ('%s') AND time>=%s \
                AND time<=%s group by `tag.host` limit 100''' % (
            vtaps_name, start_time, end_time
        )
        data = {'db': 'deepflow_system', 'sql': sql}
        data = urlencode(data, encoding='gb2312')
        res = requests.post(
            url='http://%s:%s/v1/query/' %
            (self.df_mgt_ip, self.df_query_port), headers=headers, data=data
        )
        log.info(f"get_vtaps_max_cpu_usage:: sql:{sql} res: {res.content}")
        for i in res.json()['result']['values']:
            max_mem_list.append(i[-1])
        return max(max_mem_list)

    def get_vtaps_max_dispatcher_bps(self, start_time, end_time):
        '''Maximum BPS of the agent on DF by API. Parameter description:
        start_time; required field, Start time for filtering data
        end_time; required field, End time for filtering data
        '''
        max_dispatcher_bps = list()
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        sql = '''select (Sum(`metrics.rx_bytes`)*8/60) AS rx_bytes,time(time, 60) AS time_interval,`tag.host` from \
                deepflow_agent_dispatcher where `tag.host` IN ('%s') AND time>=%s \
                AND time<=%s group by time_interval,`tag.host` limit 100''' % (
            self.property_vtap_full_name, start_time, end_time
        )
        data = {'db': 'deepflow_system', 'sql': sql}
        data = urlencode(data, encoding='gb2312')
        res = requests.post(
            url='http://%s:%s/v1/query/' %
            (self.df_mgt_ip, self.df_query_port), headers=headers, data=data
        )
        log.info(
            f"get_vtaps_max_dispatcher_bps:: sql:{sql} res: {res.content}"
        )
        for i in res.json()['result']['values']:
            max_dispatcher_bps.append(i[-1])
        return max(max_dispatcher_bps)

    def get_vtaps_max_dispatcher_pps(self, start_time, end_time):
        '''Maximum PPS of the agent on DF by API. Parameter description:
        start_time; required field, Start time for filtering data
        end_time; required field, End time for filtering data
        '''
        max_dispatcher_pps = list()
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        sql = '''select (Sum(`metrics.rx`)/60) AS rx,time(time, 60) AS time_interval,`tag.host` from \
                    deepflow_agent_dispatcher where `tag.host` IN ('%s') AND time>=%s \
                    AND time<=%s group by time_interval,`tag.host` limit 100''' % (
            self.property_vtap_full_name, start_time, end_time
        )
        data = {'db': 'deepflow_system', 'sql': sql}
        data = urlencode(data, encoding='gb2312')
        res = requests.post(
            url='http://%s:%s/v1/query/' %
            (self.df_mgt_ip, self.df_query_port), headers=headers, data=data
        )
        log.info(
            f"get_vtaps_max_dispatcher_pps:: sql:{sql} res: {res.content}"
        )
        for i in res.json()['result']['values']:
            max_dispatcher_pps.append(i[-1])
        return max(max_dispatcher_pps)

    def get_vtaps_max_drop_pack(self, start_time, end_time):
        '''Maximum drop-pack of the agent on DF by API. Parameter description:
        start_time; required field, Start time for filtering data
        end_time; required field, End time for filtering data
        '''
        drop_pack = list()
        query_url = 'http://%s:%s/v1/query/' % (
            self.df_mgt_ip, self.df_query_port
        )
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        sql = '''select Max(`metrics.kernel_drops`) AS drops,`tag.host` from \
                    deepflow_agent_dispatcher where `tag.host` IN ('%s') AND time>=%s \
                    AND time<=%s group by `tag.host` limit 100''' % (
            self.property_vtap_full_name, start_time, end_time
        )
        data = {'db': 'deepflow_system', 'sql': sql}
        data = urlencode(data, encoding='gb2312')
        res = requests.post(url=query_url, headers=headers, data=data)
        log.info(f"get_vtaps_max_drop_pack:: sql:{sql} res: {res.content}")
        for i in res.json()['result']['values']:
            drop_pack.append(i[-1])
        return max(drop_pack)

    def get_vtaps_max_concuerrent(self, start_time, end_time):
        '''Maximum number of agent concurrent connections on DF by API. Parameter description:
        start_time; required field, Start time for filtering data
        end_time; required field, End time for filtering data
        '''
        concurrent = list()
        query_url = 'http://%s:%s/v1/query/' % (
            self.df_mgt_ip, self.df_query_port
        )
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        sql = '''select Max(`metrics.concurrent`) AS concurrent,`tag.host` from \
                    deepflow_agent_flow_map where `tag.host` IN ('%s') AND time>=%s \
                    AND time<=%s group by `tag.host` limit 100''' % (
            self.property_vtap_full_name, start_time, end_time
        )
        data = {'db': 'deepflow_system', 'sql': sql}
        data = urlencode(data, encoding='gb2312')
        res = requests.post(url=query_url, headers=headers, data=data)
        log.info(f"get_vtaps_max_drop_pack:: sql:{sql} res: {res.content}")
        for i in res.json()['result']['values']:
            concurrent.append(i[-1])
        return max(concurrent)

    def unit_format(self, datas):
        '''Data format conversion, The specific fields are as follows.
        max_cpu: Values are retained in two decimal places and converted to percentage form
        max_mem: The unit of the value is converted from bytes to megabytes
        dispatcher_pps: The unit of the value is converted from packets per second to thousands of packets per second. 
        drop_pack: The format of the value is converted to string form.
        concurrent: The format of the value is converted to string form.
        '''
        data = copy.deepcopy(datas)
        data["max_cpu"] = "%.2f" % round(data["max_cpu"], 2)
        data["max_cpu"] = f"{data['max_cpu']}%"
        data["max_mem"] = "%.2fM" % round(data["max_mem"] / 1000000, 2)
        data["dispatcher_bps"] = "%.2fGbps" % round(
            data["dispatcher_bps"] / 1000000000, 2
        ) if data["dispatcher_bps"] >= 1000000000 else "%.2fMbps" % round(
            data["dispatcher_bps"] / 1000000, 2
        )
        data["dispatcher_pps"
             ] = "%.2fKpps" % round(data["dispatcher_pps"] / 1000, 2)
        data["drop_pack"] = "%d" % data["drop_pack"]
        data["concurrent"] = "%d" % data["concurrent"]
        return data

    def get_dispatcher_info_action(self, start_time, end_time):
        '''Performance results from the agent on DF by API.
        '''
        cpu_usage = self.get_vtaps_max_cpu_usage(
            start_time=start_time, end_time=end_time
        )
        mem_usage = self.get_vtaps_max_mem_usage(
            start_time=start_time, end_time=end_time
        )
        dispatcher_bps = self.get_vtaps_max_dispatcher_bps(
            start_time=start_time, end_time=end_time
        )
        dispatcher_pps = self.get_vtaps_max_dispatcher_pps(
            start_time=start_time, end_time=end_time
        )
        drop_pack = self.get_vtaps_max_drop_pack(
            start_time=start_time, end_time=end_time
        )
        concurrent = self.get_vtaps_max_concuerrent(
            start_time=start_time, end_time=end_time
        )
        return cpu_usage, mem_usage, dispatcher_bps, dispatcher_pps, drop_pack, concurrent

    def generate_format_point(self, start_time, end_time):
        max_cpu, max_mem, dispatcher_bps, dispatcher_pps, drop_pack, concurrent = self.get_dispatcher_info_action(
            start_time, end_time
        )
        if max_cpu == None or max_mem == None or dispatcher_bps == None or dispatcher_pps == None or drop_pack == None:
            log.error(
                'max_cpu/max_mem/dispatcher_bps/dispatcher_pps/drop_pack is invalid'
            )
            assert False
        point = {
            "max_cpu": max_cpu,
            "max_mem": max_mem,
            "dispatcher_bps": dispatcher_bps,
            "dispatcher_pps": dispatcher_pps,
            "drop_pack": drop_pack,
            "concurrent": concurrent,
        }
        format_point = self.unit_format(point)
        return format_point
