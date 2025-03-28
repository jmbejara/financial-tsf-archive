"""
Pull selected premium tables from WRDS
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from pathlib import Path

import pandas as pd
import wrds

from settings import config

DATA_DIR = Path(config("DATA_DIR"))
WRDS_USERNAME_BANK_PREMIUM = config("WRDS_USERNAME_BANK_PREMIUM")


def pull_selected_premium_tables(wrds_username=WRDS_USERNAME_BANK_PREMIUM):
    db = wrds.Connection(wrds_username=wrds_username)
    # db.list_libraries()
    # db.list_tables(library='bank')

    wrds_struct_rel_ultimate = db.get_table(
        library="bank", table="wrds_struct_rel_ultimate"
    )
    # wrds_struct_rel_ultimate.info()

    wrds_call_research = db.get_table(library="bank", table="wrds_call_research")
    wrds_call_research["date"] = pd.to_datetime(wrds_call_research["date"])
    # wrds_call_research.info(verbose=True)

    wrds_bank_crsp_link = db.get_table(library="bank", table="wrds_bank_crsp_link")
    # wrds_bank_crsp_link.info()

    idrssd_to_lei = db.get_table(library="bank", table="idrssd_to_lei")
    # idrssd_to_lei.info()

    lei_main = db.get_table(
        library="bank",
        table="lei_main",
        columns=[
            "lei_record_id",
            "most_recent",
            "lei",
            "legalname",
            "entitycategory",
            "entitystatus",
            "rec_bdate",
            "rec_edate",
        ],
    )
    # lei_main.info()

    lei_legalevents = db.get_table(library="bank", table="lei_legalevents")
    # lei_legalevents.info()

    lei_otherentnames = db.get_table(library="bank", table="lei_otherentnames")
    # lei_otherentnames.info()

    lei_successorentity = db.get_table(library="bank", table="lei_successorentity")
    # lei_successorentity.info()
    db.close()

    selected_tables = {
        "wrds_struct_rel_ultimate": wrds_struct_rel_ultimate,
        "wrds_call_research": wrds_call_research,
        "wrds_bank_crsp_link": wrds_bank_crsp_link,
        "idrssd_to_lei": idrssd_to_lei,
        "lei_main": lei_main,
        "lei_legalevents": lei_legalevents,
        "lei_otherentnames": lei_otherentnames,
        "lei_successorentity": lei_successorentity,
    }
    return selected_tables


available_tables = [
    "wrds_struct_rel_ultimate",
    "wrds_call_research",
    "wrds_bank_crsp_link",
    "idrssd_to_lei",
    "lei_main",
    "lei_legalevents",
    "lei_otherentnames",
    "lei_successorentity",
]


def load_table(table_name, data_dir=DATA_DIR):
    if table_name not in available_tables:
        raise ValueError(f"Table {table_name} not available")
    return pd.read_parquet(data_dir / f"{table_name}.parquet")


def _demo():
    wrds_struct_rel_ultimate = load_table("wrds_struct_rel_ultimate")
    wrds_struct_rel_ultimate.info()

    wrds_call_research = load_table("wrds_call_research")
    wrds_call_research.info(verbose=True)
    wrds_call_research["date"] = pd.to_datetime(wrds_call_research["date"])
    wrds_call_research[["date"]].describe()

    idrssd_to_lei = load_table("idrssd_to_lei")
    idrssd_to_lei.info()

    lei_main = load_table("lei_main")
    lei_main.info()


if __name__ == "__main__":
    # Create subfolder
    dest_dir = DATA_DIR
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Pull data
    selected_tables = pull_selected_premium_tables(
        wrds_username=WRDS_USERNAME_BANK_PREMIUM
    )
    for table_name, df in selected_tables.items():
        df.to_parquet(dest_dir / f"{table_name}.parquet")
