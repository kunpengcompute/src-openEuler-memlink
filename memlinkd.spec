#needsrootforbuild
%global systemctl_bin /usr/bin/systemctl

Summary: UVP memory overcommit services for euleros
Name:    memlinkd
Version: 1.0.0
Release: 210
License: MulanPSL2
ExclusiveArch: aarch64
Group:   System Environment/Daemons
Source0: memlinkd-1.0.0.tar.gz

BuildRequires: libvirt libvirt-devel libboundscheck
BuildRequires: systemd-devel systemd-rpm-macros
BuildRequires: gnutls gnutls-devel cmake CUnit-devel

Requires: libvirt libboundscheck
Requires: systemd

%description
UVP memory overcommit services for euleros

%prep
%setup -q -n memlinkd-1.0.0

%build
rm -rf build
mkdir -p build
cd build
cmake ../src -DFIT_FOR_AARCH64:STRING=TRUE
%make_build

%install
mkdir -p %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}/etc/sysmonitor/process/

install -m 550 build/memlinkd %{buildroot}%{_sbindir}/memlinkd
install -m 644 src/memlinkd.service %{buildroot}%{_unitdir}/
install -m 640 src/memlinkd.conf %{buildroot}%{_sysconfdir}/memlinkd.conf
install -m 600 src/sysmonitor/memlinkd-daemon %{buildroot}/etc/sysmonitor/process/memlinkd-daemon

%files
%{_sbindir}/memlinkd
%{_unitdir}/memlinkd.service
%config(noreplace) %{_sysconfdir}/memlinkd.conf
/etc/sysmonitor/process/memlinkd-daemon

%post
%systemd_post memlinkd.service

%preun
%systemd_preun memlinkd.service

%postun
%systemd_postun_with_restart memlinkd.service

%changelog
* Thu May 21 2026 Leizongkun <leizongkun@huawei.com> - 1.0.0-210
- rename spec and replace tar

* Tue Apr 21 2026 Leizongkun <leizongkun@huawei.com> - 1.0.0-209
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add integration test suite for memlinkd

* Tue Aug 26 2025 Leizongkun <leizongkun@huawei.com> - 1.0.0-208
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add init code of memlinkd
