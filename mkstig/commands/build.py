import logging
import os
import shutil

from util.ckl import Checklist, parse as parseCkl
from jinja2 import Environment, FileSystemLoader

def copy_static_files(output_dir: str):
    for dir in os.listdir("mkstig/templates"):
        dir_path = os.path.join("mkstig/templates", dir)
        if os.path.isdir(dir_path):
            shutil.copytree(dir_path, os.path.join(output_dir, dir))

def build(output_dir: str):
    input_dir = "stigs"

    shutil.rmtree(output_dir, True)
    os.mkdir(output_dir)

    env = Environment(loader=FileSystemLoader("mkstig/templates"))
    template = env.get_template("base.html")

    checklists = []
    hosts = {}

    for file in os.listdir(input_dir):
        if file.endswith(".ckl"):
            ckl_path = os.path.join(input_dir, file)
            checklist = parseCkl(ckl_path)

            checklists.append(checklist)
    
    for checklist in checklists:
        env = Environment(loader=FileSystemLoader("mkstig/templates"))
        template = env.get_template("base.html")

        hostname = checklist.asset['host_name']
        stig_id = checklist.stig['stigid']

        if not hostname in hosts.keys():
            hosts[hostname] = { 'name': hostname, 'ckls': [] }
            os.mkdir(os.path.join(output_dir, hostname))

        hosts[hostname]['ckls'].append(stig_id)

        print(hosts.items())

        filename = f"{os.path.join(output_dir, hostname, stig_id)}.html"
        content = template.render(
            hostname=hostname,
            stig_id=stig_id,
            vulns=checklist.vulns,
            vuln_summary=checklist.summary,
            repo_name='WadeMason/mkstig',
            repo_url='https://github.com/WadeMason/mkstig',
            hosts=hosts.values(),
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

    copy_static_files(output_dir)