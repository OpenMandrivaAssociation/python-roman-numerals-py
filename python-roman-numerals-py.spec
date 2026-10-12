Name:		python-roman-numerals-py
Version:	4.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/roman_numerals_py/roman_numerals_py-%{version}.tar.gz
Summary:	Manipulate well-formed Roman numerals
URL:		https://pypi.org/project/roman-numerals-py/
License:	0BSD OR CC0-1.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python
BuildArch:	noarch

%description
Manipulate well-formed Roman numerals

%files
# 4.1.0 is a dependency shim. The importable module is roman-numerals.
%{py_sitedir}/roman_numerals_py-%{version}.dist-info
