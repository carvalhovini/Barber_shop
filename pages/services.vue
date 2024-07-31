<template>
    <div class="container">
      <h1>Our Services</h1>
      <ul>
        <li v-for="service in services" :key="service.id">
          <strong>{{ service.name }}</strong> - {{ service.duration }} min - ${{ service.price }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    middleware: 'auth',
    data() {
      return {
        services: []
      }
    },
    async mounted() {
      await this.getServices()
    },
    methods: {
      async getServices() {
        try {
          const response = await this.$axios.get('/services')
          this.services = response.data
        } catch (error) {
          console.error('Failed to fetch services:', error)
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .container {
    margin-top: 50px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    background: white;
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  li strong {
    font-size: 1.1em;
  }
  </style>
  