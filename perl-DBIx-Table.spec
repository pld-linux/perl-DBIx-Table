#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Table
Summary:	DBIx::Table - Class used to represent DBI database tables
Summary(pl):	DBIx::Table - klasa u�ywana do reprezentowania tabel DBI
Name:		perl-DBIx-Table
Version:	0.04
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
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

%description -l pl
DBIx::Table to klasa zaprojektowana tak, by s�u�y�a jako warstwa
abstrakcji dla do�� du�ego podzbioru zapyta� SQL. Nazywa si� "Table",
poniewa� jest zaprojektowana zasadniczo tak, �e pojedyncza podklasa
udost�pnia zorientowany obiektowo interfejs do pojedynczej tabeli bazy
danych. Modu� jest jednak na tyle elastyczny, �e mo�e by� u�ywany do
wyabstrahowania prawie ka�dego schematu w spos�b wygodny dla perlowego
kodera niezbyt zaznajomionego z podstawowymi schematami czy nawet
SQL-em.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
