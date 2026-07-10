%global tl_name babel-greek
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.15
Release:	%{tl_revision}.1
Summary:	Babel support for the Greek language and script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/greek
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides comprehensive support for the Greek language and
script via the Babel system. Document authors can select between the
monotonic (single-diacritic), polytonic (multiple-diacritic), and
ancient orthography of the Greek language. Included are the packages
grmath for Greek function names in mathematics, and athnum for Attic
numerals.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-greek
%dir %{_datadir}/texmf-dist/source/generic/babel-greek
%dir %{_datadir}/texmf-dist/tex/generic/babel-greek
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/athnum.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/babel-greek-doc.html
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/babel-greek-doc.rst
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/babel-greek.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/grmath.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-athnum.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-athnum.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-encoding-switch.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-greek-8bitcompat.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-greek-ini.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-greek.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-greek.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-greeknum.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-greeknum.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/test-lgr-fixes.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/usage.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-greek/usage.tex
%doc %{_datadir}/texmf-dist/source/generic/babel-greek/athnum.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-greek/babel-greek.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-greek/babel-greek.ins
%doc %{_datadir}/texmf-dist/source/generic/babel-greek/grmath.dtx
%{_datadir}/texmf-dist/tex/generic/babel-greek/athnum.sty
%{_datadir}/texmf-dist/tex/generic/babel-greek/greek.ldf
%{_datadir}/texmf-dist/tex/generic/babel-greek/grmath.sty
