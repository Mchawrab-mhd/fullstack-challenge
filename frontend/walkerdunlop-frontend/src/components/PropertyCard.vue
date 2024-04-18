<template>
  <div class="border rounded p-4 shadow-md">
    <button
      @click="redirectToMapsPage(property.id, property.latitude, property.longitude)"
      class="focus:outline-none border border-blue-500 rounded px-2 py-1"
    >
      <span class="text-blue-500">View</span>
      <span> </span>
      <span class="text-yellow-500">On</span>
      <span> </span>
      <span class="text-red-500">Map</span>
    </button>
    <h2 class="text-lg font-bold">{{ property.full_address }}</h2>
    <p>{{ property.class_description }}</p>
    <p class="mt-2 text-blue-600">
      Estimated Market Value: ${{ property.estimated_market_value }}
    </p>
    <p class="text-red-600">
      Building Use: {{ property.bldg_use ? property.bldg_use : '---' }}
    </p>
    <p>Building Sqft: {{ property.building_sq_ft }} sqft</p>
    <div class="mt-4 border-t pt-4 text-sm text-gray-600">
      <p>City: {{ property.city }}</p>
      <p>Zip Code: {{ property.zip_code }}</p>
      <p>Neighborhood: {{ property.neighborhood }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    property: Object
  },
  // mounted () {
  //   },
  methods: {
    redirectToMapsPage (id, latitude, longitude) {
      console.log(id, latitude, longitude)
      this.$router.push({ name: 'MapsPage', params: {id, latitude, longitude} })
    }
  }
}
</script>
