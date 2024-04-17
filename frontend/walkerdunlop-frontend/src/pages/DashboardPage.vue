<template>
    <nav class="bg-blue-500 text-white py-4 px-8 fixed w-full top-0 z-10">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <div class="text-xl font-bold">My Property Finder</div>
            <div>
                <div class="ml-4">Hi, Admin</div>
            </div>
        </div>
    </nav>
    <div class="flex">
        <div class="w-2/4 h-4/4 bg-blue-200 p-4">
            <h2 class="text-lg font-bold mb-4">Filters</h2>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Building Use</label>
                <select v-model="propertyType" class="border rounded px-2 py-1 w-full">
                    <option value="none">None</option>
                    <option value="Multi Family">Multi Family</option>
                    <option value="Single Family">Single Family</option>
                </select>
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Price Range</label>
                <div class="flex">
                    <input v-model="minPrice" type="number" placeholder="Min" class="border rounded px-2 py-1 w-1/2 mr-2">
                    <input v-model="maxPrice" type="number" placeholder="Max" class="border rounded px-2 py-1 w-1/2">
                </div>
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Building sq/ft</label>
                <div class="flex">
                    <input v-model="minPrice" type="number" placeholder="Min" class="border rounded px-2 py-1 w-1/2 mr-2">
                    <input v-model="maxPrice" type="number" placeholder="Max" class="border rounded px-2 py-1 w-1/2">
                </div>
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Address</label>
                <input v-model="address" type="text" placeholder="Search by address"
                    class="border rounded px-2 py-1 w-full">
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Class description</label>
                <input v-model="address" type="text" placeholder="Search by Class Description"
                    class="border rounded px-2 py-1 w-full">
            </div>

            <button @click="applyFilters" class="bg-blue-500 text-white px-4 py-2 rounded-md">Apply Filters</button>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-3 gap-4 m-4">
    <div v-for="property in properties" :key="property.id" class="border rounded p-4 shadow-md">
        <h2 class="text-lg font-bold">{{ property.full_address }}</h2>
        <p>{{ property.class_description }}</p>
        <p class="mt-2 text-blue-600">Estimated Market Value: ${{ property.estimated_market_value }}</p>
        <p class="text-red-600">Building Use: {{ property.bldg_use ? property.bldg_use : '---' }}</p>
        <p>Building Sqft: {{ property.building_sq_ft }} sqft</p>
        <div class="mt-4 border-t pt-4 text-sm text-gray-600">
            <p>City: {{ property.city }}</p>
            <p>Zip Code: {{ property.zip_code }}</p>
            <p>Neighborhood: {{ property.neighborhood }}</p>
        </div>
    </div>
</div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            properties: []
        };
    },
    mounted() {
        fetch('http://localhost:8000/properties', {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                // Add any other headers as needed
            }
        })
            .then(response => response.json())
            .then(data => {
                this.properties = data.properties;
                console.log(this.properties); // Add this line to log the properties array
            })
            .catch(error => {
                console.error('Error fetching properties:', error);
            });
    }
};
</script>