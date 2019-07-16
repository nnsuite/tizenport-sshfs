Name:       sshfs
Summary:    filesystem client based on SSH File Transfer Protocol
Version:    2.10
Release:    0
Group:      Base/File Systems
Packager:	Wook Song <wook16.song@samsung.com>
License:	GPL-2.0
Source0:	sshfs-%{version}.tar.gz
Source1001:	sshfs.manifest
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(glib-2.0)

%description
SSHFS allows you to mount a remote filesystem using SFTP.
Most SSH servers support and enable this SFTP access by default,
so SSHFS is very simple to use - there's nothing to do on the server-side.
It is a TAOS meta repository for system configuration & building-blocks.

%prep
%setup -q
cp %{SOURCE1001} .

%build
autoreconf -fi
%{configure}
%{__make} %{?_smp_mflags}

%install
%{make_install}
rm -rf %{buildroot}%{_mandir}

%files
%{_bindir}/sshfs
