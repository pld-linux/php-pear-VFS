# TODO
# - check that weird packaging to lib dir
%define		_status		beta
%define		_pearname	VFS
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - Virtual File System API
Summary(pl.UTF-8):	%{_pearname} - API wirtualnego systemu plików
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	5
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b562ab13bcbf96ac48d63fbcda6d8ba4
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/VFS/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php(gettext)
Requires:	php-pear
Requires:	php-pear-Log
Requires:	php-pear-PEAR-core >= 1:1.4.0-0.b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# http://pear.php.net/bugs/bug.php?id=17795
%define		_noautoreq	pear(Horde/Kolab/Storage/List.php) pear(Horde/MIME/Magic.php)

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
%dir %{php_pear_dir}/VFS
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/VFS/*.php
# ???
%dir %{php_pear_dir}/lib
%dir %{php_pear_dir}/lib/VFS
%{php_pear_dir}/lib/VFS/kolab.php

%{php_pear_dir}/data/%{_pearname}
