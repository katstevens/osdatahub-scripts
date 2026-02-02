# osdatahub-scripts
Scripts for use with OS Data Hub, including postcode lookup

## Install

### Requirements

>- Python >= 3.13 (https://www.python.org/downloads/)

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Authentication 

Add your OS API key to the `.env` file (you can make a copy from the `.env.template` file).

Note that you will need the appropriate licence to request and use an OS API key.

See the Ordnance Survey Data Hub for more details: https://osdatahub.os.uk/ 

## Usage

Run the postcode lookup script with:

```shell
./postcode_lookup.py "AB1 2DE" --maxresults 10
```

For a given postcode, the script will print a list of properties, their UPRN
and associated local authority.
