# Property Management System API

This API provides endpoints for managing properties, including CRUD operations and search functionalities.

## Frontend

The frontend of this Property Management System is developed using Vue.js. It includes a basic login system with the following credentials:

- Username: admin
- Password: admin

The login credentials are stored in local storage for simplicity.

## Endpoints

### GET /properties/count

- **Description:** Retrieves the count of all properties in the database.
- **Response:** Returns the count of properties.

### GET /properties

- **Description:** Retrieves a list of properties with a limit of 20 records.
- **Response:** Returns a list of properties.

### GET /property/{property_id}

- **Description:** Retrieves details of a specific property identified by its ID.
- **Parameters:** 
  - `property_id` (integer): ID of the property to retrieve.
- **Response:** Returns the details of the specified property.

### GET /properties/search/full_address

- **Description:** Searches properties by their full address.
- **Parameters:** 
  - `full_address` (string): Full address to search for.
- **Response:** Returns properties matching the provided full address.

### GET /properties/search/class

- **Description:** Searches properties by their class description.
- **Parameters:** 
  - `class_name` (string): Class description to search for.
- **Response:** Returns properties matching the provided class description.

### GET /properties/search/market_value

- **Description:** Searches properties by their estimated market value within a specified range.
- **Parameters:** 
  - `min_value` (float): Minimum estimated market value.
  - `max_value` (float): Maximum estimated market value.
- **Response:** Returns properties within the specified market value range.

### GET /properties/search/building_sq_ft

- **Description:** Searches properties by their building square footage within a specified range.
- **Parameters:** 
  - `min_value` (integer): Minimum building square footage.
  - `max_value` (integer): Maximum building square footage.
- **Response:** Returns properties within the specified building square footage range.

### GET /properties/search/building_use

- **Description:** Searches properties by their building use category.
- **Parameters:** 
  - `propertyType` (string): Type of building use ('none', 'Multi Family', 'Single Family', etc.).
- **Response:** Returns properties matching the specified building use category.

### GET /properties/search (This is the most used one)

- **Description:** Searches properties based on various criteria such as estimated market value, building square footage, and building use.
- **Parameters:** 
  - `minPrice` (float): Minimum estimated market value.
  - `maxPrice` (float): Maximum estimated market value.
  - `minSq` (integer): Minimum building square footage.
  - `maxSq` (integer): Maximum building square footage.
  - `propertyType` (string): Type of building use ('none', 'Multi Family', 'Single Family', etc.).
- **Response:** Returns properties that match the specified criteria.

### Bonus Optimization

One optimization that can help improve the performance of the application under increased data loads is implementing server-side pagination. Currently, the application fetches and displays all properties at once, which can lead to performance issues as the dataset grows. By implementing server-side pagination, the application can retrieve and display data in smaller, more manageable chunks, reducing the load on both the server and the client-side rendering. This approach can enhance the responsiveness of the application and improve the overall user experience.

### Additional Feature

To enhance the user experience while searching for properties, a useful feature would be to implement autocomplete or predictive search functionality for the "Full Address" input field. This feature would provide users with suggestions or predictions as they type, based on existing property addresses in the database. Implementing a sleek and intuitive design for this autocomplete feature can significantly improve the usability of the search functionality.
