Name:           python-pybtex-docutils
Version:        0.2.1
Release:        11
Summary:        A docutils backend for pybtex
License:        MIT
URL:            https://github.com/mcmtroffaes/pybtex-docutils
Source0:        https://files.pythonhosted.org/packages/source/p/pybtex-docutils/pybtex-docutils-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel python2-docutils python2-nose python2-pybtex python2-setuptools
BuildRequires:  python3-pybtex python3-setuptools python3-six python3-sphinx python3-nose-cov
BuildRequires:  python2-six python2-sphinx python3-devel python3-docutils python3-nose

%description
This package contains a docutils backend for pybtex, a BibTeX-compatible bibliography processor
written in Python. Bibliographic references in BibTeX format (or any other format supported by
pybtex) can be inserted into python documentation to be rendered by docutils.

%package -n     python2-pybtex-docutils
Summary:        Docutils backend for pybtex
Requires:       python2-docutils python2-pybtex python2-six
Provides:       bundled(jquery) bundled(js-underscore)
%{?python_provide:%python_provide python2-pybtex-docutils}

%description -n python2-pybtex-docutils
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
cp -a pybtex-docutils-%{version} python3-pybtex-docutils-%{version}
sed -i 's/"rb"/"rt"/' python3-pybtex-docutils-%{version}/doc/conf.py

%build
cd pybtex-docutils-%{version}
%py2_build
PYTHONPATH=$PWD make -C doc html SPHINXBUILD=%{_bindir}/sphinx-build-%{python2_version}
cd -
cd python3-pybtex-docutils-%{version}
%py3_build
PYTHONPATH=$PWD make -C doc html SPHINXBUILD=%{_bindir}/sphinx-build-%{python3_version}
cd -

%install
cd pybtex-docutils-%{version}
%py2_install
cd -
cd python3-pybtex-docutils-%{version}
%py3_install
cd -

%check
cd pybtex-docutils-%{version}
PYTHONPATH=$PWD nosetests-%{python2_version} -v
cd -
cd python3-pybtex-docutils-%{version}
PYTHONPATH=$PWD nosetests-%{python3_version} -v
cd -

%files -n python2-pybtex-docutils
%doc pybtex-docutils-%{version}/doc/_build/html/* pybtex-docutils-%{version}/LICENSE.rst
%{python2_sitelib}/pybtex_docutils*

%files -n python3-pybtex-docutils
%doc python3-pybtex-docutils-%{version}/doc/_build/html/* python3-pybtex-docutils-%{version}/LICENSE.rst
%{python3_sitelib}/pybtex_docutils*
%{python3_sitelib}/__pycache__/pybtex_docutils*

%changelog
* Fri Mar 6 2020 Ling Yang <lingyang2@huawei.com> - 0.2.1-11
- Package Init
