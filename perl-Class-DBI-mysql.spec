%define upstream_name    Class-DBI-mysql
%define upstream_version 1.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Class::DBI extension for MySQL
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::DBI)

BuildArch:	noarch

%description
This is an extension to Class::DBI, containing several functions and
optimisations for the MySQL database. Instead of setting Class::DBI as your
base class, use this instead.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# requires a running mysql server

%install
%makeinstall_std

%files
%doc Changes README INSTALL
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.0.0-6mdv2011.0
+ Revision: 680809
- mass rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-5mdv2011.0
+ Revision: 505426
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.00-4mdv2010.0
+ Revision: 430327
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.00-3mdv2009.0
+ Revision: 241179
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2008.0
+ Revision: 91095
- import perl-Class-DBI-mysql


* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2008.0
- first mdv release
