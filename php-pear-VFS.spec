%include	/usr/lib/rpm/macros.php
%define         _class          VFS
%define		_status		beta
%define		_pearname	%{_class}
Summary:	%{_pearname} - Virtual File System API
Summary(pl):	%{_pearname} - API Wirtualnego Systemu Plików
Name:		php-pear-%{_pearname}
Version:	0.0.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5d2660a9a395a284de73842045edaf50
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet dostarcza API Wirtualnego systemu plików, ze wsparciem dla:
- SQL
- FTP
- Lokalnych systemów plików
- Hybrydy SQL i systemu plików.

... w przysz³o¶ci te¿ dla innych. Zapis/odczt/listowanie plików jest
wspierane, oraz dostêpny jest interfejs do listowania katalogów oparty
na obiektach, jak i na tablicy.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php                         $RPM_BUILD_ROOT%{php_pear_dir}
install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
