#! /usr/bin/python

###########################
##   COMON DICTS PYTHON LIBRARY   v1.0
##   
##    This file contains commonly referenced lists for text
##    replacement and functions for frequently used methods
##    
##    redqueen@rabbit-hole.org
###########################


# Function to abbreviate State names (params: state <string>  returns: stateAbbr <string>)

def abbrState( state ):
	states = {
		'alaska' : 'AK',
		'alabama': 'AL',
		'arkansas': 'AR',
		'american samoa': 'AS',
		'arizona': 'AZ',
		'california': 'CA',
		'colorado' : 'CO',
		'connecticut': 'CT',
		'district of columbia': 'DC',
		'delaware': 'DE',
		'florida': 'FL',
		'georgia': 'GA',
		'guam': 'GU',
		'hawaii': 'HI',
		'iowa': 'IA',
		'idaho': 'ID',
		'illinois': 'IL',
		'indiana': 'IN',
		'kansas': 'KS',
		'kentucky': 'KY',
		'louisiana': 'LA',
		'massachusetts': 'MA',
		'maryland': 'MD',
		'maine': 'ME',
		'michigan': 'MI',
		'minnesota': 'MN',
		'missouri': 'MO',
		'northern mariana islands': 'MP',
		'mississippi': 'MS',
		'montana': 'MT',
		'north carolina': 'NC',
		'north dakota': 'ND',
		'nebraska': 'NE',
		'new hampshire': 'NH',
		'new jersey': 'NJ',
		'new mexico': 'NM',
		'nevada': 'NV',
		'new york': 'NY',
		'ohio': 'OH',
		'oklahoma': 'OK',
		'oregon': 'OR',
		'pennsylvania': 'PA',
		'puerto rico': 'PR',
		'rhode island': 'RI',
		'south carolina': 'SC',
		'south dakota': 'SD',
		'tennessee': 'TN',
		'texas': 'TX',
		'utah': 'UT',
		'virginia': 'VA',
		'virgin Islands': 'VI',
		'vermont': 'VT',
		'washington': 'WA',
		'wisconsin': 'WI',
		'west virginia': 'WV',
		'wyoming': 'WY'
	}
	
	abbr = {
		'AK': 'Alaska',
		'AL': 'Alabama',
		'AR': 'Arkansas',
		'AS': 'American Samoa',
		'AZ': 'Arizona',
		'CA': 'California',
		'CO': 'Colorado',
		'CT': 'Connecticut',
		'DC': 'District of Columbia',
		'DE': 'Delaware',
		'FL': 'Florida',
		'GA': 'Georgia',
		'GU': 'Guam',
		'HI': 'Hawaii',
		'IA': 'Iowa',
		'ID': 'Idaho',
		'IL': 'Illinois',
		'IN': 'Indiana',
		'KS': 'Kansas',
		'KY': 'Kentucky',
		'LA': 'Louisiana',
		'MA': 'Massachusetts',
		'MD': 'Maryland',
		'ME': 'Maine',
		'MI': 'Michigan',
		'MN': 'Minnesota',
		'MO': 'Missouri',
		'MP': 'Northern Mariana Islands',
		'MS': 'Mississippi',
		'MT': 'Montana',
		'NA': 'National',
		'NC': 'North Carolina',
		'ND': 'North Dakota',
		'NE': 'Nebraska',
		'NH': 'New Hampshire',
		'NJ': 'New Jersey',
		'NM': 'New Mexico',
		'NV': 'Nevada',
		'NY': 'New York',
		'OH': 'Ohio',
		'OK': 'Oklahoma',
		'OR': 'Oregon',
		'PA': 'Pennsylvania',
		'PR': 'Puerto Rico',
		'RI': 'Rhode Island',
		'SC': 'South Carolina',
		'SD': 'South Dakota',
		'TN': 'Tennessee',
		'TX': 'Texas',
		'UT': 'Utah',
		'VA': 'Virginia',
		'VI': 'Virgin Islands',
		'VT': 'Vermont',
		'WA': 'Washington',
		'WI': 'Wisconsin',
		'WV': 'West Virginia',
		'WY': 'Wyoming'
	}

	if state.isalpha():
		if len(state) > 2:
			if state.lower() in states:
				stateAbbr = states[state.lower()]
				return stateAbbr
			else:
				return 'WARNING:  No matching states'
		else:
			if state.upper() in abbr:
				stateAbbr = abbr[state.upper()]
				return stateAbbr
			else:
				return 'WARNING:  No matching states'
	else:
		return 'ERROR: State names must be alphanumeric'
	
