%define	upstream_name	 Catalyst-Plugin-Authorization-ACL
%define abbrev_name      Catalyst-P-A-ACL
%define upstream_version 0.11

Name:		perl-%{abbrev_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	ACL support for Catalyst applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.7
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::Throwable)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Tree::Simple::Visitor::FindByPath)
BuildRequires:	perl(Tree::Simple::Visitor::GetAllDescendents)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildArch:	noarch
Provides:	perl-%{upstream_name}
Obsoletes:	perl-%{upstream_name}


%description
This module provides Access Control List style path protection, with
arbitrary rules for Catalyst applications. It operates only on the
Catalyst private namespace, at least at the moment.

%define _requires_exceptions perl(A

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst

%Changelog
* Sat Aug 05 2006 Scott Karns <scottk@mandriva.org> 0.08-1mdv2007.0
- Version 0.08
- Renamed from perl-Catalyst-Plugin-Authorization-ACL to meet
  joliet filename length constraint.
