import subprocess
import re
from datetime import datetime as dt

query = subprocess.run(
    [
        "ssh",
        "mbennett@storage.cism.ucl.ac.be",
        "df | grep ions"
    ],
    stdout=subprocess.PIPE).stdout.decode("utf-8")

used = query.split()[4]

# grab digits from string
used = int(re.findall("\d+", used)[0])

if used > 80:
    warn_level = "warning"
    if used > 90:
        warn_level = "critical"

    with open("/home/mattb/maintenance/monitor.log", "a") as log:
        log.write(f"\n{warn_level}: cism storage is at {used}% ({dt.now()})")
