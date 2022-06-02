Name:           python-pybtex-docutils
Version:        1.0.1
Release:        1
Summary:        A docutils backend for pybtex
License:        MIT
URL:            https://github.com/mcmtroffaes/pybtex-docutils
Source0:        https://files.pythonhosted.org/packages/41/3b/69c21deab7974b76018124b441c059edc6d6cec970ac038e5f62682eac8a/pybtex-docutils-1.0.1.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pybtex python3-setuptools python3-six python3-sphinx
BuildRequires:  python3-devel python3-docutils python3-nose2 python3-pytest

%description
This package contains a docutils backend for pybtex, a BibTeX-compatible bibliography processor
written in Python. Bibliographic references in BibTeX format (or any other format supported by
pybtex) can be inserted into python documentation to be rendered by docutils.

%package -n     python3-pybtex-docutils
Summary:        Docutils backend for pybtex
Requires:       python3-docutils python3-pybtex python3-six
Provides:       bundled(jquery) bundled(js-underscore)
%{?python_provide:%python_provide python3-pybtex-docutils}

%description -n python3-pybtex-docutils
This package contains a docutils backend for pybtex, a BibTeX-compatible bibliography processor
written in Python. Bibliographic references in BibTeX format (or any other format supported by
pybtex) can be inserted into python documentation to be rendered by docutils.

%prep
%autosetup -c
sed -i "s/'default'/'alabaster'/" pybtex-docutils-%{version}/doc/conf.py
sed -i 's/"rb"/"rt"/' pybtex-docutils-%{version}/doc/conf.py

%build
cd pybtex-docutils-%{version}
%py3_build
PYTHONPATH=$PWD make -C doc html SPHINXBUILD=%{_bindir}/sphinx-build-%{python3_version}
cd -

%install
cd pybtex-docutils-%{version}
%py3_install
cd -

%check
cd pybtex-docutils-%{version}
PYTHONPATH=$PWD nose2-%{python3_version} -v
cd -

%files -n python3-pybtex-docutils
%doc pybtex-docutils-%{version}/doc/_build/html/* pybtex-docutils-%{version}/LICENSE.rst
%{python3_sitelib}/pybtex_docutils*
%{python3_sitelib}/pybtex_docutils/*

%changelog
* Tue May 31 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 1.0.1-1
- update to 1.0.1

* Fri Mar 6 2020 Ling Yang <lingyang2@huawei.com> - 0.2.1-11
- Package Init
