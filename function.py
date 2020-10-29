import os

import requests

import s3


def lambda_handler(event, context):
    main()


def main():
    url = "https://enrarchives.sos.mo.gov/apfeed/apfeed.asmx/GetElectionResults"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0"}
    params = {'AccessKey': os.getenv("ACCESS_KEY")}
    r = requests.get(url, headers=headers, params=params)

    r.raise_for_status()

    s3.archive(
        r.content, r.headers['Content-Type'], path='sos'
        )

if __name__ == '__main__':
    main()
