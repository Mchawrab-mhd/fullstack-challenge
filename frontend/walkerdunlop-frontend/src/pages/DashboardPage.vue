<template>
  <nav class="bg-blue-500 text-white py-4 px-8 fixed w-full top-0 z-10">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
      <div class="flex gap-20">
        <div class="text-xl font-bold">My Property Finder</div>
        <div>
          <input
            v-model="address"
            type="text"
            placeholder="Search by address"
            class="border rounded px-2 py-1 text-black"
            @input="handleAddressChange"
          />
        </div>
        <div>
          <input
            v-model="class_name"
            type="text"
            placeholder="Search by Class Desc"
            class="border rounded px-2 py-1 w-full text-black"
            @input="handleClassChange"
          />
        </div>
      </div>
      <div>
        <div class="ml-4">Hi, Admin</div>
        <button @click="logout" class="flex justify-center align-center">
          <img src="../assets/logout.svg" alt="Logo" style="max-width: 15px" />
          <div class="ml-4">Logout</div>
        </button>
      </div>
    </div>
  </nav>
  <div class="flex">
    <div class="w-2/4 h-4/4 bg-blue-200 p-4">
      <h2 class="text-lg font-bold mb-4">Filters</h2>
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700"
          >Building Use</label
        >
        <select v-model="propertyType" class="border rounded px-2 py-1 w-full">
          <option value="none">None</option>
          <option value="Multi Family">Multi Family</option>
          <option value="Single Family">Single Family</option>
        </select>
      </div>
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700"
          >Price Range</label
        >
        <div class="flex">
          <input
            v-model="minPrice"
            type="number"
            placeholder="Min"
            class="border rounded px-2 py-1 w-1/2 mr-2"
          />
          <input
            v-model="maxPrice"
            type="number"
            placeholder="Max"
            class="border rounded px-2 py-1 w-1/2"
          />
        </div>
      </div>
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700"
          >Building sq/ft</label
        >
        <div class="flex">
          <input
            v-model="minSq"
            type="number"
            placeholder="Min"
            class="border rounded px-2 py-1 w-1/2 mr-2"
          />
          <input
            v-model="maxSq"
            type="number"
            placeholder="Max"
            class="border rounded px-2 py-1 w-1/2"
          />
        </div>
      </div>
      <button
        @click="applyFilters"
        class="bg-blue-500 text-white px-4 py-2 rounded-md"
      >
        Apply Filters
      </button>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-3 gap-4 m-4">
      <PropertyCard v-for="(property, index) in properties" :key="index" :property="property" />
    </div>
  </div>
</template>

<script>
import PropertyCard from '@/components/PropertyCard.vue';

export default {
  components: {
    PropertyCard
  },
  data () {
    return {
      propertyType: 'none',
      properties: []
    }
  },
  mounted () {
    fetch('http://localhost:8000/properties', {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
        // Add any other headers as needed
      }
    })
      .then(response => response.json())
      .then(data => {
        this.properties = data.properties
        console.log(this.properties) // Add this line to log the properties array
      })
      .catch(error => {
        console.error('Error fetching properties:', error)
      })
  },
  methods: {
    logout () {
      localStorage.removeItem('userName')
      this.$router.push('/login')
    },
    applyFilters () {
      // Construct the base URL
      let url = 'http://localhost:8000/properties/search?'
      // Check if any filters are present and add them to the URL
      console.log(this.propertyType)
      if (this.propertyType !== 'none') {
        url += `propertyType=${this.propertyType}&`
      } else {
        url += `propertyType=none&`
      }
      if (this.minPrice !== undefined && this.minPrice !== '') {
        url += `minPrice=${this.minPrice}&`
      }
      if (this.maxPrice !== undefined && this.maxPrice !== '') {
        url += `maxPrice=${this.maxPrice}&`
      }

      if (this.minSq !== undefined && this.minSq !== '') {
        url += `minSq=${this.minSq}&`
      }
      if (this.maxSq !== undefined && this.maxSq !== '') {
        url += `maxSq=${this.maxSq}&`
      }

      if (url.endsWith('&')) {
        url = url.slice(0, -1)
      }
      url = url.replace(/&$/, '')
      url = url.replace(/&\w+=undefined/, '')
      // Make the API call
      fetch(url, {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => response.json())
        .then(data => {
          this.properties = data
          console.log(this.properties)
        })
        .catch(error => {
          console.error('Error fetching properties:', error)
        })
    },
    handleAddressChange () {
      // Clear previous debounce timer
      clearTimeout(this.debounceTimer)

      // Set new debounce timer
      this.debounceTimer = setTimeout(() => {
        // Access the updated address value through the event object
        const newAddress = this.address

        fetch(
          `http://localhost:8000/properties/search/full_address?full_address=${newAddress}`,
          {
            method: 'GET',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
              // Add any other headers as needed
            }
          }
        )
          .then(response => response.json())
          .then(data => {
            this.properties = data
            console.log(this.properties) // Log the properties array
          })
          .catch(error => {
            console.error('Error fetching properties:', error)
          })
      }, 500)
    },
    handleClassChange () {
      // Clear previous debounce timer
      clearTimeout(this.debounceTimer)

      // Set new debounce timer
      this.debounceTimer = setTimeout(() => {
        // Access the updated address value through the event object
        const class_name = this.class_name

        // Make the API call with the address
        fetch(
          `http://localhost:8000/properties/search/class?class_name=${class_name}`,
          {
            method: 'GET',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
              // Add any other headers as needed
            }
          }
        )
          .then(response => response.json())
          .then(data => {
            // Update the properties data with the new data from the API response
            this.properties = data
            console.log(this.properties) // Log the properties array
          })
          .catch(error => {
            console.error('Error fetching properties:', error)
          })
      }, 500)
    }
  }
}
</script>
