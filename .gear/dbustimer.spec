Name: dbustimer
Version: 0.4
Release: alt1

Summary: Display sytem time
License: GPLv3+
Group: Other
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: rpm-build-python3

%description
This program displays notifications about the system time with a frequency of one hour.

Source: %name-%version.tar
%prep
%setup -q

%install


mkdir -p \
        %buildroot%python3_sitelibdir_noarch/%name/
install -Dm0755 script_dbus.py \
        %buildroot%python3_sitelibdir_noarch/%name/

mkdir -p \
        %buildroot%_sysconfdir/xdg/systemd/user/
cp script_dbus.timer script_dbus.service \
        %buildroot%_sysconfdir/xdg/systemd/user/



%changelog
* Thu Nov 16 2026 step <stepmr4@gmail.com> 0.4-alt1
