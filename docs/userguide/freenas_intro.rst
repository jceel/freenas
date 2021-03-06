:orphan:

|93cover.jpg|

.. centered:: FreeNAS® is © 2011-2014 iXsystems

.. centered:: FreeNAS® and the FreeNAS® logo are registered trademarks of iXsystems.
   
.. centered:: FreeBSD is a registered trademark of the FreeBSD Foundation
   
.. centered:: Cover art by Jenny Rosenberg

Written by users of the FreeNAS® network-attached storage operating system.

Version 9.3

Published XX, 2014

Copyright © 2011-2014
`iXsystems <http://www.ixsystems.com/>`_

.. sectnum::

This Guide covers the installation and use of FreeNAS® 9.3.

The FreeNAS® Users Guide is a work in progress and relies on the contributions of many individuals. If you are interested in helping us to improve the Guide,
read the instructions in the `README 
<https://github.com/freenas/freenas/blob/master/docs/userguide/README>`_. If you use IRC Freenode, you are welcome to join the #freenas channel where you will
find other FreeNAS® users.

The FreeNAS® Users Guide is freely available for sharing and redistribution under the terms of the
`Creative Commons Attribution License
<http://creativecommons.org/licenses/by/3.0/>`_. This means that you have permission to copy, distribute, translate, and adapt the work as long as you
attribute iXsystems as the original source of the Guide.

FreeNAS® and the FreeNAS® logo are registered trademarks of iXsystems.

3ware® and LSI® are trademarks or registered trademarks of LSI Corporation.

Active Directory® is a registered trademark or trademark of Microsoft Corporation in the United States and/or other countries.

Apple, Mac and Mac OS are trademarks of Apple Inc., registered in the U.S. and other countries.

Chelsio® is a registered trademark of Chelsio Communications.

Cisco® is a registered trademark or trademark of Cisco Systems, Inc. and/or its affiliates in the United States and certain other countries.

Django® is a registered trademark of Django Software Foundation.

Facebook® is a registered trademark of Facebook Inc.

FreeBSD and the FreeBSD logo are registered trademarks of the FreeBSD Foundation.

Fusion-io is a trademark or registered trademark of Fusion-io, Inc.

Intel, the Intel logo, Pentium Inside, and Pentium are trademarks of Intel Corporation in the U.S. and/or other countries.

LinkedIn® is a registered trademark of LinkedIn Corporation.

Linux® is a registered trademark of Linus Torvalds.

Marvell® is a registered trademark of Marvell or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its affiliates.

Twitter is a trademark of Twitter, Inc. in the United States and other countries.

UNIX® is a registered trademark of The Open Group.

VirtualBox® is a registered trademark of Oracle.

VMware® is a registered trademark of VMware, Inc.

Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

Windows® is a registered trademark of Microsoft Corporation in the United States and other countries.

**Typographic Conventions**

The FreeNAS® 9.3 Users Guide uses the following typographic conventions:

* Names of graphical elements such as buttons, icons, fields, columns, and boxes are enclosed within quotes. For example: click the "Performance Test" button.

* Menu selections are italicized and separated by arrows. For example: :menuselection:`System --> Information`.

* Commands that are mentioned within text are highlighted in :command:`bold text`. Command examples and command output are contained in green code blocks.

* Volume, dataset, and file names are enclosed in a blue box :file:`/like/this`.

* Keystrokes are formatted in a blue box. For example: press :kbd:`Enter`.

* **bold text:** used to emphasize an important point.

* *italic text:* used to represent device names or text that is input into a GUI field.

Introduction
============

FreeNAS® is an embedded open source network-attached storage (NAS) system based on FreeBSD and released under a BSD license. A NAS provides an operating
system that has been optimized for file storage and sharing.

Notable features in FreeNAS® include:

* supports AFP, CIFS, FTP, NFS, SSH (including SFTP), and TFTP as file sharing mechanisms

* supports exporting file or device extents via iSCSI

* supports Active Directory or LDAP for user authentication as well as manual user and group creation

* supports the creation and import of UFS2 based volumes, including gmirror, gstripe, and graid3

* supports the creation and import of
  `ZFS <http://en.wikipedia.org/wiki/ZFS>`_
  pools, enabling many features not available in UFS2 such as quotas, snapshots, compression, replication, and datasets for sharing subsets of volumes

* upgrade procedure saves the current operating system to an inactive partition, allowing for an easy reversal of an undesirable upgrade

* system notifications are automatically mailed to the root user account

* `Django <http://en.wikipedia.org/wiki/Django_%28Web_framework%29>`_
  driven graphical user interface available through a web browser

* secure replication, automatic ZFS snapshots, scheduling of ZFS scrubs, and cron management are all configurable through the graphical interface

* support for menu localization and keyboard layouts

* SMART monitoring and UPS management in GUI

* support for Windows ACLs and UNIX filesystem permissions

* periodic ZFS snapshots are visible in Windows as shadow copies

* includes
  `tmux <http://sourceforge.net/projects/tmux/>`_, a BSD-licensed utility similar to GNU screen

What's New in 9.3
-----------------

FreeNAS® 9.3 fixes this list of bugs.

It is based on the stable version of FreeBSD 9.3 which adds 
`these features <https://www.freebsd.org/releases/9.3R/relnotes.html>`_, supports
`this hardware <https://www.freebsd.org/releases/9.3R/hardware.html>`_, and incorporates all of the
`security releases <http://www.freebsd.org/security/advisories.html>`_
issued since FreeBSD 9.3 RELEASE.

* FreeNAS® is now 64-bit only.

* A configuration wizard has been added. On a fresh install, this wizard will run after the *root* password is set, making it easy to quickly create a volume
  and share(s). Users who prefer to manually create their volumes and shares can exit the wizard and create these as usual. The wizard can be re-run at a
  later time by selecting `Wizard`_ from the graphical tree menu.

* Kernel iSCSI has replaced :command:`istgt`. This improves support for VMWare VAAI acceleration and adds support for Microsoft ODX acceleration and Windows
  2012 clustering.

* Support for Link Layer Discovery Protocol (`LLDP`_) has been added. This allows network devices to advertise their identity, capabilities, and neighbors on
  an Ethernet LAN.

The GUI has been reorganized as follows:

* :menuselection:`System --> System Information` is now :menuselection:`System --> Information`.

* :menuselection:`System --> Settings` has been divided into :menuselection:`System --> General`, :menuselection:`System --> Advanced`,
  :menuselection:`System --> Email`, and :menuselection:`System --> System Dataset`.

* :menuselection:`System --> Sysctls` and :menuselection:`System --> Tunables` have been merged into :menuselection:`System --> Tunables`. The "Type" field
  has been added to :menuselection:`System --> Tunables` so you can specify whether a "Loader" or a "Sysctl" is being created.

* NTP Servers has been moved to :menuselection:`System --> General`.

* :menuselection:`System --> Settings --> SSL` has been moved to :menuselection:`System --> General --> Set SSL Certificate`.
  
* A new `Tasks`_ menu has been added and the following have been moved to Tasks: Cron Jobs, Init/Shutdown Scripts, Rsync Tasks, and S.M.A.R.T Tests.

* A `ZFS Snapshots`_ menu has been added to Storage.

* :menuselection:`Services --> Directory Services` has been renamed to Directory Service and moved as its own item in the tree.

* :menuselection:`Services --> Directory Services --> Domain Controller` has been moved to :menuselection:`Services --> Domain Controller`.

* :menuselection:`Services --> LLDP` has been added.

* Log Out has been moved from the upper right corner to the tree menu.

The following fields have been added or deleted:

* The "WebGUI -> HTTPS Port" field has been added to :menuselection:`System --> General`.

* The "System dataset pool" and "Use system dataset for syslog" fields have been removed from :menuselection:`System --> Advanced` as these are now set in
  :menuselection:`System --> System Dataset`.

* A "Performance Test" button has been added to :menuselection:`System --> Advanced`.

* The "Directory Services" field is now deprecated and has been removed from :menuselection:`System --> General`. FreeNAS® now supports the
  `System Security Services Daemon (SSSD) <https://fedorahosted.org/sssd/>`_
  which provides support for multiple directory services.

* The "Rebuild LDAP/AD Cache" button has been removed from :menuselection:`System --> Advanced`. It has been renamed to "Rebuild Directory Service Cache" and
  now appears in the configuration screen for each type of directory service.

* The "HTTP Proxy" field has been added to :menuselection:`Network --> Global Configuration`.

* A "Run Now" button has been added for the highlighted cron job in :menuselection:`Tasks --> Cron Jobs --> View Cron Jobs`.

* An "Upgrade" button has been added to the available icons for a highlighted volume in :menuselection:`Storage --> Volumes --> View Volumes`. This means that
  you no longer need to upgrade a ZFS pool from the command line.

* The "Domain logons" checkbox has been added to :menuselection:`Services --> CIFS`.

* The "Workgroup Name" field is deprecated and has been removed from :menuselection:`Directory Service --> Active Directory`. The "Encryption Mode",
  "Certificate", and "Enable" fields and the "Idmap backend" drop-down menu have been added to :menuselection:`Directory Service --> Active Directory`. The
  "Kerberos Server" and "Kerberos Password Server" fields have been replaced by the "Kerberos Realm" drop-down menu.

* The "Encryption Mode" and "Auxiliary Parameters" fields have been removed from :menuselection:`Directory Service --> LDAP` and the "Enable" checkbox, "Use
  default domain" field and "Kerberos Realm", "Kerberos Keytab", and "Idmap backend" drop-down menus have been added.

* The "Enable" checkbox has been added to :menuselection:`Directory Service --> NIS`.

* The "Use default domain" and "Enable" checkboxes and the "Idmap backend" drop-down menu have been added to :menuselection:`Directory Service --> NT4`.

* :menuselection:`Directory Service --> Kerberos Realms` and `Directory Service --> Kerberos Keytabs` have been added.

* The "Database Path" field has been moved from :menuselection:`Sharing --> Apple (AFP) Share --> Add Apple (AFP) Share` to :menuselection:`Services --> AFP`.

* The "Zero Device Numbers" field has been moved from :menuselection:`Services --> AFP to Sharing --> Apple (AFP) Share --> Add Apple (AFP) Share`.

* The "Obey pam restrictions" has been added to :menuselection:`Services --> CIFS`.

* The "IP Server" field has been added to :menuselection:`Services --> Dynamic DNS`.

* The "Enable TPC" field has been added to :menuselection:`Services --> iSCSI --> Extents --> Add Extent`.

* :menuselection:`Services --> iSCSI --> Target Global Configuration` has been reduced to three configuration options used by kernel iSCSI.

* The "Target Flags" and "Queue Depth" fields are now deprecated and have been removed from :menuselection:`Services --> iSCSI --> Targets --> Add Target`.

Known Issues
------------

Before installing FreeNAS® you should be aware of the following known issues:

* **UPGRADES FROM FreeNAS® 0.7x ARE NOT SUPPORTED.** The system has no way to import configuration settings from 0.7x versions of FreeNAS®, meaning that you
  will have to manually recreate your configuration. However, you should be able to import_supported FreeNAS® 0.7x volumes.

* **The ZFS upgrade procedure is non-reversible.** Do not upgrade your ZFS version unless you are absolutely sure that you will never want to go back to the
  previous version. There is no reversing a ZFS pool upgrade, and there is no way for a system with an older version of ZFS to access pools that have been
  upgraded.

* The available space reported in the parent zpool may not reflect reality and can be confusing because the available space represented by datasets or zvols
  can exceed that of the parent zpool.

* Disks with certain configurations can get probed by GEOM and become essentially unwritable without manual intervention. For instance, if you use disks that
  previously had a gmirror on them, the system may pick that up and the disks will be unavailable until the existing gmirror is stopped and destroyed.

* The mps driver for 6G LSI SAS HBAs is version 16, which requires phase 16 firmware on the controller. It is recommended to upgrade the firmware before
  installing FreeNAS® or immediately after upgrading FreeNAS®. Running older firmware can cause many woes, including the failure to probe all of the
  attached disks, which can lead to degraded or unavailable arrays.

Hardware Recommendations
------------------------

Since FreeNAS® 9.3 is based on FreeBSD 9.3, it supports the same hardware found in the `FreeBSD Hardware Compatibility List
<http://www.freebsd.org/releases/9.3R/hardware.html>`__. Supported processors are listed in section
`2.1 amd64 <https://www.freebsd.org/releases/9.3R/hardware.html#proc>`_. Beginning with version 9.3, FreeNAS® is only available for 64-bit (also known as
amd64) processors.

Actual hardware requirements will vary depending upon what you are using your FreeNAS® system for. This section provides some guidelines to get you started.
You can also skim through the
`FreeNAS® Hardware Forum <http://forums.freenas.org/forumdisplay.php?18-Hardware>`_ for performance tips from other FreeNAS® users or to post questions
regarding the hardware best suited to meet your requirements. This
`forum post <http://forums.freenas.org/threads/so-you-want-some-hardware-suggestions.12276/>`_
provides some specific recommendations if you are planning on purchasing hardware.

RAM
~~~

The best way to get the most out of your FreeNAS® system is to install as much RAM as possible. The recommended minimum is 8 GB of RAM. The more RAM, the
better the performance, and the
`FreeNAS® Forums <http://forums.freenas.org/>`_
provide anecdotal evidence from users on how much performance is gained by adding more RAM. For systems with a disk capacity greater than 8 TB, a general rule
of thumb is 1 GB of RAM for every 1 TB of storage. This
`post <http://hardforum.com/showpost.php?s=8d31305e57c1dd2853eb817124ff18d9&p=1036865233&postcount=3>`_
describes how RAM is used by ZFS.

If you plan to use your server for home use, you can often soften the rule of thumb of 1 GB of RAM for every 1 TB of storage, though 8 GB of RAM is still the
recommended minimum. If performance is inadequate, consider adding more RAM as a first remedy. The sweet spot for most home or small business users is 16 GB
of RAM. While it is possible to use ZFS on systems with less than 8 GB of RAM, performance will be substantially reduced. The ZFS filesystem will
automatically disable pre-fetching (caching) on systems where it is not able to use at least 4 GB of memory for its cache and data structures.

.. note:: if your RAM is limited, you can consider using the UFS filesystem until you can afford better hardware. However, many of the compelling features of
   FreeNAS® are not available with UFS.

If your system supports it and your budget allows for it, install ECC RAM. While more expensive, ECC RAM is highly recommended as it prevents in-flight
corruption of data before the error-correcting properties of ZFS come into play, thus providing consistency for the checksumming and parity calculations
performed by ZFS. If you consider your data to be important, use ECC RAM. This 
`Case Study <http://research.cs.wisc.edu/adsl/Publications/zfs-corruption-fast10.pdf>`_ describes the risks associated with memory corruption.

If you plan to use ZFS deduplication, a general rule of thumb is 5 GB RAM per TB of storage to be deduplicated.

If you use Active Directory with FreeNAS®, add an additional 2 GB of RAM for winbind's internal cache.

If you are installing FreeNAS® on a headless system, disable the shared memory settings for the video card in the BIOS.

If you don't have at least 8GB of RAM with ZFS or 2GB of RAM with UFS, you should consider getting more powerful hardware before using FreeNAS® to store your
data. Plenty of users expect FreeNAS® to function with less than these requirements, just at reduced performance.  The
bottom line is that these minimums are based on the feedback of many users. Users that do not meet these requirements and who ask for help in the forums or
IRC will likely be ignored because of the abundance of information that FreeNAS® may not behave properly with less than 8GB of RAM.

Compact or USB Flash
~~~~~~~~~~~~~~~~~~~~

The FreeNAS® operating system is a running image. This means that it should not be installed onto a hard drive, but rather to a USB or compact flash device
that is at least 2 GB in size. If you don't have compact flash, use a USB thumb drive that is dedicated to the running image and which stays inserted in the
USB slot. While technically you can install FreeNAS® onto a hard drive, this is discouraged as you will lose the storage capacity of the drive. In other
words, the operating system will take over the drive and will not allow you to store data on it, regardless of the size of the drive.

.. note:: many USB thumb drives that are labeled as 2GB are not really 2GB in size.  For this reason, it is recommended to use media that is 4GB or larger and
   to use a name brand USB stick.

USB 3.0 support is disabled by default as it currently is not compatible with some hardware, including Haswell (Lynx point) chipsets. If you receive a
"failed with error 19" message when trying to boot FreeNAS®, make sure that xHCI/USB3 is disabled in the system BIOS. While this will downclock the USB
ports to 2.0, the bootup and shutdown times will not be significantly different. To see if USB 3.0 support works with your hardware, create a `Tunables`_
named *xhci_load*, set its value to
*YES*, and reboot the system.

Storage Disks and Controllers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The
`Disk section <http://www.freebsd.org/releases/9.3R/hardware.html#DISK>`_
of the FreeBSD Hardware List lists the supported disk controllers. In addition, support for 3ware 6gbps RAID controllers has been added along with the CLI
utility :command:`tw_cli` for managing 3ware RAID controllers.

FreeNAS® supports hot pluggable drives. To use this feature, make sure that AHCI is enabled in the BIOS. Note that hot plugging is **not the same** as a hot
spare, which is not supported at this time.

If you need reliable disk alerting and immediate reporting of a failed drive, use a fully manageable hardware RAID controller such as a LSI
MegaRAID controller or a 3Ware twa-compatible controller. More information about LSI cards and FreeNAS® can be found in this
`forum post <http://forums.freenas.org/showthread.php?11901-Confused-about-that-LSI-card-Join-the-crowd>`_.

Suggestions for testing disks before adding them to a RAID array can be found in this
`forum post <http://forums.freenas.org/showthread.php?12082-Checking-new-HDD-s-in-RAID>`_.

`This article <http://technutz.com/purpose-built-nas-hard-drives/>`_
provides a good overview of hard drives which are well suited for a NAS.

If you have some money to spend and wish to optimize your disk subsystem, consider your read/write needs, your budget, and your RAID requirements:

* If you have steady, non-contiguous writes, use disks with low seek times. Examples are 10K or 15K SAS drives which cost about $1/GB. An example
  configuration would be six 600 GB 15K SAS drives in a RAID 10 which would yield 1.8 TB of usable space or eight 600 GB 15K SAS drives in a RAID 10 which
  would yield 2.4 TB of usable space.

* 7200 RPM SATA disks are designed for single-user sequential I/O and are not a good choice for multi-user writes.

If you have the budget and high performance is a key requirement, consider a
`Fusion-I/O card <http://www.fusionio.com/products/>`_
which is optimized for massive random access. These cards are expensive and are suited for high-end systems that demand performance. A Fusion-I/O card can be
formatted with a filesystem and used as direct storage; when used this way, it does not have the write issues typically associated with a flash device. A
Fusion-I/O card can also be used as a cache device when your ZFS dataset size is bigger than your RAM. Due to the increased throughput, systems running these
cards typically use multiple 10 GigE network interfaces.

If you will be using ZFS,
`Disk Space Requirements for ZFS Storage Pools <http://download.oracle.com/docs/cd/E19253-01/819-5461/6n7ht6r12/index.html>`_
recommends a minimum of 16 GB of disk space. Due to the way that ZFS creates swap, **you can not format less than 3 GB of space with ZFS**. However, on a
drive that is below the minimum recommended size you lose a fair amount of storage space to swap: for example, on a 4 GB drive, 2 GB will be reserved for
swap.

If you are new to ZFS and are purchasing hardware, read through
`ZFS Storage Pools  <http://www.open-tech.com/2011/10/zfs-best-practices-guide-from-solaris-internals/>`_
`Recommendations <http://www.solarisinternals.com/wiki/index.php/ZFS_Best_Practices_Guide#ZFS_Storage_Pools_Recommendations>`_
first.

ZFS uses dynamic block sizing, meaning that it is capable of striping different sized disks. However, if you care about performance, use disks of the same
size. Further, when creating a RAIDZ*, only the size of the smallest disk will be used on each disk.

Network Interfaces
~~~~~~~~~~~~~~~~~~

The
`Ethernet section <http://www.freebsd.org/releases/9.3R/hardware.html#ETHERNET>`_
of the FreeBSD Hardware Notes indicates which interfaces are supported by each driver. While many interfaces are supported, FreeNAS® users have seen the best
performance from Intel and Chelsio interfaces, so consider these brands if you are purchasing a new NIC. Realteks will perform poorly under CPU load as
interfaces with these chipsets do not provide their own processors.

At a minimum, a GigE interface is recommended. While GigE interfaces and switches are affordable for home use, modern disks can easily saturate 110 MB/s. If
you require higher network throughput, you can bond multiple GigE cards together using the LACP type of `Link Aggregations`_. However, the switch will need to
support LACP which means you will need a more expensive managed switch.

If network performance is a requirement and you have some money to spend, use 10 GigE interfaces and a managed switch. If you are purchasing a managed switch,
consider one that supports LACP and jumbo frames as both can be used to increase network throughput.

.. note:: at this time the following are not supported: InfiniBand, FibreChannel over Ethernet, or wireless interfaces.

If network speed is a requirement, consider both your hardware and the type of shares that you create. On the same hardware, CIFS will be slower than FTP or
NFS as Samba is
`single-threaded <http://www.samba.org/samba/docs/man/Samba-Developers-Guide/architecture.html>`_. If you will be using CIFS, use a fast CPU.

Wake on LAN (WOL) support is dependent upon the FreeBSD driver for the interface. If the driver supports WOL, it can be enabled using
`ifconfig(8) <http://www.freebsd.org/cgi/man.cgi?query=ifconfig>`_. To determine if WOL is supported on a particular interface, specify the interface name to
the following command. In this example, the capabilities line indicates that WOL is supported for the *re0* interface::

 ifconfig -m re0
 re0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> metric 0 mtu 1500
 options=42098<VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,WOL_MAGIC,VLAN_HWTSO>
 capabilities=5399b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,TSO4,WOL_UCAST,WOL_MCAST, WOL_MAGIC,VLAN_HWFILTER,VLAN_H WTSO>

If you find that WOL support is indicated but not working for a particular interface, `Report a Bug`_.

ZFS Primer
----------

ZFS is an advanced, modern filesystem that was specifically designed to provide features not available in traditional UNIX filesystems. It was originally
developed at Sun with the intent to open source the filesystem so that it could be ported to other operating systems. After the Oracle acquisition of Sun,
some of the original ZFS engineers founded
`OpenZFS <http://open-zfs.org>`_ in order to provided continued, collaborative development of the open source version. To differentiate itself from Oracle ZFS
version numbers, OpenZFS uses feature flags. Feature flags are used to tag features with unique names in order to provide portability between OpenZFS
implementations running on different platforms, as long as all of the feature flags enabled on the ZFS pool are supported by both platforms.

FreeNAS® uses OpenZFS and each new version of FreeNAS® keeps up-to-date with the latest feature flags and OpenZFS bug fixes. Since many of the features
provided by ZFS are particularly suited to the storage of data, format your disk(s) with ZFS in order to get the most out of your FreeNAS® system.

Here is an overview of the features provided by ZFS:

**ZFS is a transactional, Copy-On-Write**
`(COW) <https://en.wikipedia.org/wiki/ZFS#Copy-on-write_transactional_model>`_ filesystem. For each write request, a copy is made of the associated disk
block(s) and all changes are made to the copy rather than to the original block(s). Once the write is complete, all block pointers are changed to point to the
new copy. This means that ZFS always writes to free space and most writes will be sequential. When ZFS has direct access to disks, it will bundle multiple
read and write requests into transactions; most filesystems can not do this as they only have access to disk blocks. A transaction either completes or fails,
meaning there will never be a
`write-hole <http://blogs.oracle.com/bonwick/entry/raid_z>`_  and a filesystem checker utility is not necessary. Because of the transactional design, as
additional storage capacity is added it becomes immediately available for writes; to rebalance the data, one can copy it to re-write the existing data across
all available disks. As a 128-bit filesystem, the maximum filesystem or file size is 16 exabytes.
  
**ZFS was designed to be a self-healing filesystem**. As ZFS writes data, it creates a checksum for each disk block it writes. As ZFS reads data, it validates
the checksum for each disk block it reads. If ZFS identifies a disk block checksum error on a pool that is mirrored or uses RAIDZ*, ZFS will fix the corrupted
data with the correct data. Since some disk blocks are rarely read, regular scrubs should be scheduled so that ZFS can read all of the data blocks in order to
validate their checksums and correct any corrupted blocks. While multiple disks are required in order to provide redundancy and data correction, ZFS will
still provide  data corruption detection to a system with one disk. FreeNAS® automatically schedules a monthly scrub for each ZFS pool and the results of the
scrub will be displayed in `View Volumes`_. Reading the scrub results can provide an early indication of possible disk failure.
  
Unlike traditional UNIX filesystems, **you do not need to define partition sizes at filesystem creation time**. Instead, you feed a certain number of disk(s)
at a time (known as a vdev) to a ZFS pool and create filesystems from the pool as needed. As more capacity is needed, identical vdevs can be striped into the
pool. In FreeNAS®, `ZFS Volume Manager`_ can be used to create or extend ZFS pools. Once a pool is created, it can be divided into dynamically-sized
datasets or fixed-size zvols as needed. Datasets can be used to optimize storage for the type of data being stored as permissions and properties such as
quotas and compression can be set on a per-dataset level. A zvol is essentially a raw, virtual block device which can be used for applications that need
raw-device semantics such as iSCSI device extents.
  
**ZFS supports real-time data compression**. Compression happens when a block is written to disk, but only if the written data will benefit from compression.
When a compressed block is accessed, it is automatically decompressed. Since compression happens at the block level, not the file level, it is transparent to
any applications accessing the compressed data. By default, ZFS pools made using FreeNAS® version 9.2.1 or later will use the recommended LZ4 compression
algorithm by default.
  
**ZFS provides low-cost, instantaneous snapshots** of the specified pool, dataset, or zvol. Due to COW, the initial size of a snapshot is 0 bytes and the size
of the snapshot increases over time as changes to the files in the snapshot are written to disk. Snapshots can be used to provide a copy of data at the point
in time the snapshot was created. When a file is deleted, its disk blocks are added to the free list; however, the blocks for that file in any existing
snapshots are not added to the free list until all referencing snapshots are removed. This means that snapshots provide a clever way of keeping a history of
files, should you need to recover an older copy of a file or a deleted file. For this reason, many administrators take snapshots often (e.g. every 15
minutes), store them for a period of time (e.g. for a month), and store them on another system. Such a strategy allows the administrator to roll the system
back to a specific time or, if there is a catastrophic loss, an off-site snapshot can restore the system up to the last snapshot interval (e.g. within 15
minutes of the data loss). Snapshots are stored locally but can also be replicated to a remote ZFS pool. During replication, ZFS does not do a byte-for-byte
copy but instead converts a snapshot into a stream of data. This design means that the ZFS pool on the receiving end does not need to be identical and can use
a different RAIDZ level, volume size, compression settings, etc.
  
**ZFS boot environments provide a method for recovering from a failed upgrade**. Beginning with FreeNAS® version 9.3, a snapshot of the dataset the operating
system resides on is automatically taken before an upgrade or a system configuration change. This saved boot environment is automatically added to the GRUB
boot loader. Should the upgrade or configuration change fail, simply reboot and select the previous boot environment from the boot menu.

**ZFS provides a write cache** in RAM as well as a
`ZFS Intent Log <http://blogs.oracle.com/realneel/entry/the_zfs_intent_log>`_ (ZIL). The ZIL is a temporary storage area for **synchronous** writes until they
are written asynchronously to the ZFS pool. If the system has many synchronous writes where the integrity of the write matters, such as from a database server
or when using NFS over ESXi, performance can be increased by adding a
dedicated log device, or slog, using `ZFS Volume Manager`_.  More detailed explanations can be found in this
`forum post <http://forums.freenas.org/threads/some-insights-into-slog-zil-with-zfs-on-freenas.13633/>`_ and in this
`blog post <http://nex7.blogspot.com/2013/04/zfs-intent-log.html>`_. A dedicated log device will have no affect on CIFS, AFP, or iSCSI as these protocols
rarely use synchronous writes. When creating a dedicated log device, it is recommended to use a fast SSD with a supercapacitor or a bank of capacitors that
can handle writing the contents of the SSD's RAM to the SSD. The :command:`zilstat` utility can be run from Shell to help determine if the system would
benefit from a dedicated ZIL device. See
`this website <http://www.richardelling.com/Home/scripts-and-programs-1/zilstat>`_
for usage information. If you decide to create a dedicated log device to speed up NFS writes, the SSD can be half the size of system RAM as anything larger
than that is unused capacity. The log device does not need to be mirrored on a pool running ZFSv28 or feature flags as the system will revert to using the ZIL
if the log device fails and only the data in the device which had not been written to the pool will be lost (typically the last few seconds of writes). You
can replace the lost log device in the :menuselection:`View Volumes --> Volume Status` screen. Note that a dedicated log device can not be shared between ZFS
pools and that the same device cannot hold both a log and a cache device.

**ZFS provides a read cache** in RAM, known as the ARC, to reduce read latency. FreeNAS® adds ARC stats to 
`top(1) <http://www.freebsd.org/cgi/man.cgi?query=top>`_ and includes the :command:`arc_summary.py`
and :command:`arcstat.py` tools for monitoring the efficiency of the ARC. If an SSD is dedicated as a cache device, it is known as an
`L2ARC <https://blogs.oracle.com/brendan/entry/test>`_ and ZFS uses it to store more reads which can increase random read performance. However, adding an
L2ARC is **not** a substitute for insufficient RAM as L2ARC needs RAM in order to function.  If you do not have enough RAM for a good sized ARC, you will not
be increasing performance, and in most cases you will actually hurt performance and could potentially cause system instability. RAM is always faster than
disks, so always add as much RAM as possible before determining if the system would benefit from a L2ARC device. If you have a lot of applications that do
large amounts of **random** reads, on a dataset small enough to fit into the L2ARC, read performance may be increased by adding a dedicated cache device using
`ZFS Volume Manager`_. SSD cache devices only help if your active data is larger than system RAM, but small enough that a significant percentage of it will
fit on the SSD. As a general rule of thumb, an L2ARC should not be added to a system with less than 64 GB of RAM and the size of an L2ARC should not exceed 5x
the amount of RAM. In some cases, it may be more efficient to have two separate pools: one on SSDs for active data and another on hard drives for rarely used
content. After adding an L2ARC, monitor its effectiveness using tools such as :command:`arcstat`. If you need to increase the size of an existing L2ARC, you
can stripe another cache device using `ZFS Volume Manager`_. The GUI will always stripe L2ARC, not mirror it, as the contents of L2ARC are recreated at boot.
Losing an L2ARC device will not affect the integrity of the pool, but may have an impact on read performance, depending upon the workload and the ratio of
dataset size to cache size. Note that a dedicated L2ARC device can not be shared between ZFS pools. 

**ZFS was designed to provide redundancy while addressing some of the inherent limitations of hardware RAID** such as the write-hole and corrupt data written
over time before the hardware controller provides an alert. ZFS provides three levels of redundancy, known as RAIDZ*, where the number after the RAIDZ
indicates how many disks per vdev can be lost without losing data. ZFS also supports mirrors, with no restrictions on the number of disks in the mirror. ZFS
was designed for commodity disks so no RAID controller is needed. While ZFS can also be used with a RAID controller, it is recommended that the controller be
put into JBOD mode so that ZFS has full control of the disks. When determining the type of ZFS redundancy to use, consider whether your goal is to maximize
disk space or performance:

* RAIDZ1 maximizes disk space and generally performs well when data is written and read in large chunks (128K or more).

* RAIDZ2 offers better data availability and significantly better mean time to data loss (MTTDL) than RAIDZ1.

* A mirror consumes more disk space but generally performs better with small random reads. For better performance, a mirror is strongly favored over any 
  RAIDZ, particularly for large, uncacheable, random read loads.

* Array sizes beyond 12 disks are not recommended. The recommended number of disks per vdev is between 3 and 9. If you have more disks, use multiple vdevs.

* Some older ZFS documentation recommends that a certain number of disks is needed for each type of RAIDZ in order to achieve optimal performance. On systems
  using LZ4 compression, which is the default for FreeNAS® 9.2.1 and higher, this is no longer true. See
  `ZFS RAIDZ stripe width, or: How I Learned to Stop Worrying and Love RAIDZ <http://blog.delphix.com/matt/2014/06/06/zfs-stripe-width/>`_ for details.

The following resources can also help you determine the RAID configuration best suited to your storage needs:

* `Getting the Most out of ZFS Pools <http://forums.freenas.org/showthread.php?16-Getting-the-most-out-of-ZFS-pools%21>`_

* `A Closer Look at ZFS, Vdevs and Performance <http://constantin.glez.de/blog/2010/06/closer-look-zfs-vdevs-and-performance>`_

.. warning:: NO RAID SOLUTION PROVIDES A REPLACEMENT FOR A RELIABLE BACKUP STRATEGY. BAD STUFF CAN STILL HAPPEN AND YOU WILL BE GLAD THAT YOU BACKED UP YOUR
   DATA WHEN IT DOES. See `Periodic Snapshot Tasks`_ and `Replication Tasks`_ if you would like to use replicated ZFS snapshots as part of your backup
   strategy.

While ZFS provides many benefits, there are some caveats to be aware of:

* At 90% capacity, ZFS switches from performance- to space-based optimization, which has massive performance implications. For maximum write performance and
  to prevent problems with drive replacement, add more capacity before a pool reaches 80%. If you are using iSCSI, it is recommended to not let the pool go
  over 50% capacity to prevent fragmentation issues.
  
* When considering the number of disks to use per vdev, consider the size of the disks and the amount of time required for resilvering, which is the process
  of rebuilding the array. The larger the size of the array, the longer the resilvering time. When replacing a disk in a RAIDZ*, it is possible that another
  disk will fail before the resilvering process completes. If the number of failed disks exceeds the number allowed per vdev for the type of RAIDZ, the data
  in the pool will be lost. For this reason, RAIDZ1 is not recommended for drives over 1 TB in size.
  
* It is recommended to use drives of equal sizes. While ZFS can create a pool using disks of differing sizes, the capacity will be limited by the size of the
  smallest disk.

If you are new to ZFS, the
`Wikipedia entry on ZFS <http://en.wikipedia.org/wiki/Zfs>`_
provides an excellent starting point to learn more about its features. These resources are also useful to bookmark and refer to as needed:

* `FreeBSD ZFS Tuning Guide <http://wiki.freebsd.org/ZFSTuningGuide>`_

* `ZFS Administration Guide <http://download.oracle.com/docs/cd/E19253-01/819-5461/index.html>`_

* `Becoming a ZFS Ninja (video) <http://blogs.oracle.com/video/entry/becoming_a_zfs_ninja>`_

* `Slideshow explaining VDev, zpool, ZIL and L2ARC and other newbie mistakes! <http://forums.freenas.org/threads/slideshow-explaining-vdev-zpool-zil-and-l2arc-for-noobs.7775/>`_

* `A Crash Course on ZFS <http://www.bsdnow.tv/tutorials/zfs>`_

* `ZFS: The Last Word in File Systems - Part 1 (video) <https://www.youtube.com/watch?v=uT2i2ryhCio>`_
