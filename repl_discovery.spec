#
# spec file for package innotop
#
Name:      repl_discovery
Summary:   A simple tool for discover MySQL replication topology.
Version:   0.1.1
Release:   1%{?dist}
Vendor:    zhechen <chenzhe07@gmail.com>
License:   Apache
Group:     System/Monitoring
URL:       http://highdb.com/
Buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
Buildarch: noarch
Source:    %{name}-%{version}.tar.gz
BuildRequires: perl-ExtUtils-MakeMaker, make
BuildRequires: perl-DBI, perl-DBD-MySQL, perl-TermReadKey
Requires: perl-DBI, perl-DBD-MySQL, perl-TermReadKey
%if 0%{?rhel} > 4
%endif


%define filelist %{name}-%{version}-filelist

%description
A simple tool for discover MySQL replication topology.

%prep
%setup

%build
grep -rsl '^#!.*perl' . |
grep -v '.bak$' |xargs --no-run-if-empty \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL `%{__perl} -MExtUtils::MakeMaker -e ' print qq|PREFIX=%{buildroot}%{_prefix}| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '`
%{__make} 

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall} `%{__perl} -MExtUtils::MakeMaker -e ' print \$ExtUtils::MakeMaker::VERSION <= 6.05 ? qq|PREFIX=%{buildroot}%{_prefix}| : qq|DESTDIR=%{buildroot}| '`

cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

# SuSE Linux

if [ -e /etc/SuSE-release -o -e /etc/UnitedLinux-release ]
then
    %{__mkdir_p} %{buildroot}/var/adm/perl-modules
    fname=`find %{buildroot} -name "perllocal.pod" | head -1`
    if [ -f "$fname" ] ; then                             \
        %{__cat} `find %{buildroot} -name "perllocal.pod"`  \
        | %{__sed} -e s+%{buildroot}++g                     \
        < /dev/null                                         \
        > %{buildroot}/var/adm/perl-modules/%{name} ;      \
    fi
fi

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

# no empty directories
find %{buildroot}%{_prefix}             \
    -type d -depth                      \
    -exec rmdir {} \; 2>/dev/null

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    print "%doc  Changelog";
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share|;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

%changelog
* Mon Dec 14 2015 zhe chen <chenzhe07@pwrd.com>
- v0.1.1
 - recurion find top master;
 - support hierarchical level check;
 - support multi master check;

* Thu Dec 10 2015 zhe chen <chenzhe07@pwrd.com>
- v0.1.0
 - init version
