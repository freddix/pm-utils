%define		pm_quirks	20100316

Summary:	Power management utilities and scripts
Name:		pm-utils
Version:	1.4.1
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://pm-utils.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	1742a556089c36c3a89eb1b957da5a60
Source10:	http://pm-utils.freedesktop.org/releases/pm-quirks-%{pm_quirks}.tar.gz
# Source10-md5:	9e960d066959b88727e9259a0f04161f
Source1:	%{name}-hibernate.pamd
Source2:	%{name}-powersave.pamd
Source3:	%{name}-suspend-hybrid.pamd
Source4:	%{name}-suspend.pamd
Patch0:		%{name}-use-bash.patch
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pm-utils package contains utilities and scripts useful for tasks
related to power management.

%package devel
Summary:	pm-utils development file(s)
Group:		Development/Libraries
# don't require base, only pc file

%description devel
pm-utils development file(s)

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pam.d,%{_libdir}/pm-utils/video-quirks}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/pm-hibernate
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/pm-powersave
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/pm-suspend-hybrid
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/pm-suspend
tar -xf %{SOURCE10} -C $RPM_BUILD_ROOT%{_libdir}/pm-utils/video-quirks

rm -f $RPM_BUILD_ROOT%{_libdir}/pm-utils/sleep.d/{01grub,49bluetooth,60sysfont,65alsa,90clock}
rm -f $RPM_BUILD_ROOT%{_libdir}/pm-utils/bin/pm-pmu
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* pm/HOWTO.* TODO

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/pm-*

%dir %{_libdir}/pm-utils
%dir %{_libdir}/pm-utils/bin
%dir %{_libdir}/pm-utils/module.d
%dir %{_libdir}/pm-utils/power.d
%dir %{_libdir}/pm-utils/sleep.d
%dir %{_sysconfdir}/pm
%dir %{_sysconfdir}/pm/config.d
%dir %{_sysconfdir}/pm/power.d
%dir %{_sysconfdir}/pm/sleep.d

%attr(755,root,root) %{_libdir}/pm-utils/module.d/kernel
%attr(755,root,root) %{_libdir}/pm-utils/module.d/tuxonice
%attr(755,root,root) %{_libdir}/pm-utils/module.d/uswsusp

%{_libdir}/pm-utils/defaults
%{_libdir}/pm-utils/functions
%{_libdir}/pm-utils/pm-functions
%{_libdir}/pm-utils/video-quirks

%attr(755,root,root) %{_libdir}/pm-utils/bin/pm-action
%attr(755,root,root) %{_libdir}/pm-utils/bin/pm-reset-swap
%attr(755,root,root) %{_libdir}/pm-utils/power.d/*
%attr(755,root,root) %{_libdir}/pm-utils/sleep.d/*

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/pm-hibernate
%attr(755,root,root) %{_sbindir}/pm-powersave
%attr(755,root,root) %{_sbindir}/pm-suspend
%attr(755,root,root) %{_sbindir}/pm-suspend-hybrid

%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*pc

