%define	upstream_name	 Catalyst-Plugin-Authorization-ACL
%define abbrev_name      Catalyst-P-A-ACL
%define upstream_version 0.16

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(A(.*)\\)'
%else
%define _requires_exceptions perl(A
%endif

Name:		perl-%{abbrev_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	ACL support for Catalyst applications

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.7
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Authorization::Roles)
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::Throwable)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:	perl(Tree::Simple::Visitor::FindByPath)
BuildRequires:	perl(Tree::Simple::Visitor::GetAllDescendents)

BuildArch:	noarch
%rename	perl-%{upstream_name}

%description
This module provides Access Control List style path protection, with
arbitrary rules for Catalyst applications. It operates only on the
Catalyst private namespace, at least at the moment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


