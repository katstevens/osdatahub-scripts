#!/usr/bin/env python3
"""
Return the local authority and address associated with
 a given postcode, using data from the OS Places API
"""
import argparse
import os
from osdatahub import PlacesAPI
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument(
    "postcode",
    type=str,
    help="Enter a Postcode in quotes eg 'AB1 2DE'"
)
parser.add_argument(
    "-m", "--maxresults",
    type=int,
    help="Max results to return, eg 100",
    default=100,
    required=False
)


def postcode_lookup(api_key, postcode, max_results):
    places = PlacesAPI(api_key)
    response = places.postcode(postcode, limit=max_results)
    return response


def print_address_and_local_authority(response):
    for residence in response["features"]:
        # Usually around 10-30 residences per postcode
        la_code = residence["properties"]["LOCAL_CUSTODIAN_CODE_DESCRIPTION"]
        address = residence["properties"]["ADDRESS"]
        uprn = residence["properties"]["UPRN"]

        print(f"{postcode}: UPRN {uprn}")
        print(f"- {address}")
        print(f"- {la_code}")


if __name__ == "__main__":
    args = parser.parse_args()
    max_results = args.maxresults
    postcode = args.postcode

    # Load the API key from the .env file
    load_dotenv()

    try:
        api_key = os.getenv("OS_DATA_HUB_API_KEY")
    except KeyError:
        raise KeyError("OS_DATA_HUB_API_KEY not set")

    postcode_data_response = postcode_lookup(api_key, postcode, max_results)
    print_address_and_local_authority(postcode_data_response)
