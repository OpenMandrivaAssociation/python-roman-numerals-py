Name:		python-roman-numerals-py
Version:	3.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/roman_numerals_py/roman_numerals_py-%{version}.tar.gz
Summary:	Manipulate well-formed Roman numerals
URL:		https://pypi.org/project/roman-numerals-py/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Manipulate well-formed Roman numerals

%files
%{py_sitedir}/roman_numerals
%{py_sitedir}/roman_numerals_py-%{version}.dist-info
