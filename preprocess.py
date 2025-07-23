import json
import math
import csv
import re
from typing import Any
from dateutil.parser import parse

# PRETIME = 1751120000
PRETIME = 1

logs: list[str] = []


def parse_time(time_str: str) -> int:
  """Parse the time string and return the timestamp."""
  time = parse(time_str)
  return math.floor((time.timestamp() - PRETIME))


with open('./example/final/log/01_package-watcher_15days.csv') as f:
  reader = csv.DictReader(f)
  for row in reader:
    log: dict[str, Any] = json.loads(row['log'])
    if log['package_name'] == '' or log['package_tag'] == '' or not log['package_tag'].startswith('stg-'):
      continue
    logs.append(f'create {log["package_name"]} {log["package_tag"]} {parse_time(log["time"])}\n')

found = set()

with open('./example/final/log/02_image-reflector_15days.csv') as f:
  reader = csv.DictReader(f)
  for row in reversed(list(reader)):
    log: dict[str, Any] = json.loads(row['log'])
    if log.get('name', '') == '':
      continue
    msg: str = log['msg']
    matches = re.match(r"^Latest image tag for (\S+) resolved to (\S+)", log['msg'])
    if not matches:
      continue
    image_name = matches.group(1)
    image_tag = matches.group(2)
    logs.append(f'fetch {image_name[16:]} {image_tag} {parse_time(log["ts"])}\n')

# with open('./example/final/log/03_push-events.csv') as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     log: dict[str, Any] = json.loads(row['log'])
#     included = False
#     for commit in log['commits']:
#       if 'kubernetes/apps/auth/staging/kustomization.yaml' in commit['modified']:
#         included = True
#         break
#     if not included:
#       continue
#     time_str: str = log['time']
#     time = parse(time_str)
#     logs.append(f'push {time.timestamp()-PRETIME}\n')

logs.sort(key=lambda x: float(x.split()[-1]))

with open('example/final/out_15days.txt', 'w') as f:
  f.writelines(logs)
