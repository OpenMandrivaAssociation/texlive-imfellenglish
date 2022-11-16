Name:		texlive-imfellenglish
Version:	64568
Release:	1
Summary:	IM Fell English fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/imfellenglish
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imfellenglish.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imfellenglish.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Igino Marini has implemented digital revivals of fonts
bequeathed to Oxford University by Dr. John Fell, Bishop of
Oxford and Dean of Christ Church in 1686. This package provides
the English family, consisting of Roman, Italic and Small-Cap
fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/imfellenglish
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish
%{_texmfdistdir}/fonts/type1/iginomarini/imfellenglish
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish
%{_texmfdistdir}/fonts/opentype/iginomarini/imfellenglish
%{_texmfdistdir}/fonts/map/dvips/imfellenglish
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish
%doc %{_texmfdistdir}/doc/fonts/imfellenglish

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
