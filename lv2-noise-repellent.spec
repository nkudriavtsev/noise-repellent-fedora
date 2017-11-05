Name:           lv2-noise-repellent
Version:        0.1.3f
Release:        1%{?dist}
Summary:        An lv2 plug-in for broadband noise reduction
Group:          Applications/Multimedia
License:        GPLv3.0+
URL:            https://github.com/lucianodato/noise-repellent
Source0:        https://github.com/lucianodato/noise-repellent/archive/%{version}.tar.gz

#BuildRequires:  faust
#BuildRequires:  non-ntk-devel
#BuildRequires:  libsndfile-devel
#BuildRequires:  cairomm-devel
#BuildRequires:  lv2-devel
#BuildRequires:  cmake
Requires:       lv2

%description
An lv2 plug-in for broadband noise reduction.

%prep
sed -i -e  's|lib/|%{_lib}/|g'  -e 's|\-Wall|%{optflags}|g' Makefile

%build
%{cmake}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_libdir}/lv2
make install DESTDIR=%{buildroot}

%files
%doc README.md CHANGELOG LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Nov 05 2017 Nicholas Kudriavtsev <nkudriavtsev@gmail.com>
- Initial rpm build
