<template>
    <div class="container">
      <h1>Admin Dashboard</h1>
      <form @submit.prevent="addService">
        <input v-model="name" placeholder="Service Name" />
        <input type="number" v-model="duration" placeholder="Duration (minutes)" />
        <input type="number" v-model="price" placeholder="Price" />
        <button type="submit">Add Service</button>
      </form>
      <ul>
        <li v-for="service in services" :key="service.id">
          <strong>{{ service.name }}</strong> - {{ service.duration }} min - ${{ service.price }}
          <button @click="deleteService(service.id)">Delete</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    middleware: 'auth',
    data() {
      return {
        name: '',
        duration: '',
        price: '',
        services: []
      }
    },
    async mounted() {
      await this.getServices()
    },
    methods: {
      async addService() {
        try {
          await this.$axios.post('/services', {
            name: this.name,
            duration: this.duration,
            price: this.price
          })
          await this.getServices()
        } catch (error) {
          console.error('Failed to add service:', error)
        }
      },
      async getServices() {
        try {
          const response = await this.$axios.get('/services')
          this.services = response.data
        } catch (error) {
          console.error('Failed to fetch services:', error)
        }
      },
      async deleteService(id) {
        try {
          await this.$axios.delete(`/services/${id}`)
          await this.getServices()
        } catch (error) {
          console.error('Failed to delete service:', error)
        }
      }
    }
  }
  </script>
  