Name: task-devel
Version: %distro_release
Release: 2
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

%description
Meta-package installing tools required for development

%files
