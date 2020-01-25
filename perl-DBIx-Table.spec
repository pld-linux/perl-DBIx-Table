#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	DBIx
%define		pnam	Table
Summary:	DBIx::Table - class used to represent DBI database tables
Summary(pl.UTF-8):	DBIx::Table - klasa służąca do reprezentowania tabel DBI
Name:		perl-DBIx-Table
Version:	0.04
Release:	5
# same aa perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82757c208b63ef2e3b6dad59892c2c7c
URL:		http://search.cpan.org/dist/DBIx-Table/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Table is a class designed to act as an abstraction layer around
a fairly large subset of SQL queries. It is called 'Table' because it
is primarily designed such that a single subclass provides an
object-oriented interface to a single database table. The module is
flexible enough, though, that it can be used to abstract most any
schema in a way that is comfortable to the perl coder who is not
familiar with the underlying schema, or even SQL.

%description -l pl.UTF-8
DBIx::Table to klasa zaprojektowana tak, by służyła jako warstwa
abstrakcji dla dość dużego podzbioru zapytań SQL. Nazywa się "Table",
ponieważ jest zaprojektowana zasadniczo tak, że pojedyncza podklasa
udostępnia zorientowany obiektowo interfejs do pojedynczej tabeli bazy
danych. Moduł jest jednak na tyle elastyczny, że może być używany do
wyabstrahowania prawie każdego schematu w sposób wygodny dla perlowego
kodera niezbyt zaznajomionego z podstawowymi schematami czy nawet
SQL-em.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
