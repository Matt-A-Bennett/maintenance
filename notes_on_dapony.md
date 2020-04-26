Here we can keep a record of useful information for the continuing maintenance
of this machine.   

wiki.debian.org/DontBreakDebian is a useful resource (I found it after breaking
debian...)

# General
The pc is labeled by IT as: 

## System hardware overview
We installed Debian 10 (Buster). We have two RAID arrays:

### RAID10 
RAID10 (1Tb) composed of four 500Gb drives. It is software RAID (configured
using the command line tool: mdadm). Used for OS and installed software. It
should be faster than the RAID5.

### RAID5 
RAID5 (6Tb) composed of four 2Tb drives. It is hardware raid and was already
built for use. We use it for storing data in your personal directory:
/home/<username>/

#### RAID Failure:
If there is a loud beeping (~1sec on, ~1sec off), it could be that a disk has
failed and degraded one of the RAID arrays. To inspect the RAID5 array, use
'sudo storcli help'; 'sudo storcli show all'; 'sudo storcli /c0/d0 show all'.

To turn of the beeping, use 'sudo storcli /c0 set alarm=off *(REMEMBER TO SET
THE ALARM TO ON ONCE THE ARRAY HAS BEEN REBUILT!)*

We have had a single disk fail within the RAID5 array on (lower-left drive,
when viewing the pc front panel): 22 Nov 2019 (soon after we got the thing).
We replaced the faulty disk on: 29-11-2019 and integrated it back into the
array (this took about 4 hours to complete).

## Users
Users mattb, kirstenp and valerieg have sudo rights and therefore can install
things (and delete things...). These users can also grant sudo rights to other
users.

## Software

In general, we should install things in /usr/local/ and add any necessary paths
into /etc/profile. That way, all users will be able to use the software.

### Installed

#### General
Tmux [-mattb]

AnyDesk installed for remote desktop (after passing through vpn protocol)
[-mattb]

#### Coding
Matlab 2019b [-Roland]

R installed on 26-04-20. Also installed the 'stringr' package to test it worked
[-mattb]

Python3 [-mattb]

Spyder3 [-mattb]

Anaconda3 [-mattb]

#### Neuroimaging
FSL [-mattb]

Freesurfer [-mattb]

SPM12 [-mattb]

ANTs [-mattb]

ITKSNAP 3.8.0 [-mattb]

 - To make ITKSNAP work, mattb installed the library (libpng12-0-udeb) from: 
packages.debian.org/jessie/libpng12-0-udeb

 - and these two dependencies:
     - libc6-udeb (2.19-18+deb8u10)
     - zlib1g-udeb (1:1.28.dfsg-2 and others)

     - N.B. I tried using the regular libpng12-0 (rather than the -udeb
       version), but that didn't work.
     - N.B. Do not try with the sid (unstable) libs - I did, and had to
       reinstall the OS (apparently the are very important...)


