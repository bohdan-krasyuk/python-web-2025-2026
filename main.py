from fastapi import FastAPI, Response, status
from pydantic import BaseModel, Field

from app.dtos.product_dtos import ProductDto, UpdateProductDto
from app.services.product_service import ProductServiceDependency

app = FastAPI()
# CMS - Content Management System
# CRUD - Create, Read, Update, Delete

# JSON

@app.get("/products")
def get_products(service: ProductServiceDependency) -> list[ProductDto]:
    return service.get_all_for_public()

@app.post("/products")
def create_product(service: ProductServiceDependency, request: ProductDto):
    return service.create(request)

@app.put("/products")
def update_product(service: ProductServiceDependency, request: UpdateProductDto):
    return service.update(request)


class SearchProductDto(BaseModel):
    title: str = Field(min_length=1)
    category: str
    price_from: float

@app.post("/search-products")
def search_products(search_request: SearchProductDto, response: Response):
    response.status_code = status.HTTP_201_CREATED
    temp_list = []
    print(temp_list[7])
    return search_request

@app.get("/")
def get_root():
    return "Welcome to our API"
