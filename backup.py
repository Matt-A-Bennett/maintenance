# I found the method here:
# http://www.admin-magazine.com/Articles/Using-rsync-for-Backups

# this script should be run periodically (e.g. weekly using crontab).  each
# execution will create a new full backup ('backup.0') and retain previous
# backups.{1,2,3}.  in the case of files that haven't been modified (or have
# been removed), backups.{1,2,3} will contain hard links pointing to them.
# this saves space since the files aren't duplicated, while allowing each
# backup to act as a full backup.

# for recovering a backup, use scp -r
# mbennett@storage.cism.ucl.ac.be:$backup_dir.backup.x recovery_dir where
# backup.x is the snapshot you want to reinstate and recovery_dir is an
# existing dir to put the recovered data IMPORTANT: the recovery_dir should be
# OUTSIDE of $dir_to_backup - otherwise the recovery_dir will itself get backed
# up for no reason when the script is next run

import subprocess
import socket

backup_dir=f'backup/{socket.gethostname()}'

# 4 snapshots of the directory
# remove oldest backups
subprocess.call(["ssh", "mbennett@storage.cism.ucl.ac.be",
                 "rm -rf", f"{backup_dir}.backup.3"])

# rotate all backups
subprocess.call(["ssh", "mbennett@storage.cism.ucl.ac.be",
                 "mv", f"{backup_dir}.backup.2", f"{backup_dir}.backup.3"])
subprocess.call(["ssh", "mbennett@storage.cism.ucl.ac.be",
                 "mv", f"{backup_dir}.backup.1", f"{backup_dir}.backup.2"])
subprocess.call(["ssh", "mbennett@storage.cism.ucl.ac.be",
                 "mv", f"{backup_dir}.backup.0", f"{backup_dir}.backup.1"])

with open('/home/mattb/maintenance/dirs_to_backup.txt') as dirs_to_backup:
    for dir_to_backup in dirs_to_backup:
        dir_to_backup=dir_to_backup.strip()
        backup_name=dir_to_backup.split('/')[-1]

        subprocess.call(["ssh", "mbennett@storage.cism.ucl.ac.be",
                         "mkdir -p", f"{backup_dir}.backup.0/{backup_name}"])

        # create new full backup.0 and replace files in backup.1 that have not
        # been modified in backup.0 with hardlinks to backup.0 (this way the
        # file is stored only once but has multiple links/pointers, so any
        # backup.x with a link can be used to restore it)
        subprocess.call(["rsync", "-aqz", "--delete", "-e",
                         "ssh", f"--link-dest=../../../{backup_dir}.backup.1/{backup_name}/",
                         f"{dir_to_backup}/",
                         f"mbennett@storage.cism.ucl.ac.be:{backup_dir}.backup.0/{backup_name}/"])

