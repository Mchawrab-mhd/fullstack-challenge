from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..models import Property, SessionLocal
from typing import List

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/properties/count", response_model=None)
def read_property_count(db: Session = Depends(get_db)):
    property_record = db.query(Property).count()
    if property_record is None:
        raise HTTPException(status_code=404, detail="No Properties")
    return {"details":{"count":property_record}}

@router.get("/properties", response_model=None)
def read_properties(db: Session = Depends(get_db)):
    properties = db.query(Property).limit(20).all()
    if not properties:
        raise HTTPException(status_code=404, detail="No Properties Found")
    return {"properties": properties}


@router.get("/property/{property_id}", response_model=None)
def read_property(property_id: int, db: Session = Depends(get_db)):
    property_record = db.query(Property).filter(Property.id == property_id).first()
    if property_record is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_record

# Endpoint to search properties by Full Address
@router.get("/properties/search/full_address")
def search_by_full_address(full_address: str = Query(...), db: Session = Depends(get_db)):
    properties = db.query(Property).filter(Property.full_address.ilike(f"%{full_address}%")).all()
    return properties

# Endpoint to search properties by Class
@router.get("/properties/search/class")
def search_by_class(class_name: str = Query(...), db: Session = Depends(get_db)):
    properties = db.query(Property).filter(Property.class_description.ilike(f"%{class_name}%")).all()
    return properties

@router.get("/properties/search/market_value")
def search_by_market_value(min_value: float = Query(None), max_value: float = Query(None), db: Session = Depends(get_db)):
    print("Received min_value:", min_value)
    print("Received max_value:", max_value)

    query = db.query(Property)
    if min_value is not None:
        query = query.filter(Property.estimated_market_value >= float(min_value))
    if max_value is not None:
        query = query.filter(Property.estimated_market_value <= float(max_value))
    
    properties = query.all()
    print("Properties found:", properties)
    return properties

@router.get("/properties/search/building_sq_ft")
def search_by_building_sq_ft(min_value: int = Query(None), max_value: int = Query(None), db: Session = Depends(get_db)):
    print("Received min_value:", min_value)
    print("Received max_value:", max_value)
    
    query = db.query(Property)
    if min_value is not None:
        query = query.filter(Property.building_sq_ft >= int(min_value))
    if max_value is not None:
        query = query.filter(Property.building_sq_ft <= int(max_value))
    
    properties = query.all()
    print("Properties found:", properties)
    return properties

@router.get("/properties/search/building_use")
def search_by_building_use(building_use: str = Query(...), db: Session = Depends(get_db)):
    properties = db.query(Property).filter(Property.bldg_use.ilike(f"%{building_use}%")).all()
    return properties

