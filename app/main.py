from fastapi import FastAPI
from app.endpoints import root, properties
from sqlalchemy import inspect
import pandas as pd
# from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Property, SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(root.router)
app.include_router(properties.router)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

def init_db():
    # Check if the table exists
    inspector = inspect(engine)
    if not inspector.has_table("properties"):
        Property.metadata.create_all(bind=engine)
        print("Table created.")

    # Check if data is already present in the database
    session = SessionLocal()
    try:
        if session.query(Property).count() == 0:
            # Read data from the Excel file
            data = pd.read_excel('C:\\Users\\moems\\Documents\\fullstack-challenge\\Enodo_Skills_Assessment_Data_File.xlsx')
            column_mapping = {
                'Full Address': 'full_address',
                'Longitude': 'longitude',
                'Latitude': 'latitude',
                'Zip': 'zip_code',
                'REC_TYPE': 'rec_type',
                'PIN': 'pin',
                'OVACLS': 'ovaclass',
                'CLASS_DESCRIPTION': 'class_description',
                'CURRENT_LAND': 'current_land',
                'CURRENT_BUILDING': 'current_building',
                'CURRENT_TOTAL': 'current_total',
                'ESTIMATED_MARKET_VALUE': 'estimated_market_value',
                'PRIOR_LAND': 'prior_land',
                'PRIOR_BUILDING': 'prior_building',
                'PRIOR_TOTAL': 'prior_total',
                'PPRIOR_LAND': 'pprior_land',
                'PPRIOR_BUILDING': 'pprior_building',
                'PPRIOR_TOTAL': 'pprior_total',
                'PPRIOR_YEAR': 'pprior_year',
                'TOWN': 'town',
                'VOLUME': 'volume',
                'LOC': 'loc',
                'TAX_CODE': 'tax_code',
                'NEIGHBORHOOD': 'neighborhood',
                'HOUSENO': 'houseno',
                'DIR': 'direction',
                'STREET': 'street',
                'SUFFIX': 'suffix',
                'APT': 'apt',
                'CITY': 'city',
                'RES_TYPE': 'res_type',
                'BLDG_USE': 'bldg_use',
                'APT_DESC': 'apt_desc',
                'COMM_UNITS': 'comm_units',
                'EXT_DESC': 'ext_desc',
                'FULL_BATH': 'full_bath',
                'HALF_BATH': 'half_bath',
                'BSMT_DESC': 'bsmt_desc',
                'ATTIC_DESC': 'attic_desc',
                'AC': 'ac',
                'FIREPLACE': 'fireplace',
                'GAR_DESC': 'gar_desc',
                'AGE': 'age',
                'BUILDING_SQ_FT': 'building_sq_ft',
                'LAND_SQ_FT': 'land_sq_ft',
                'BLDG_SF': 'bldg_sf',
                'UNITS_TOT': 'units_tot',
                'MULTI_SALE': 'multi_sale',
                'DEED_TYPE': 'deed_type',
                'SALE_DATE': 'sale_date',
                'SALE_AMOUNT': 'sale_amount',
                'APPCNT': 'appcnt',
                'APPEAL_A': 'appeal_a',
                'APPEAL_A_STATUS': 'appeal_a_status',
                'APPEAL_A_RESULT': 'appeal_a_result',
                'APPEAL_A_REASON': 'appeal_a_reason',
                'APPEAL_A_PIN_RESULT': 'appeal_a_pin_result',
                'APPEAL_A_PROPAV': 'appeal_a_propav',
                'APPEAL_A_CURRAV': 'appeal_a_currav',
                'APPEAL_A_RESLTDATE': 'appeal_a_resltdate'
            }
            data.rename(columns=column_mapping, inplace=True)
            # Insert data into the database
            for _, row in data.iterrows():
                property_instance = Property(**row.to_dict())
                session.add(property_instance)
            session.commit()
            print("Data added to the database.")
        else:
            print("Data is already present in the database.")
    finally:
        session.close()
@app.on_event("startup")
def startup_event():
    init_db()