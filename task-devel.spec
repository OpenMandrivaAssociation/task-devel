Name: task-devel
Version: 2014.1
Release: 0.4
Summary: Meta-package installing tools required for development
URL: http://openmandriva.org/
License: GPLv3+
Group: Development/Other
Requires: make
Requires: binutils
Requires: gcc gcc-c++
Requires: clang
Requires: %mklibname -d stdc++
Requires: glibc-devel
Requires: rpm-build
Requires: tar
Requires: cpio
# Not strictly required, but used by a load of build scripts
# and rpmlint...
Requires: python >= 3.0
Requires: python2

%description
Meta-package installing tools required for development

%files
