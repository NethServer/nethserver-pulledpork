Summary: NethServer pulledpork configuration
Name: nethserver-pulledpork
Version: 2.0.0
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

Requires: pulledpork
Requires: nethserver-base
Requires: perl-LWP-Protocol-https
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
* Wed Sep 28 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.0-1
- Replace Snort with Suricata - NethServer/dev#5104

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

* Tue Nov 10 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- pulledpork config: update url for community download - Bug #3301 [NethServer]
- Rotate /var/log/sid_changes.log - Enhancement #3273 [NethServer]

* Tue May 19 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- pulledpork drop policy should reflect snort policy - Enhancement #3162 [NethServer]

* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- IDS/IPS (snort) - Feature #1771 [NethServer]

