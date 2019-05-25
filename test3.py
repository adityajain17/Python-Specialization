import json
countries=countries=[
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Singapore",
    "optionValue": "Singapore"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Malaysia",
    "optionValue": "Malaysia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Indonesia",
    "optionValue": "Indonesia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Philippines",
    "optionValue": "Philippines"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Thailand",
    "optionValue": "Thailand"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Vietnam",
    "optionValue": "Vietnam"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Afghanistan",
    "optionValue": "Afghanistan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Albania",
    "optionValue": "Albania"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Algeria",
    "optionValue": "Algeria"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Andorra",
    "optionValue": "Andorra"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Angola",
    "optionValue": "Angola"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Antigua & Deps",
    "optionValue": "Antigua & Deps"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Argentina",
    "optionValue": "Argentina"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Armenia",
    "optionValue": "Armenia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Australia",
    "optionValue": "Australia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Austria",
    "optionValue": "Austria"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Azerbaijan",
    "optionValue": "Azerbaijan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Bahamas",
    "optionValue": "Bahamas"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Bahrain",
    "optionValue": "Bahrain"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Bangladesh",
    "optionValue": "Bangladesh"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Barbados",
    "optionValue": "Barbados"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Belarus",
    "optionValue": "Belarus"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Belgium",
    "optionValue": "Belgium"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Belize",
    "optionValue": "Belize"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Benin",
    "optionValue": "Benin"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Bhutan",
    "optionValue": "Bhutan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Bolivia",
    "optionValue": "Bolivia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Bosnia Herzegovina",
    "optionValue": "Bosnia Herzegovina"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Botswana",
    "optionValue": "Botswana"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Brazil",
    "optionValue": "Brazil"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Brunei",
    "optionValue": "Brunei"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Bulgaria",
    "optionValue": "Bulgaria"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Burkina",
    "optionValue": "Burkina"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Burundi",
    "optionValue": "Burundi"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Cambodia",
    "optionValue": "Cambodia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Cameroon",
    "optionValue": "Cameroon"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Canada",
    "optionValue": "Canada"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Cape Verde",
    "optionValue": "Cape Verde"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Central African Rep",
    "optionValue": "Central African Rep"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Chad",
    "optionValue": "Chad"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Chile",
    "optionValue": "Chile"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "China",
    "optionValue": "China"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Colombia",
    "optionValue": "Colombia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Comoros",
    "optionValue": "Comoros"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Congo",
    "optionValue": "Congo"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Congo {Democratic Rep}",
    "optionValue": "Congo {Democratic Rep}"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Costa Rica",
    "optionValue": "Costa Rica"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Croatia",
    "optionValue": "Croatia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Cuba",
    "optionValue": "Cuba"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Cyprus",
    "optionValue": "Cyprus"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Czech Republic",
    "optionValue": "Czech Republic"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Denmark",
    "optionValue": "Denmark"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Djibouti",
    "optionValue": "Djibouti"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Dominica",
    "optionValue": "Dominica"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Dominican Republic",
    "optionValue": "Dominican Republic"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "East Timor",
    "optionValue": "East Timor"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Ecuador",
    "optionValue": "Ecuador"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Egypt",
    "optionValue": "Egypt"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "El Salvador",
    "optionValue": "El Salvador"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Equatorial Guinea",
    "optionValue": "Equatorial Guinea"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Eritrea",
    "optionValue": "Eritrea"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Estonia",
    "optionValue": "Estonia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Ethiopia",
    "optionValue": "Ethiopia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Fiji",
    "optionValue": "Fiji"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Finland",
    "optionValue": "Finland"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "France",
    "optionValue": "France"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Gabon",
    "optionValue": "Gabon"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Gambia",
    "optionValue": "Gambia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Georgia",
    "optionValue": "Georgia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Germany",
    "optionValue": "Germany"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Ghana",
    "optionValue": "Ghana"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Greece",
    "optionValue": "Greece"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Grenada",
    "optionValue": "Grenada"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Guatemala",
    "optionValue": "Guatemala"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Guinea",
    "optionValue": "Guinea"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Guinea-Bissau",
    "optionValue": "Guinea-Bissau"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Guyana",
    "optionValue": "Guyana"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Haiti",
    "optionValue": "Haiti"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Honduras",
    "optionValue": "Honduras"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Hungary",
    "optionValue": "Hungary"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Iceland",
    "optionValue": "Iceland"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "India",
    "optionValue": "India"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Iran",
    "optionValue": "Iran"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Iraq",
    "optionValue": "Iraq"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Ireland {Republic}",
    "optionValue": "Ireland {Republic}"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Israel",
    "optionValue": "Israel"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Italy",
    "optionValue": "Italy"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Ivory Coast",
    "optionValue": "Ivory Coast"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Jamaica",
    "optionValue": "Jamaica"
  },
{
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Japan",
    "optionValue": "Japan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Jordan",
    "optionValue": "Jordan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Kazakhstan",
    "optionValue": "Kazakhstan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Kenya",
    "optionValue": "Kenya"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Kiribati",
    "optionValue": "Kiribati"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Korea North",
    "optionValue": "Korea North"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Korea South",
    "optionValue": "Korea South"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Kosovo",
    "optionValue": "Kosovo"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Kuwait",
    "optionValue": "Kuwait"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Kyrgyzstan",
    "optionValue": "Kyrgyzstan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Laos",
    "optionValue": "Laos"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Latvia",
    "optionValue": "Latvia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Lebanon",
    "optionValue": "Lebanon"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Lesotho",
    "optionValue": "Lesotho"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Liberia",
    "optionValue": "Liberia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Libya",
    "optionValue": "Libya"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Liechtenstein",
    "optionValue": "Liechtenstein"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Lithuania",
    "optionValue": "Lithuania"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Luxembourg",
    "optionValue": "Luxembourg"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Macedonia",
    "optionValue": "Macedonia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Madagascar",
    "optionValue": "Madagascar"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Malawi",
    "optionValue": "Malawi"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Maldives",
    "optionValue": "Maldives"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Mali",
    "optionValue": "Mali"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Malta",
    "optionValue": "Malta"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Marshall Islands",
    "optionValue": "Marshall Islands"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Mauritania",
    "optionValue": "Mauritania"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Mauritius",
    "optionValue": "Mauritius"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Mexico",
    "optionValue": "Mexico"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Micronesia",
    "optionValue": "Micronesia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Moldova",
    "optionValue": "Moldova"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Monaco",
    "optionValue": "Monaco"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Mongolia",
    "optionValue": "Mongolia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Montenegro",
    "optionValue": "Montenegro"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Morocco",
    "optionValue": "Morocco"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Mozambique",
    "optionValue": "Mozambique"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Myanmar, {Burma}",
    "optionValue": "Myanmar, {Burma}"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Namibia",
    "optionValue": "Namibia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Nauru",
    "optionValue": "Nauru"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Nepal",
    "optionValue": "Nepal"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Netherlands",
    "optionValue": "Netherlands"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "New Zealand",
    "optionValue": "New Zealand"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Nicaragua",
    "optionValue": "Nicaragua"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Niger",
    "optionValue": "Niger"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Nigeria",
    "optionValue": "Nigeria"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Norway",
    "optionValue": "Norway"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Oman",
    "optionValue": "Oman"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Pakistan",
    "optionValue": "Pakistan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Palau",
    "optionValue": "Palau"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Panama",
    "optionValue": "Panama"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Papua New Guinea",
    "optionValue": "Papua New Guinea"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Paraguay",
    "optionValue": "Paraguay"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Peru",
    "optionValue": "Peru"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Poland",
    "optionValue": "Poland"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Portugal",
    "optionValue": "Portugal"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Qatar",
    "optionValue": "Qatar"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Romania",
    "optionValue": "Romania"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Russian Federation",
    "optionValue": "Russian Federation"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Rwanda",
    "optionValue": "Rwanda"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "St Kitts & Nevis",
    "optionValue": "St Kitts & Nevis"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "St Lucia",
    "optionValue": "St Lucia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Saint Vincent & the Grenadines",
    "optionValue": "Saint Vincent & the Grenadines"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Samoa",
    "optionValue": "Samoa"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "San Marino",
    "optionValue": "San Marino"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Sao Tome & Principe",
    "optionValue": "Sao Tome & Principe"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Saudi Arabia",
    "optionValue": "Saudi Arabia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Senegal",
    "optionValue": "Senegal"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Serbia",
    "optionValue": "Serbia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Seychelles",
    "optionValue": "Seychelles"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Sierra Leone",
    "optionValue": "Sierra Leone"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Slovakia",
    "optionValue": "Slovakia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Slovenia",
    "optionValue": "Slovenia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Solomon Islands",
    "optionValue": "Solomon Islands"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Somalia",
    "optionValue": "Somalia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "South Africa",
    "optionValue": "South Africa"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "South Sudan",
    "optionValue": "South Sudan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Spain",
    "optionValue": "Spain"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Sri Lanka",
    "optionValue": "Sri Lanka"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Sudan",
    "optionValue": "Sudan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Suriname",
    "optionValue": "Suriname"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Swaziland",
    "optionValue": "Swaziland"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Sweden",
    "optionValue": "Sweden"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Switzerland",
    "optionValue": "Switzerland"
  },
{
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Syria",
    "optionValue": "Syria"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Taiwan",
    "optionValue": "Taiwan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Tajikistan",
    "optionValue": "Tajikistan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Tanzania",
    "optionValue": "Tanzania"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Togo",
    "optionValue": "Togo"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Tonga",
    "optionValue": "Tonga"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Trinidad & Tobago",
    "optionValue": "Trinidad & Tobago"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Tunisia",
    "optionValue": "Tunisia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Turkey",
    "optionValue": "Turkey"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Turkmenistan",
    "optionValue": "Turkmenistan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Tuvalu",
    "optionValue": "Tuvalu"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Uganda",
    "optionValue": "Uganda"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Ukraine",
    "optionValue": "Ukraine"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "United Arab Emirates",
    "optionValue": "United Arab Emirates"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "United Kingdom",
    "optionValue": "United Kingdom"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "United States",
    "optionValue": "United States"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Uruguay",
    "optionValue": "Uruguay"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Uzbekistan",
    "optionValue": "Uzbekistan"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Vanuatu",
    "optionValue": "Vanuatu"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Vatican City",
    "optionValue": "Vatican City"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Venezuela",
    "optionValue": "Venezuela"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Yemen",
    "optionValue": "Yemen"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Zambia",
    "optionValue": "Zambia"
  },
  {
    "id": "male",
    "active": True,
    "defaultOption": True,
    "optionText": "Zimbabwe",
    "optionValue": "Zimbabwe"
  }
]
c=1
for te in countries:
    te["id"]=str(c)
    c=c+1
    v=json.dumps(te,indent=4)
    print(v,end=',\n')
