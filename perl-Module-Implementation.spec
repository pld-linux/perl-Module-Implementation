#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Implementation
Summary:	Module::Implementation - loads one of several alternate underlying implementations for a module
Summary(pl.UTF-8):	Module::Implementation - wczytywanie jednej z kilku alternatywnych implementacji modułu
Name:		perl-Module-Implementation
Version:	0.09
Release:	1
License:	Artistic v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	52e3fe0ca6b1eff0488d59b7aacc0667
URL:		http://search.cpan.org/dist/Module-Implementation/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Module-Runtime >= 0.012
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl-Test-Fatal >= 0.006
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module abstracts out the process of choosing one of several
underlying implementations for a module. This can be used to provide
XS and pure Perl implementations of a module, or it could be used to
load an implementation for a given OS or any other case of needing to
provide multiple implementations.

This module is only useful when you know all the implementations ahead
of time. If you want to load arbitrary implementations then you
probably want something like a plugin system, not this module.

%description -l pl.UTF-8
Ten moduł abstrahuje proces wyboru jednego z kilku różnych
implementacji modułu. Może być wykorzystany do zapewneinia
implementacji XS oraz czysto perlowej jakiegoś modułu, albo wczytania
implementacji dla danego systemu operacyjnego, albo w innym przypadku
wymagającym wielu implementacji.

Moduł jest przydatny tylko jeśli z góry znane są wszystkie
implementacje. Jeśli mają być wczytywane dowolne implementacje,
lepiej użyć systemu wtyczek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Module/Implementation.pm
%{_mandir}/man3/Module::Implementation.3pm*
