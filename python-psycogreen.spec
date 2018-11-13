# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Enable psycopg2 to work with coroutine libraries
Name:		python-psycogreen
Version:	1.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/psycogreen/psycogreen-%{version}.tar.gz
# Source0-md5:	7a32d8f5abdb4ce17ac512f8c8a698a9
URL:		https://bitbucket.org/dvarrazzo/psycogreen/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
Requires:	python-psycopg2 >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The psycogreen package enables psycopg2 to work with coroutine
libraries, using asynchronous calls internally but offering a blocking
interface so that regular code can run unmodified.

%package -n python3-psycogreen
Summary:	Enable psycopg2 to work with coroutine libraries
Group:		Libraries/Python
Requires:	python3-psycopg2 >= 2.2

%description -n python3-psycogreen
The psycogreen package enables psycopg2 to work with coroutine
libraries, using asynchronous calls internally but offering a blocking
interface so that regular code can run unmodified.

%prep
%setup -q -n psycogreen-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/psycogreen
%{py_sitescriptdir}/psycogreen-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-psycogreen
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/psycogreen
%{py3_sitescriptdir}/psycogreen-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
