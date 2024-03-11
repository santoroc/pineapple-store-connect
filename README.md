# pineapple-store-connect

This Python SDK simplifies the process of connecting to the App Store Connect API for reporting purposes. It provides a streamlined interface for downloading sales and subscription reports, eliminating the need for manual HTTP logic and API parameter handling. With this SDK, you can focus on your data, not the details of API interaction.

## Installation

```
pip install pineapple-store-connect
```

## Using pineapple-store-connect to download the sales report

```python
from pineapple.client import AppStoreClient

private_key = """<your-private-key-here>"""
vendor_number = '<your-vendor-number-here>'
key_id = '<your-key-id-here>'
issuer_id = '<your-issuer-id-here>'

client = AppStoreClient(vendor_number=vendor_number, key_id=key_id,
                        issuer_id=issuer_id, private_key=private_key)

report_date = '<your-report-date-here>'
report_file = client.fetch_sales_report(report_date)

with open(f'appstore_sales_{report_date}.csv', 'wb') as f:
    f.write(report_file)
```

# Reference

### pineapple.client.AppStoreClient
This class allows connecting with App Store Connect API and to querying its data.
#### Parameters
- vendor_number: str. Appstore vendor account number. More in finding vendor number [here](https://developer.apple.com/help/app-store-connect/getting-paid/view-payments-and-proceeds).
- issuer_id: str. Your issuer ID from the API Keys page in App Store Connect; for example, `57246542-96fe-1a63-e053-0824d011072a`.
- key_id: str. The private key identifier that can be found on the private key creation page. Learn more about the creation of a private key [here](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api).
- private_key: str. The private key string generated in App Store Connect portal. Learn more about the creation of a private key [here](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api).

### pineapple.client.AppStoreClient.fetch_sales_report
This method downloads the daily Sales Report data.
#### Parameters
- report_date: str. Must follow the format `YYYY-mm-dd`. The reports are saved for one year after they become available. They are usually available the following day.
- compressed: bool. It is not required and defaults to False. If True the method returns compressed gzip data.

### pineapple.client.AppStoreClient.fetch_sales_report
This method downloads the daily Subscription Events report data.
#### Parameters
- report_date: str. Must follow the format `YYYY-mm-dd`. The reports are saved for one year after they become available. They are usyally available the following day.
- compressed: bool. It is not required and defaults to False. If True the method returns compressed gzip data.

### pineapple.client.AppStoreClient.fetch_sales_endpoint
This method allows the user to change the API parameters and call for different types of reports. Not all combinations of parameters are valid. Learn more about the parameters by visiting this [documentation](https://developer.apple.com/documentation/appstoreconnectapi/download_sales_and_trends_reports).
#### Parameters
- frequency: str. (Required) Frequency of the report to download. For a list of values, see Allowed Values. Based on Sales Report Type below. Possible Values: DAILY, WEEKLY, MONTHLY, YEARLY
- report_date: str. The report date to download. Specify the date in the YYYY-MM-DD format for all report frequencies except DAILY, which doesn’t require a date. For more information, see [report availability and storage](https://help.apple.com/itc/appssalesandtrends/#/itc48f999955).
- report_type: str. (Required) The report to download. For more details on each report type see About Reports. Possible Values: SALES, PRE_ORDER, NEWSSTAND, SUBSCRIPTION, SUBSCRIPTION_EVENT, SUBSCRIBER, SUBSCRIPTION_OFFER_CODE_REDEMPTION, INSTALLS, FIRST_ANNUAL.
- report_subtype: str. (Required) The report subtype to download. For a list of values, see Allowed Values Based on Sales Report Type below. Possible Values: SUMMARY, DETAILED, SUMMARY_INSTALL_TYPE, SUMMARY_TERRITORY, SUMMARY_CHANNEL.
- version: str. The version of the report. See the [list of values](https://developer.apple.com/documentation/appstoreconnectapi/download_sales_and_trends_reports#discussion).
- compressed: bool. It is not required and defaults to False. If True the method returns compressed gzip data.

# Room for improvement
- Add automated test scripts.
- Cover all the App Store Connect API reporting endpoints.