Summary: NethServer pulledpork configuration
Name: nethserver-pulledpork
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Group: Networking/Daemons
Source0: %{name}-%{version}.tar.gz
Packager: Giacomo Sanchietti <giacomo@nethesis.it>

BuildArch: noarch

Requires: pulledpork
Requires: nethserver-base

BuildRequires: nethserver-devtools
AutoReq: no

%description
NethServer pulledpork configuration


%prep
%setup -q

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist


%post

%preun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%config(noreplace) /etc/snort/rules/snort.rules

%changelog
