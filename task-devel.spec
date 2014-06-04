Name: task-devel
Version: 2014.1
Release: 0.1
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
Requires: bsdtar bsdcpio
BuildRequires: bsdtar bsdcpio

%description
Meta-package installing tools required for development

%files
