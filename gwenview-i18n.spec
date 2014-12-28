Summary:	Gwenview - international support
Summary(pl.UTF-8):	Gwenview - wsparcie dla wielu języków
Name:		gwenview-i18n
Version:	1.4.2
Release:	0.1
License:	GPL
Group:		I18n
Source0:	http://dl.sourceforge.net/gwenview/%{name}-%{version}.tar.bz2
# Source0-md5:	68be7ede4c3a17e1c3f807e14143c967
BuildRequires:	gettext-tools
BuildRequires:	kdelibs-devel >= 9:3.2
BuildArch:	noarch
Obsoletes:	gwenview-i18n-base
Obsoletes:	gwenview-i18n-Brazil_Portuguese
Obsoletes:	gwenview-i18n-Breton
Obsoletes:	gwenview-i18n-Bulgarian
Obsoletes:	gwenview-i18n-Catalan
Obsoletes:	gwenview-i18n-Croatian
Obsoletes:	gwenview-i18n-Cymraeg
Obsoletes:	gwenview-i18n-Czech
Obsoletes:	gwenview-i18n-Danish
Obsoletes:	gwenview-i18n-Dutch
Obsoletes:	gwenview-i18n-English_UK
Obsoletes:	gwenview-i18n-Estonian
Obsoletes:	gwenview-i18n-Faroese
Obsoletes:	gwenview-i18n-French
Obsoletes:	gwenview-i18n-German
Obsoletes:	gwenview-i18n-Greek
Obsoletes:	gwenview-i18n-Hebrew
Obsoletes:	gwenview-i18n-Hungarian
Obsoletes:	gwenview-i18n-Irish
Obsoletes:	gwenview-i18n-Italian
Obsoletes:	gwenview-i18n-Lao
Obsoletes:	gwenview-i18n-Norwegian_Bokmaal
Obsoletes:	gwenview-i18n-Norwegian_Nynorsk
Obsoletes:	gwenview-i18n-Polish
Obsoletes:	gwenview-i18n-Portuguese
Obsoletes:	gwenview-i18n-Romanian
Obsoletes:	gwenview-i18n-Russian
Obsoletes:	gwenview-i18n-Serbian
Obsoletes:	gwenview-i18n-Simplified_Chinese
Obsoletes:	gwenview-i18n-Slovak
Obsoletes:	gwenview-i18n-Slovenian
Obsoletes:	gwenview-i18n-Spanish
Obsoletes:	gwenview-i18n-Swedish
Obsoletes:	gwenview-i18n-Tajik
Obsoletes:	gwenview-i18n-Tamil
Obsoletes:	gwenview-i18n-Turkish
Obsoletes:	gwenview-i18n-Uzbek
Obsoletes:	gwenview-i18n-Zulu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gwenview - international language support.

%description -l pl.UTF-8
Gwenview - wsparcie dla wielu języków.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl.UTF-8):	Pusty metapakiet z obsoletes
Group:		I18n
Requires:	kde-i18n-base
Obsoletes:	gwenview-i18n

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl.UTF-8
Pusty metapakiet z Obsoletes dla oddzielnych podpakietów i18n.

%package Afrikaans
Summary:	Gwenview - Afrikaans language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka afrykanerskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Afrikaans
Kexi  - Afrikaans language support.

%description Afrikaans -l pl.UTF-8
Gwenview - wsparcie dla języka afrykanerskiego.

%package Arabic
Summary:	Gwenview - Arabic language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka arabskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Arabic
Gwenview - Arabic language support.

%description Arabic -l pl.UTF-8
Gwenview - wsparcie dla języka arabskiego.

%package Azerbaijani
Summary:	Gwenview - Azerbaijani language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka azerskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Azerbaijani
Gwenview - Azerbaijani language support.

%description Azerbaijani -l pl.UTF-8
Gwenview - wsparcie dla języka azerskiego.

%package Bulgarian
Summary:	Gwenview - Bulgarian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka bułgarskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Bulgarian
Gwenview - Bulgarian language support.

%description Bulgarian -l pl.UTF-8
Gwenview - wsparcie dla języka bułgarskiego.

%package Breton
Summary:	Gwenview - Breton language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka bretońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Breton
Gwenview - Breton language support.

%description Breton -l pl.UTF-8
Gwenview - wsparcie dla języka bretońskiego.

%package Bosnian
Summary:	Gwenview - Bosnian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka bośniackiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Bosnian
Gwenview - Bosnian language support.

%description Bosnian -l pl.UTF-8
Gwenview - wsparcie dla języka bośniackiego.

%package Catalan
Summary:	Gwenview - Catalan language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka katalońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Catalan
Gwenview - Catalan language support.

%description Catalan -l pl.UTF-8
Gwenview - wsparcie dla języka katalońskiego.

%package Czech
Summary:	Gwenview - Czech language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka czeskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Czech
Gwenview - Czech language support.

%description Czech -l pl.UTF-8
Gwenview - wsparcie dla języka czeskiego.

%package Cymraeg
Summary:	Gwenview - Cymraeg language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka walijskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Cymraeg
Gwenview - Cymraeg language support.

%description Cymraeg -l pl.UTF-8
Gwenview - wsparcie dla języka walijskiego.

%package Danish
Summary:	Gwenview - Danish language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka duńskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Danish
Gwenview - Danish language support.

%description Danish -l pl.UTF-8
Gwenview - wsparcie dla języka duńskiego.

%package German
Summary:	Gwenview - German language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka niemieckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description German
Gwenview - German language support.

%description German -l pl.UTF-8
Gwenview - wsparcie dla języka niemieckiego.

%package Greek
Summary:	Gwenview - Greek language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka greckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Greek
Gwenview - Greek language support.

%description Greek -l pl.UTF-8
Gwenview - wsparcie dla języka greckiego.

%package English
Summary:	Gwenview - English language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka angielskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description English
Gwenview - English language support.

%description English -l pl.UTF-8
Gwenview - wsparcie dla języka angielskiego.

%package English_UK
Summary:	Gwenview - English (UK) language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka angielskiego (odmiany brytyjskiej)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description English_UK
Gwenview - English (UK) language support.

%description English_UK -l pl.UTF-8
Gwenview - wsparcie dla języka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	Gwenview - Esperanto language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka esperanto
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Esperanto
Gwenview - Esperanto language support.

%description Esperanto -l pl.UTF-8
Gwenview - wsparcie dla języka esperanto.

%package Spanish
Summary:	Gwenview - Spanish language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka hiszpańskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Spanish
Gwenview - Spanish language support.

%description Spanish -l pl.UTF-8
Gwenview - wsparcie dla języka hiszpańskiego.

%package Estonian
Summary:	Gwenview - Estonian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka estońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Estonian
Gwenview - Estonian language support.

%description Estonian -l pl.UTF-8
Gwenview - wsparcie dla języka estońskiego.

%package Basque
Summary:	Gwenview - Basque language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka baskijskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Basque
Gwenview - Basque language support.

%description Basque -l pl.UTF-8
Gwenview - wsparcie dla języka baskijskiego.

%package Farsi
Summary:	Gwenview - Farsi language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka perskiego (farsi)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Farsi
Gwenview - Farsi language support.

%description Farsi -l pl.UTF-8
Gwenview - wsparcie dla języka perskiego (farsi).


%package Finnish
Summary:	Gwenview - Finnish language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka fińskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Finnish
Gwenview - Finnish language support.

%description Finnish -l pl.UTF-8
Gwenview - wsparcie dla języka fińskiego.

%package Faroese
Summary:	Gwenview - Faroese language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka faroezyjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Faroese
Gwenview - Faroese language support.

%description Faroese -l pl.UTF-8
Gwenview - wsparcie dla języka faroezyjskiego.

%package French
Summary:	Gwenview - French language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka francuskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description French
Gwenview - French language support.

%description French -l pl.UTF-8
Gwenview - wsparcie dla języka francuskiego.

%package Irish
Summary:	Gwenview - Irish language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka irlandzkiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Irish
Gwenview - Irish language support.

%description Irish -l pl.UTF-8
Gwenview - wsparcie dla języka irlandzkiego.

%package Galician
Summary:	Gwenview - Galician language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka galicyjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Galician
Gwenview - Galician language support.

%description Galician -l pl.UTF-8
Gwenview - wsparcie dla języka galicyjskiego.

%package Hindi
Summary:	Gwenview - Hindi language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka hindi
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Hindi
Gwenview - Hindi language support.

%description Hindi -l pl.UTF-8
Gwenview - wsparcie dla języka hindi.

%package Hebrew
Summary:	Gwenview - Hebrew language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka hebrajskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Hebrew
Gwenview - Hebrew language support.

%description Hebrew -l pl.UTF-8
Gwenview - wsparcie dla języka hebrajskiego.

%package Croatian
Summary:	Gwenview - Croatian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka chorwackiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Croatian
Gwenview - Croatian language support.

%description Croatian -l pl.UTF-8
Gwenview - wsparcie dla języka chorwackiego.

%package Hungarian
Summary:	Gwenview - Hungarian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka węgierskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Hungarian
Gwenview - Hungarian language support.

%description Hungarian -l pl.UTF-8
Gwenview - wsparcie dla języka węgierskiego.

%package Upper_Sorbian
Summary:	Gwenview - Upper Sorbian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka górnołużyckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Upper_Sorbian
Gwenview - Upper Sorbian language support.

%description Upper_Sorbian  -l pl.UTF-8
Gwenview - wsparcie dla języka górnołużyckiego.

%package Indonesian
Summary:	Gwenview - Indonesian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka indonezyjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Indonesian
Gwenview - Indonesian language support.

%description Indonesian -l pl.UTF-8
Gwenview - wsparcie dla języka indonezyjskiego.

%package Icelandic
Summary:	Gwenview - Icelandic language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka islandzkiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Icelandic
Gwenview - Icelandic language support.

%description Icelandic -l pl.UTF-8
Gwenview - wsparcie dla języka islandzkiego.

%package Italian
Summary:	Gwenview - Italian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka włoskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Italian
Gwenview - Italian language support.

%description Italian -l pl.UTF-8
Gwenview - wsparcie dla języka włoskiego.

%package Japanese
Summary:	Gwenview - Japanese language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka japońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Japanese
Gwenview - Japanese language support.

%description Japanese -l pl.UTF-8
Gwenview - wsparcie dla języka japońskiego.

%package Korean
Summary:	Gwenview - Korean language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka koreańskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Korean
Gwenview - Korean language support.

%description Korean -l pl.UTF-8
Gwenview - wsparcie dla języka koreańskiego.

%package Lithuanian
Summary:	Gwenview - Lithuanian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka litewskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Lithuanian
Gwenview - Lithuanian language support.

%description Lithuanian -l pl.UTF-8
Gwenview - Wsparcie dla języka litewskiego.

%package Lao
Summary:	Gwenview - Lao language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka laotańskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Lao
Gwenview - lao language support.

%description Lao -l pl.UTF-8
Gwenview - wsparcie dla języka laotańskiego.

%package Latvian
Summary:	Gwenview - Latvian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka łotewskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Latvian
Gwenview - Latvian language support.

%description Latvian -l pl.UTF-8
Gwenview - wsparcie dla języka łotewskiego.

%package Maori
Summary:	Gwenview - Maori language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka maoryjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Maori
Gwenview - Maori language support.

%description Maori -l pl.UTF-8
Gwenview - wsparcie dla języka maoryjskiego.

%package Macedonian
Summary:	Gwenview - Macedonian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka macedońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Macedonian
Gwenview - Macedonian language support.

%description Macedonian -l pl.UTF-8
Gwenview - wsparcie dla języka macedońskiego.

%package Malay
Summary:	Gwenview - Malay language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka malajskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Malay
Gwenview - Malay language support.

%description Malay -l pl.UTF-8
Gwenview - wsparcie dla języka malajskiego.

%package Maltese
Summary:	Gwenview - Maltese language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka maltańskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Maltese
Gwenview - Maltese language support.

%description Maltese -l pl.UTF-8
Gwenview - wsparcie dla języka maltańskiego.

%package Mongolian
Summary:	Gwenview - Mongolian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka mongolskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Mongolian
Gwenview - Mongolian language support.

%description Mongolian -l pl.UTF-8
Gwenview - wsparcie dla języka mongolskiego.

%package Dutch
Summary:	Gwenview - Dutch language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka holenderskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Dutch
Gwenview - Dutch language support.

%description Dutch -l pl.UTF-8
Gwenview - wsparcie dla języka holenderskiego.

%package Norwegian_Bokmaal
Summary:	Gwenview - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Bokmaal
Gwenview - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
Gwenview - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	Gwenview - Norwegian (Nynorsk) language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka norweskiego (odmiany nynorsk)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Nynorsk
Gwenview - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl.UTF-8
Gwenview - wsparcie dla języka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	Gwenview - Northern Sotho language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla północnej odmiany języka ludu Soto
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sotho
Gwenview - Northern Sotho language support.

%description Northern_Sotho -l pl.UTF-8
Gwenview - wsparcie dla północnej odmiany języka ludu Soto.

%package Gascon_occitan
Summary:	Gwenview - Occitan (Gascon) language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka oksytańskiego (dialektu gaskońskiego)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Gascon_occitan
Gwenview - Occitan (Gascon) language support.

%description Gascon_occitan -l pl.UTF-8
Gwenview - wsparcie dla języka oksytańskiego (dialektu gaskońskiego).

%package Polish
Summary:	Gwenview - Polish language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka polskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Polish
Gwenview - Polish language support.

%description Polish -l pl.UTF-8
Gwenview - wsparcie dla języka polskiego.

%package Portuguese
Summary:	Gwenview - Portuguese language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka portugalskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Portuguese
Gwenview - Portuguese language support.

%description Portuguese -l pl.UTF-8
Gwenview - wsparcie dla języka portugalskiego.

%package Brazil_Portuguese
Summary:	Gwenview - Portuguese (Brazil) language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka portugalskiego (odmiany brazylijskiej)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Brazil_Portuguese
Gwenview - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl.UTF-8
Gwenview - wsparcie dla języka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	Gwenview - Romanian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka rumuńskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Romanian
Gwenview - Romanian language support.

%description Romanian -l pl.UTF-8
Gwenview - wsparcie dla języka rumuńskiego.

%package Russian
Summary:	Gwenview - Russian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka rosyjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Russian
Gwenview - Russian language support.

%description Russian -l pl.UTF-8
Gwenview - wsparcie dla języka rosyjskiego.

%package Swati
Summary:	Gwenview - Swati language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka swati
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Swati
Gwenview - Swati language support.

%description Swati -l pl.UTF-8
Gwenview - wsparcie dla języka swati.

%package Northern_Sami
Summary:	Gwenview - Northern Sami language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla północnego języka saami (lapońskiego)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sami
Gwenview - Northern Sami language support.

%description Northern_Sami -l pl.UTF-8
Gwenview - wsparcie dla północnego języka saami (lapońskiego).

%package Slovak
Summary:	Gwenview - Slovak language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka słowackiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Slovak
Gwenview - Slovak language support.

%description Slovak -l pl.UTF-8
Gwenview - wsparcie dla języka słowackiego.

%package Slovenian
Summary:	Gwenview - Slovenian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka słoweńskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Slovenian
Gwenview - Slovenian language support.

%description Slovenian -l pl.UTF-8
Gwenview - wsparcie dla języka słoweńskiego.

%package Serbian
Summary:	Gwenview - Serbian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka serbskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Serbian
Gwenview - Serbian language support.

%description Serbian -l pl.UTF-8
Gwenview - wsparcie dla języka serbskiego.

%package Swedish
Summary:	Gwenview - Swedish language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka szwedzkiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Swedish
Gwenview - Swedish language support.

%description Swedish -l pl.UTF-8
Gwenview - wsparcie dla języka szwedzkiego.

%package Tamil
Summary:	Gwenview - Tamil language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka tamilskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Tamil
Gwenview - Tamil language support.

%description Tamil -l pl.UTF-8
Gwenview - wsparcie dla języka tamilskiego.

%package Tajik
Summary:	Gwenview - Tajik language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka tadżyckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Tajik
Gwenview - Tajik language support.

%description Tajik -l pl.UTF-8
Gwenview - wsparcie dla języka tadżyckiego.

%package Thai
Summary:	Gwenview - Thai language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka tajlandzkiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Thai
Gwenview - Thai language support.

%description Thai -l pl.UTF-8
Gwenview - wsparcie dla języka tajlandzkiego.

%package Turkish
Summary:	Gwenview - Turkish language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka tureckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Turkish
Gwenview - Turkish language support.

%description Turkish -l pl.UTF-8
Gwenview - wsparcie dla języka tureckiego.

%package Ukrainian
Summary:	Gwenview - Ukrainian language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka ukraińskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Ukrainian
Gwenview - Ukrainian language support.

%description Ukrainian -l pl.UTF-8
Gwenview - wsparcie dla języka ukraińskiego.

%package Uzbek
Summary:	Gwenview - Uzbek language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka uzbeckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Uzbek
Gwenview - Uzbek language support.

%description Uzbek -l pl.UTF-8
Gwenview - wsparcie dla języka uzbeckiego.

%package Venda
Summary:	Gwenview - Venda language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka venda
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Venda
Gwenview - Venda language support.

%description Venda -l pl.UTF-8
Gwenview - wsparcie dla języka venda.

%package Vietnamese
Summary:	Gwenview - Vietnamese language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka wietnamskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Vietnamese
Gwenview - Vietnamese language support.

%description Vietnamese -l pl.UTF-8
Gwenview - wsparcie dla języka wietnamskiego.

%package Walloon
Summary:	Gwenview - Walloon language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka walońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Walloon
Gwenview - Walloon language support.

%description Walloon -l pl.UTF-8
Gwenview - wsparcie dla języka walońskiego.

%package Xhosa
Summary:	Gwenview - Xhosa language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka khosa
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Xhosa
Gwenview - Xhosa language support.

%description Xhosa -l pl.UTF-8
Gwenview - wsparcie dla języka khosa.

%package Simplified_Chinese
Summary:	Gwenview - simplified Chinese language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla uproszczonego języka chińskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Simplified_Chinese
Gwenview - simplified Chinese language support.

%description Simplified_Chinese -l pl.UTF-8
Gwenview - wsparcie dla uproszczonego języka chińskiego.

%package Chinese
Summary:	Gwenview - Chinese language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka chińskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Chinese
Gwenview - Chinese language support.

%description Chinese -l pl.UTF-8
Gwenview - wsparcie dla języka chińskiego.

%package Zulu
Summary:	Gwenview - Zulu language support
Summary(pl.UTF-8):	Gwenview - wsparcie dla języka zuluskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Zulu
Gwenview - Zulu language support.

%description Zulu -l pl.UTF-8
Gwenview - wsparcie dla języka zuluskiego.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
%{__make} -f admin/Makefile.common cvs
./configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

FindLang() {
#    $1 - short language name
#    $2 - long language name

    echo "%defattr(644,root,root,755)" > "$2.lang"

# share/locale/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$1" ]; then
       echo "%lang($1) %{_datadir}/locale/$1/LC_MESSAGES/*.mo" >> "$2.lang"
    fi
# share/doc/kde/HTML/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$1" ]; then
       echo "%lang($1) %{_kdedocdir}/$1/gwenview" >> "$2.lang"
    fi
}

##FindLang af Afrikaans
##FindLang ar Arabic
##FindLang az Azerbaijani
FindLang bg Bulgarian
FindLang br Breton
##FindLang bs Bosnian
FindLang ca Catalan
FindLang cs Czech
FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
# FindLang en English
FindLang en_GB English_UK
##FindLang eo Esperanto
FindLang es Spanish
FindLang et Estonian
##FindLang eu Basque
##FindLang fa Farsi
##FindLang fi Finnish
FindLang fo Faroese
FindLang fr French
FindLang ga Irish
##FindLang gl Galician
FindLang he Hebrew
##FindLang hsb Upper_Sorbian
##FindLang hi Hindi
FindLang hr Croatian
FindLang hu Hungarian
# FindLang id Indonesian
##FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
## FindLang ko Korean
##FindLang lt Lithuanian
FindLang lo Lao
## FindLang lv Latvian
# FindLang mi Maori
##FindLang mk Macedonian
##FindLang mn Mongolian
##FindLang ms Malay
##FindLang mt Maltese
FindLang nb Norwegian_Bokmaal
FindLang nl Dutch
FindLang nn Norwegian_Nynorsk
#indLang nso Northern_Sotho
# FindLang oc Gascon_occitan
FindLang pl Polish
FindLang pt Portuguese
FindLang pt_BR Brazil_Portuguese
FindLang ro Romanian
FindLang ru Russian
##FindLang ss Swati
FindLang se Northern_Sami
FindLang sk Slovak
FindLang sl Slovenian
FindLang sr Serbian
FindLang sv Swedish
FindLang ta Tamil
FindLang tg Tajik
FindLang th Thai
FindLang tr Turkish
##FindLang uk Ukrainian
FindLang uz Uzbek
FindLang ven Venda
##FindLang vi Vietnamese
##FindLang wa Walloon
##FindLang xh Xhosa
FindLang zh_CN Simplified_Chinese
##FindLang zh_TW Chinese
FindLang zu Zulu

%find_lang gwenview

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gwenview.lang
%defattr(644,root,root,755)
%files base
%defattr(644,root,root,755)
#%%files -f Afrikaans.lang Afrikaans
#%%defattr(644,root,root,755)
#%%files -f Arabic.lang Arabic
##%files -f Azerbaijani.lang Azerbaijani
%files -f Bulgarian.lang Bulgarian
%defattr(644,root,root,755)
%files -f Breton.lang Breton
%defattr(644,root,root,755)
##%files -f Bosnian.lang Bosnian
%files -f Catalan.lang Catalan
%defattr(644,root,root,755)
%files -f Czech.lang Czech
%defattr(644,root,root,755)
%files -f Cymraeg.lang Cymraeg
%defattr(644,root,root,755)
%files -f Danish.lang Danish
%defattr(644,root,root,755)
%files -f German.lang German
%defattr(644,root,root,755)
%files -f Greek.lang Greek
%defattr(644,root,root,755)
# %files -f English.lang English
%files -f English_UK.lang English_UK
%defattr(644,root,root,755)
#%%files -f Esperanto.lang Esperanto
#%%defattr(644,root,root,755)
%files -f Spanish.lang Spanish
%defattr(644,root,root,755)
%files -f Estonian.lang Estonian
%defattr(644,root,root,755)
##%files -f Basque.lang Basque
#%%files -f Farsi.lang Farsi
#%%defattr(644,root,root,755)
#%%files -f Finnish.lang Finnish
#%%defattr(644,root,root,755)
%files -f Faroese.lang Faroese
%defattr(644,root,root,755)
%files -f French.lang French
%defattr(644,root,root,755)
%files -f Irish.lang Irish
%defattr(644,root,root,755)
##%files -f Galician.lang Galician
##%files -f Hindi.lang Hindi
%files -f Hebrew.lang Hebrew
%defattr(644,root,root,755)
#%%files -f Upper_Sorbian.lang Upper_Sorbian
#%%defattr(644,root,root,755)
%files -f Croatian.lang Croatian
%defattr(644,root,root,755)
%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)
##%files -f Indonesian.lang Indonesian
#%%files -f Icelandic.lang Icelandic
%files -f Italian.lang Italian
%defattr(644,root,root,755)
#%%files -f Japanese.lang Japanese
#%%defattr(644,root,root,755)
##%files -f Korean.lang Korean
%files -f Lao.lang Lao
%defattr(644,root,root,755)
#%%files -f Lithuanian.lang Lithuanian
##%files -f Latvian.lang Latvian
#%%files -f Maltese.lang Maltese
#%%defattr(644,root,root,755)
##%files -f Malay.lang Malay
##%files -f Mongolian.lang Mongolian
# %files -f Maori.lang Maori
#%%files -f Macedonian.lang Macedonian
%files -f Dutch.lang Dutch
%defattr(644,root,root,755)
%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)
%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
%defattr(644,root,root,755)
#%%files -f Northern_Sotho.lang Northern_Sotho
# %files -f Gascon_occitan.lang Gascon_occitan
%files -f Polish.lang Polish
%defattr(644,root,root,755)
#%%{_datadir}/services/searchproviders/*.desktop
%files -f Portuguese.lang Portuguese
%defattr(644,root,root,755)
%files -f Brazil_Portuguese.lang Brazil_Portuguese
%defattr(644,root,root,755)
%files -f Romanian.lang Romanian
%defattr(644,root,root,755)
%files -f Russian.lang Russian
%defattr(644,root,root,755)
#%%files -f Northern_Sami.lang Northern_Sami
#%%defattr(644,root,root,755)
#%%files -f Swati.lang Swati
%files -f Slovak.lang Slovak
%defattr(644,root,root,755)
%files -f Slovenian.lang Slovenian
%defattr(644,root,root,755)
%files -f Serbian.lang Serbian
%defattr(644,root,root,755)
%files -f Swedish.lang Swedish
%defattr(644,root,root,755)
%files -f Tamil.lang Tamil
%defattr(644,root,root,755)
%files -f Tajik.lang Tajik
%defattr(644,root,root,755)
#%%files -f Thai.lang Thai
#%%defattr(644,root,root,755)
%files -f Turkish.lang Turkish
%defattr(644,root,root,755)
##%files -f Ukrainian.lang Ukrainian
%files -f Uzbek.lang Uzbek
%defattr(644,root,root,755)
#%%files -f Venda.lang Venda
#%%defattr(644,root,root,755)
#%%files -f Vietnamese.lang Vietnamese
# %files -f Walloon.lang Walloon
#%%files -f Xhosa.lang Xhosa
#%%defattr(644,root,root,755)
%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)
#%%files -f Chinese.lang Chinese
#%%defattr(644,root,root,755)
%files -f Zulu.lang Zulu
%defattr(644,root,root,755)
