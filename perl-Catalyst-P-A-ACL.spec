%define	module	Catalyst-Plugin-Authorization-ACL
%define abbrevname Catalyst-P-A-ACL
%define name	perl-%{abbrevname}
%define	modprefix Catalyst

%define version 0.08
%define release %mkrel 4

Summary:	ACL support for Catalyst applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.7
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::Throwable)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Tree::Simple::Visitor::FindByPath)
BuildRequires:	perl(Tree::Simple::Visitor::GetAllDescendents)
Provides:	perl-%{module}
Obsoletes:	perl-%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
This module provides Access Control List style path protection, with
arbitrary rules for Catalyst applications. It operates only on the
Catalyst private namespace, at least at the moment.

%define _requires_exceptions perl(A

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%Changelog
* Sat Aug 05 2006 Scott Karns <scottk@mandriva.org> 0.08-1mdv2007.0
- Version 0.08
- Renamed from perl-Catalyst-Plugin-Authorization-ACL to meet
  joliet filename length constraint.
