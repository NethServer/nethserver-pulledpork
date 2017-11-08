Summary: NethServer pulledpork configuration
Name: nethserver-pulledpork
Version: 2.1.1
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
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist
mkdir -p %{buildroot}/etc/suricata/rules/iplists
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%dir /etc/suricata/rules/iplists

%changelog
* Wed Nov 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.1.1-1
- Suricata rules download error - Bug NethServer/dev#5370

* Fri Oct 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.1.0-1
- EveBox - NethServer/dev#5346

* Wed Jan 25 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.1-1
- Daily cron email about pulledpork.pl - Bug NethServer/dev#5191
- Pulledpork: wrong configuration - Bug NethServer/dev#5199

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

