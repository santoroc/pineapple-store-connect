import requests
import logging
import gzip
from pineapple.authentication import Authenticator


logger = logging.getLogger()


class AppStoreClient(Authenticator):

    def __init__(self, vendor_number: str, key_id: str, issuer_id: str, private_key: str):
        self.vendor_number = vendor_number
        self.key_id = key_id
        self.issuer_id = issuer_id
        self.private_key = private_key

    
    URL_BASE = 'https://api.appstoreconnect.apple.com'


    def fetch_sales_endpoint(self, frequency: str, report_date: str,
                    report_type: str, report_subtype: str, version: str,
                    compressed=False) -> bytes:
        """
            Requests sales endpoint with the given parameters.
        args:
            report_date (str): Must be in the last year. The current version of
                                appstore api can't retrieve more than that.
                                Format: YYYY-mm-dd
            compressed (bool): The method will return a gzip file when it's true and unziped csv
                                file when it's false.
            
            Find additional information on the other args in
                 https://developer.apple.com/documentation/appstoreconnectapi/download_sales_and_trends_reports
        """

        ENDPOINT = '/v1/salesReports'
        url_parameters = (
            f'filter[vendorNumber]={self.vendor_number}'
            + f'&filter[frequency]={frequency}'
            + f'&filter[reportDate]={report_date}'
            + f'&filter[reportType]={report_type}'
            + f'&filter[reportSubType]={report_subtype}'
            + f'&filter[version]={version}'
        )

        token = self.generate_token(ENDPOINT, url_parameters)
        headers = {"Authorization": f"Bearer {token}"}
        full_url = f"{self.URL_BASE}{ENDPOINT}?{url_parameters}"

        r = requests.get(full_url, headers=headers)
        if r.status_code != 200:
            logger.debug(f"Request content: {r.content}")
            raise requests.ConnectionError(f"Expected status code 200, but got {r.status_code}. URL: {r.url}")
        
        if compressed:
            return r.content
        else:
            return gzip.decompress(r.content)


    def fetch_sales_report(self, report_date: str, compressed=False):
        """
            This method returns a file with sales summary report for a specific date
            without the need to configure many api parameters.
        
        args:
            report_date (str): Must be in the last year. The current version of
                                appstore api can't retrieve more than that.
                                Format: YYYY-mm-dd
            compressed (bool): The method will return a gzip file when it's true and unziped csv
                                file when it's false.
        """

        frequency = 'DAILY'
        report_type = 'SALES'
        report_subtype = 'SUMMARY'
        version = '1_1'

        return self.fetch_sales_endpoint(
            frequency=frequency,
            report_date=report_date,
            report_type=report_type,
            report_subtype=report_subtype,
            version=version,
            compressed=compressed
        )


    def fetch_subscription_events_report(self, report_date: str, compressed=False):
        """
            This method returns a file with subscription events summary report for a specific date
            without the need to configure many api parameters.
        
        args:
            report_date (str): Must be in the last year. The current version of
                                appstore api can't retrieve more than that.
                                Format: YYYY-mm-dd
            compressed (bool): The method will return a gzip file when it's true and unziped csv
                                file when it's false.
        """

        frequency = 'DAILY'
        report_type = 'SUBSCRIPTION_EVENT'
        report_subtype = 'SUMMARY'
        version = '1_3'

        return self.fetch_sales_endpoint(
            frequency=frequency,
            report_date=report_date,
            report_type=report_type,
            report_subtype=report_subtype,
            version=version,
            compressed=compressed
        )