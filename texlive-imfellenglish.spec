%global tl_name imfellenglish
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	IM Fell English fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/imfellenglish
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imfellenglish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imfellenglish.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Igino Marini has implemented digital revivals of fonts bequeathed to
Oxford University by Dr. John Fell, Bishop of Oxford and Dean of Christ
Church in 1686. This package provides the English family, consisting of
Roman, Italic and Small-Cap fonts.

