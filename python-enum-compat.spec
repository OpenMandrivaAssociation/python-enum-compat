Name:           python-enum-compat
Version:        0.0.3
Release:        1
Summary:        Enum/Enum34 compatibility package
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/jstasiak/enum-compat
Source:         https://files.pythonhosted.org/packages/source/e/enum-compat/enum-compat-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
BuildArch:      noarch

%description
This is a virtual package, its whole purpose is to install enum34 on
Python older than 3.4. On Python 3.4+ it's a no-op.

%prep
%setup -q -n enum-compat-%{version}

%build
%py3_build

%install
%py3_install

%files
%{python_sitelib}/*
