%define module  Class-DBI-mysql
%define name    perl-%{module}
%define version 1.00
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Class::DBI extension for MySQL
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildRequires:	perl(Class::DBI)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is an extension to Class::DBI, containing several functions and
optimisations for the MySQL database. Instead of setting Class::DBI as your
base class, use this instead.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# requires a running mysql server

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README INSTALL
%{perl_vendorlib}/Class
%{_mandir}/*/*

