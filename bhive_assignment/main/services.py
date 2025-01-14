import requests
from typing import Dict
from main.models import FundHouse, Portfolio, User
from django.conf import settings


class BhiveFundService:

    def __init__(self) -> None:
        self.fund_nav_url = "https://latest-mutual-fund-nav.p.rapidapi.com/master"
        self.querystring = {"RTA_Agent_Code":"CAMS"}
        self.headers = {
            'x-rapidapi-host': "latest-mutual-fund-nav.p.rapidapi.com"
        }


    def get_fund_house_schemes(self, fund_house: str) -> (bool, Dict):

        self.querystring.update({
            "AMC_Code": fund_house
        })
        self.headers.update({
             'x-rapidapi-key': settings.RAPID_API_SECRET_KEY
        })
        try:
            response = requests.get(self.fund_nav_url, headers=self.headers, params=self.querystring)
        except Exception as e:
            return False, str(e)

        return True, response.json()[:20]    # returning only 20 objs instead of 13k
    
    def sync_portfolio(self, portfolio: Portfolio):
        # API call to sync portfolio valuer as per Value.
        return

    def sync_portfolio_value_hourly(self):
        portfolios = Portfolio.objects.all()
        for portfolio in portfolios:
            self.sync_portfolio(portfolio=portfolio)
        return