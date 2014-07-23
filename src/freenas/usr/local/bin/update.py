#!/usr/local/bin/python -R

import os, sys, getopt

sys.path.append("/usr/local/lib")

import freenasOS.Manifest as Manifest
import freenasOS.Configuration as Configuration
import freenasOS.Package as Installer

def usage():
    print >> sys.stderr, "Usage: %s [-R root] [-M manifest_file] <cmd>, where cmd is one of:" % sys.argv[0]
    print >> sys.stderr, "\tcheck\tCheck for updates"
    print >> sys.stderr, "\tupdate\tDo an update"
    print >> sys.stderr, "\tinstall\tInstall"
    sys.exit(1)

def CheckForUpdates(root = None, handler = None):
    """
    Check for an updated manifest.
    Very simple, uses the configuration module.
    Returns the new manifest if there is an update,
    and None otherwise.
    (It determines if there is an update if the latest-found
    manifeset's sequence number is larger than the current
    sequence number.)
    The optional argument handler is a function that
    will be called for each difference in the new manifest
    (if there is one); it will be called with three
    arguments:  operation, package, old package.
    operation will be "delete", "upgrade", or "install";
    old package will be None for delete and install.
    """
    conf = Configuration.Configuration(root)
    cur = conf.SystemManifest()
#    m = conf.FindNewerManifest(cur.Sequence())
    m = conf.FindLatestManifest()
    print >> sys.stderr, "Current sequence = %d, available sequence = %d" % (cur.Sequence(), m.Sequence() if m is not None else 0)
    if handler is not None and m is not None and cur.Sequence() != m.Sequence():
        diffs = Manifest.CompareManifests(cur, m)
        for (pkg, op, old) in diffs:
            handler(op, pkg, old)

    if m is not None and m.Sequence() > cur.Sequence():
        return m
    return None

def Update(root = None):
    """
    Perform an update.  Calls CheckForUpdates() first, to see if
    there are any. If there are, then magic happens.
    """
    new_man = CheckForUpdates(root)
    if new_man is None:
        return
    print "I MUST UPDATE OR MY HEAD WILL EXPLODE"
    return
try:
    opts, args = getopt.getopt(sys.argv[1:], "qvdR:M:")
except getopt.GetoptError as err:
    print str(err)
    usage()
            
root = None
manifile = None
            
for o, a in opts:
    if o == "-v":
        verbose += 1
    elif o == "-q":
        quiet = True
    elif o == "-d":
        debug += 1
    elif o == "-R":
        root = a
    elif o == "-M":
        manifile = a
    else:
        assert False, "unhandled option"

if root is not None and os.path.isdir(root) == False:
    print >> sys.stderr, "Specified root (%s) does not exist" % root
    sys.exit(1)

if len(args) != 1:
    usage()

if args[0] == "check":
    def Handler(op, pkg, old):
        if op == "upgrade":
            print "%s:  %s -> %s" % (pkg.Name(), old.Version(), pkg.Version())
        else:
            print "%s:  %s %s" % (pkg.Name(), op, pkg.Version())

    if verbose > 0 or debug > 0:
        pfcn = Handler
    else:
        pfcn = None
    r = False if CheckForUpdates(root, pfcn) is None else True

    print >> sys.stderr, "Newer manifest found" if r else "No newer manifest found"
    if r:   
        sys.exit(0)
    else:
        sys.exit(1)
elif args[0] == "update":
    Update(root)

else:
    usage()
