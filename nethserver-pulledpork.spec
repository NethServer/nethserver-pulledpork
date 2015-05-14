Summary: NethServer pulledpork configuration
Name: nethserver-pulledpork
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

Requires: pulledpork
Requires: nethserver-base
BuildRequires: nethserver-devtools

%description
NethServer pulledpork configuration

%prep
%setup -q

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%config(noreplace) /etc/snort/rules/snort.rules
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- IDS/IPS (snort) - Feature #1771 [NethServer]

