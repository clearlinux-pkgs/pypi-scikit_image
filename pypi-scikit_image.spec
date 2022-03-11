#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-scikit_image
Version  : 0.19.2
Release  : 72
URL      : https://files.pythonhosted.org/packages/83/7d/756dcbf1f2fcbfd60e14842aeadefa2354eff714ed4ec3ae7a107a5787d1/scikit-image-0.19.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/83/7d/756dcbf1f2fcbfd60e14842aeadefa2354eff714ed4ec3ae7a107a5787d1/scikit-image-0.19.2.tar.gz
Summary  : Image processing in Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-scikit_image-bin = %{version}-%{release}
Requires: pypi-scikit_image-license = %{version}-%{release}
Requires: pypi-scikit_image-python = %{version}-%{release}
Requires: pypi-scikit_image-python3 = %{version}-%{release}
Requires: pypi(cloudpickle)
Requires: pypi(dask)
Requires: pypi(imageio)
Requires: pypi(matplotlib)
Requires: pypi(networkx)
Requires: pypi(pillow)
Requires: pypi(pywavelets)
Requires: pypi(scipy)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(dask)
BuildRequires : pypi(imageio)
BuildRequires : pypi(networkx)
BuildRequires : pypi(numpy)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pillow)
BuildRequires : pypi(pythran)
BuildRequires : pypi(pywavelets)
BuildRequires : pypi(scikit_learn)
BuildRequires : pypi(scipy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tifffile)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython

%description
# scikit-image: Image processing in Python
[![Image.sc forum](https://img.shields.io/badge/dynamic/json.svg?label=forum&url=https%3A%2F%2Fforum.image.sc%2Ftags%2Fscikit-image.json&query=%24.topic_list.tags.0.topic_count&colorB=brightgreen&suffix=%20topics&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAABPklEQVR42m3SyyqFURTA8Y2BER0TDyExZ+aSPIKUlPIITFzKeQWXwhBlQrmFgUzMMFLKZeguBu5y+//17dP3nc5vuPdee6299gohUYYaDGOyyACq4JmQVoFujOMR77hNfOAGM+hBOQqB9TjHD36xhAa04RCuuXeKOvwHVWIKL9jCK2bRiV284QgL8MwEjAneeo9VNOEaBhzALGtoRy02cIcWhE34jj5YxgW+E5Z4iTPkMYpPLCNY3hdOYEfNbKYdmNngZ1jyEzw7h7AIb3fRTQ95OAZ6yQpGYHMMtOTgouktYwxuXsHgWLLl+4x++Kx1FJrjLTagA77bTPvYgw1rRqY56e+w7GNYsqX6JfPwi7aR+Y5SA+BXtKIRfkfJAYgj14tpOF6+I46c4/cAM3UhM3JxyKsxiOIhH0IO6SH/A1Kb1WBeUjbkAAAAAElFTkSuQmCC)](https://forum.image.sc/tags/scikit-image)
[![Stackoverflow](https://img.shields.io/badge/stackoverflow-Ask%20questions-blue.svg)](https://stackoverflow.com/questions/tagged/scikit-image)
[![project chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://skimage.zulipchat.com)
[![codecov.io](https://codecov.io/github/scikit-image/scikit-image/coverage.svg?branch=main)](https://codecov.io/github/scikit-image/scikit-image?branch=main)

%package bin
Summary: bin components for the pypi-scikit_image package.
Group: Binaries
Requires: pypi-scikit_image-license = %{version}-%{release}

%description bin
bin components for the pypi-scikit_image package.


%package license
Summary: license components for the pypi-scikit_image package.
Group: Default

%description license
license components for the pypi-scikit_image package.


%package python
Summary: python components for the pypi-scikit_image package.
Group: Default
Requires: pypi-scikit_image-python3 = %{version}-%{release}

%description python
python components for the pypi-scikit_image package.


%package python3
Summary: python3 components for the pypi-scikit_image package.
Group: Default
Requires: python3-core
Provides: pypi(scikit_image)
Requires: pypi(imageio)
Requires: pypi(networkx)
Requires: pypi(numpy)
Requires: pypi(packaging)
Requires: pypi(pillow)
Requires: pypi(pywavelets)
Requires: pypi(scipy)
Requires: pypi(tifffile)

%description python3
python3 components for the pypi-scikit_image package.


%prep
%setup -q -n scikit-image-0.19.2
cd %{_builddir}/scikit-image-0.19.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647038232
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
#make test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-scikit_image
cp %{_builddir}/scikit-image-0.19.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-scikit_image/9c5c45c8433b83e2ac82898a64d41746dec6f2fc
cp %{_builddir}/scikit-image-0.19.2/doc/tools/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-scikit_image/fb50fd87a0153fd93be5975f012fa41347306040
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/skivi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-scikit_image/9c5c45c8433b83e2ac82898a64d41746dec6f2fc
/usr/share/package-licenses/pypi-scikit_image/fb50fd87a0153fd93be5975f012fa41347306040

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
