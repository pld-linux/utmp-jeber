Summary:	Print and optionally remove broken UTMP entries
Summary(pl):	Wy�wietl i opcjonalnie usu� wadliwe wpisy UTMP
Name:		utmp-jeber
Version:	1.0.13
Release:	3
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.pld.org.pl/software/utmp-jeber/%{name}-%{version}.tar.gz
# Source0-md5:	e1c8b052a29c6fb7160123400cda5452
Patch0:		%{name}-multiline.patch
URL:		http://utmp-jeber.pld.org.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UTMP Jeber is a small tool which prints broken entries found in UTMP.
It has various methods of process analysis, which you can select using
command line arguments. It optionally removes broken entries.

%description -l pl
UTMP Jeber to ma�e narz�dzie, kt�re wy�wietla uszkodzone wpisy
znalezione w UTMP. Posiada ono par� metod analizowania proces�w, a ich
wyboru mo�esz dokona� u�ywaj�c argument�w linii polece�. Jeber
opcjonalnie potrafi usuwa� uszkodzone wpisy.

%package cron
Summary:	cron script for UTMP Jeber
Summary(pl):	Skrypt cyklicznego wykonywania dla UTMP Jeber
Group:		Applications/System
Requires:	%{name} = %{version}
Requires:	crontabs
Requires:	crondaemon
Requires:	syslogdaemon

%description cron
This package contains a script, which runs UTMP Jeber in batch mode
and reports actions (if any) via syslog. The script is run
periodicaly, every hour using cron.

%description cron -l pl
Ten pakiet zawiera skrypt, kt�ry uruchamia UTMP Jebera w trybie
wsadowym i zg�asza ewentualnie podj�te dzia�ania (je�li jakie�
wyst�pi�) poprzez demona syslog. Skrypt jest co godzin� uruchamiany
przy u�yciu demona cron.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--with-utmp-file=/var/run/utmpx

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/cron.hourly

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.cron $RPM_BUILD_ROOT/etc/cron.hourly/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%doc %lang(pl) README.polish
%attr(755,root,root) %{_bindir}/*

%files cron
%defattr(644,root,root,755)
%attr(755,root,root) /etc/cron.hourly/%{name}
