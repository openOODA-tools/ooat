Name:           ooat
Version:        0.2.0
Release:        1%{?dist}
Summary:        Single-run scheduled command coordinator backed by transient systemd timer units.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooat
Source0:        ooat-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooat is a sovereign, capability-bounded ONESHOT TIMER written
in pure openOODA, featuring zero ambient authority, systemd timer integration,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooat
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooat-uninstall

%files
/usr/bin/ooat
/usr/bin/ooat-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to v0.2.0 with transient systemd timer coordination and MCP stdio server
