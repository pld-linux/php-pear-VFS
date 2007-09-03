%include	/usr/lib/rpm/macros.php
%define		_class		VFS
%define		_status		beta
%define		_pearname	%{_class}
Summary:	%{_pearname} - Virtual File System API
Summary(pl.UTF-8):	%{_pearname} - API wirtualnego systemu plików
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c38b1f577d98f1185df1b9b65707d8c6
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/VFS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gettext)
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Log
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Virtual File System API, with backends for:
- SQL
- FTP
- Local Filesystems
- Hybrid SQL and filesystem

... and more planned. Reading/writing/listing of files are all
supported, and there are both object-based and array-based interfaces
to directory listing.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza API Wirtualnego systemu plików, ze wsparciem dla:
- SQL
- FTP
- lokalnych systemów plików
- hybrydy SQL i systemu plików.

... w przyszłości też dla innych. Obsługiwane są zapis, odczyt i
listowanie plików oraz dostępny jest interfejs do listowania katalogów
oparty zarówno na obiektach, jak i na tablicy.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}
%patch0 -p2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php

%{php_pear_dir}/data/%{_pearname}
