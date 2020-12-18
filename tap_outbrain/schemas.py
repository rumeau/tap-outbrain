#pylint: disable=invalid-name
link = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': ('ID of this PromotedLink, i.e. '
                            '"00f4b02153ee75f3c9dc4fc128ab041962"')
        },
        'campaignId': {
            'type': 'string',
            'description': ('The ID of the campaign to which the '
                            'PromotedLink belongs, i.e. '
                            '"00f4b02153ee75f3c9dc4fc128ab041963"')
        },
        'text': {
            'type': 'string',
            'description': ('The text of the PromotedLink, i.e. "Google to '
                            'take over huge NASA hangar, give execs\' private '
                            'planes a home"'),
        },
        'lastModified': {
            'type': ['null', 'string'],
            'format': 'date-time',
            'description': ('The time when the PromotedLink was last '
                            'modified, i.e. "2013-03-16T10:32:31Z"')
        },
        'creationTime': {
            'type': 'string',
            'format': 'date-time',
            'description': ('The time when the PromotedLink was created, '
                            'i.e. "2013-01-14T07:19:16Z"')
        },
        'url': {
            'type': 'string',
            'description': ('The URL visitors will be sent to upon clicking '
                            'the PromotedLink, i.e. "http://www.engadget.com'
                            '/2014/02/11/nasa-google-hangar-one/"')
        },
        'siteName': {
            'type': ['null', 'string'],
            'description': ('The name of the publisher the PromotedLink '
                            'URL points to, i.e. "cnn.com"')
        },
        'sectionName': {
            'type': ['null', 'string'],
            'description': ('The section name of the site the PromotedLink '
                            'URL points to, i.e. "Sports"')
        },
        'status': {
            'type': ['null', 'string'],
            'description': ('The review status of the PromotedLink, '
                            'i.e. "PENDING"')
        },
        'cachedImageUrl': {
            'type': ['null', 'string'],
            'description': ('The URL of the PromotedLink\'s image, cached '
                            'on Outbrain\'s servers, i.e. "http://images'
                            '.outbrain.com/imageserver/v2/s/gtE/n/plcyz/abc'
                            '/iGYzT/plcyz-f8A-158x110.jpg"')
        },
        'enabled': {
            'type': ['null','boolean'],
            'description': ('Designates whether this PromotedLink will be '
                            'served.')
        },
        'archived': {
            'type': ['null','boolean'],
            'description': ('Designates whether this PromotedLink is '
                            'archived.')
        },
        'documentLanguage': {
            'type': ['null', 'string'],
            'description': ('The 2-letter code for the language of this '
                            'PromotedLink (via the PromotedLinks URL), '
                            'i.e. "EN"')
        },
        'cpc': {
            'type': ['null', 'number'],
            'description': ('Cost per click, i.e. 0.58')
        }
    }
}


campaign = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'Campaign ID'
        },
        'name': {
            'type': 'string',
            'description': 'Campaign name'
        },
        'enabled': {
            'type': 'boolean',
            'description': 'Is the campaign enabled'
        },
        'marketerId': {
            'type': 'string',
            'description': 'Marketer ID'
        },

        'onAirReason': {
            'type': ['null', 'string'],
            'description': 'On Air Reason'
        },
        'creationTime': {
            'type': 'string',
            'format': 'date-time',
            'description': ('The time when the CreationTime was created, '
                            'i.e. "2013-01-14T07:19:16Z"')
        },
        'lastModified': {
            'type': 'string',
            'format': 'date-time',
            'description': ('The time when the LastModified was created, '
                            'i.e. "2013-01-14T07:19:16Z"')
        },
        'cpc': {
            'type': ['null', 'number'],
            'description': ('Cost per monetized user action (for example '
                'cost per click). See Currencies for valid '
                'cost values')
        },
        'autoArchived': {
            'type': 'boolean'
        },
        'minimumCpc': {
            'type': ['null', 'number'],
            'description': ('Minimum Cost per monetized user action (for example '
                'cost per click). See Currencies for valid '
                'cost values')
        },
        'currency': {
            'type': ['null', 'string'],
            'description': 'Currency'
        },
        'budget': {
            'type': 'object',
            'description': ('Partial Budget entity of a campaign. For full '
                            'details use Budget'),
            'properties': {
                'id': {
                    'type': 'string',
                    'description': ('The id of this Budget, i.e. '
                                    '"00f4b02153ee75f3c9dc4fc128ab041962"')
                },
                'name': {
                    'type': 'string',
                    'description': ('The name of this Budget, i.e. '
                                    '"First quarter budget"'),
                },
                'shared': {
                    'type': 'boolean',
                    'description': ('Whether the Budget is shared between '
                                    'Campaigns, provided for convenience '
                                    'based on the number of Campaigns '
                                    'associated to this Budget, i.e. true')
                },
                'amount': {
                    'type': ['null', 'number'],
                    'description': ('The monetary amount of this Budget, '
                                    'i.e. 2000.00')
                },
                'currency': {
                    'type': ['null', 'string'],
                    'description': ('The currency denomination applied to the '
                                    'budget amount, i.e. "USD"')
                },
                'creationTime': {
                    'type': ['null', 'string'],
                    'format': 'date-time',
                    'description': ('The time when this Budget was created, '
                                    'i.e. "2013-01-14 07:19:16"')
                },
                'lastModified': {
                    'type': ['null', 'string'],
                    'format': 'date-time',
                    'description': ('The last modification date of this '
                                    'Budget, i.e. "2014-01-15 12:24:01"')
                },
                'startDate': {
                    'type': ['null', 'string'],
                    'format': 'date',
                    'description': ('The date this Budget is scheduled to '
                                    'begin spending, i.e. "2014-01-15"')
                },
                'endDate': {
                    'type': ['null', 'string'],
                    'format': 'date',
                    'description': ('The date this Budget is scheduled to '
                                    'stop spending. If runForever is true '
                                    'this will not be used. i.e. "2014-01-17"')
                },
                'runForever': {
                    'type': 'boolean',
                    'description': ('Designates whether the budged has an end '
                                    'date In case of true, "endDate" '
                                    'attribute will not be part of the '
                                    'Budgets attributes. i.e. true')
                },
                'type': {
                    'type': ['null', 'string'],
                    'description': ('Controls on which period the Budget '
                                    'refreshes, i.e. "MONTHLY"')
                },
                'pacing': {
                    'type': ['null', 'string'],
                    'description': ('Controls how fast the Budget will be '
                                    'spent, i.e. "AUTOMATIC"')
                }
            }
        },

        'liveStatus': {
            'campaignOnAir': {
                'type': 'boolean',
                'description': ('Is the campaign on air, same as campaignOnAir '
                    'in Live Status')
            },
            'onAirReason': {
                'type': ['null', 'string'],
                'description': ('The reason for the campaign on air status, same '
                    'as onAirReason in Live Status')
            },
            'amountSpent': {
                'type': 'number',
                'description': ('Amount spent')
            }
        }
    }
}


campaign_performance = {
    'type': 'object',
    'properties': {
        'campaignId': {
            'type': 'string',
            'description': ('The campaign ID plus the start date (day) '
                            'for this record.')
        },
        'fromDate': {
            'type': ['null', 'string'],
            'format': 'date',
            'description': 'The start date for this record.'
        },
        'impressions': {
            'type': ['null', 'number'],
            'description': ('Total number of PromotedLinks impressions across '
                            'the entire query range.'),
        },
        'clicks': {
            'type': ['null', 'number'],
            'description': ('Total PromotedLinks clicks across the entire '
                            'query range.'),
        },
        'ctr': {
            'type': ['null', 'number'],
            'description': ('The average CTR (Click Through Rate) percentage '
                            'across the entire query range (clicks / '
                            'impressions)/100.'),
        },
        'spend': {
            'type': ['null', 'number'],
            'description': ('The total amount of money spent across the '
                            'entire query range.'),
        },
        'ecpc': {
            'type': ['null', 'number'],
            'description': ('The effective (calculated) average CPC (Cost Per '
                            'Click) across the entire query range. '
                            'Calculated as: (spend / clicks)'),
        },
        'conversions': {
            'type': ['null', 'number'],
            'description': ('The total number of conversions calculated '
                            'across the entire query range.')
        },
        'conversionRate': {
            'type': ['null', 'number'],
            'description': ('The average rate of conversions per click '
                            'percentage across the entire query range. '
                            'Calculated as: (conversions / clicks)/100')
        },
        'cpa': {
            'type': ['null', 'number'],
            'description': ('The average CPA (Cost Per Acquisition) '
                            'calculated across the entire query range. '
                            'Calculated as: (spend / conversions)')
        }
    }
}

link_performance = {
    'type': 'object',
    'properties': {
        'campaignId': {
            'type': 'string',
            'description': ('The campaign ID for this record.')
        },
        'linkId': {
            'type': ['null', 'string'],
            'description': ('The link ID for this record.')
        },
        'fromDate': {
            'type': ['null', 'string'],
            'format': 'date',
            'description': 'The start date for this record.'
        },
        'impressions': {
            'type': ['null', 'number'],
            'description': ('Total number of PromotedLinks impressions across '
                            'the entire query range.'),
        },
        'clicks': {
            'type': ['null', 'number'],
            'description': ('Total PromotedLinks clicks across the entire '
                            'query range.'),
        },
        'ctr': {
            'type': ['null', 'number'],
            'description': ('The average CTR (Click Through Rate) percentage '
                            'across the entire query range (clicks / '
                            'impressions)/100.'),
        },
        'spend': {
            'type': ['null', 'number'],
            'description': ('The total amount of money spent across the '
                            'entire query range.'),
        },
        'ecpc': {
            'type': ['null', 'number'],
            'description': ('The effective (calculated) average CPC (Cost Per '
                            'Click) across the entire query range. '
                            'Calculated as: (spend / clicks)'),
        },
        'conversions': {
            'type': ['null', 'number'],
            'description': ('The total number of conversions calculated '
                            'across the entire query range.')
        },
        'conversionRate': {
            'type': ['null', 'number'],
            'description': ('The average rate of conversions per click '
                            'percentage across the entire query range. '
                            'Calculated as: (conversions / clicks)/100')
        },
        'cpa': {
            'type': ['null', 'number'],
            'description': ('The average CPA (Cost Per Acquisition) '
                            'calculated across the entire query range. '
                            'Calculated as: (spend / conversions)')
        }
    }
}
