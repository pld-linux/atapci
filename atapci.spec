Summary:	ATA PCI Utilities
Summary(pl.UTF-8):	Narzędzia ATA PCI
Name:		atapci
Version:	0.52
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://home.elka.pw.edu.pl/~bzolnier/atapci/%{name}-%{version}.tar.bz2
# Source0-md5:	93b905034584cdafd30a76362538036b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
atapci is a userland port of Linux kernel code responsible for
displaying /proc/ide/ chipset specific information, formerly this
program was called ide-info

%description -l pl.UTF-8
atapci jest odpowiednikiem kodu jądra odpowiedzialnego za wyświetlanie
informacji z /proc/ide/ specyficznej dla określonych chipsetów.

%prep
%setup -q

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install atapci		$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README STATUS
%attr(755,root,root) %{_sbindir}/*
