Name: task-devel
Version: 2015.0
Release: 0.8
Summary: Meta-package installing tools required for development
URL: http://openmandriva.org/
License: GPLv3+
Group: Development/Other
Requires: make
Requires: binutils
Requires: gcc gcc-c++
Requires: llvm-polly
Requires: clang
Requires: %mklibname -d stdc++
Requires: glibc-devel
Requires: rpm-build
# (tpg) we use bsdtar from libarchive as a replacement for tar
# originall tar was renamed to gnutar
# bsdtar froom libarchive provides tar, and bsdtar
%if "%{distepoch}" >= "2015.0"
Requires: bsdtar
%else
Requires: tar
%endif
Requires: cpio
# Not strictly required, but used by a load of build scripts
# and rpmlint...
Requires: python >= 3.0

%description
Meta-package installing tools required for development.

%files
