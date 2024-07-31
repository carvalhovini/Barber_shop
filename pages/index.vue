<template>
    <div>
      <div class="hero">
        <h1>Welcome to Barbershop</h1>
        <p>Your one-stop solution for all your grooming needs.</p>
        <div class="buttons">
          <NuxtLink to="/services" class="btn">Our Services</NuxtLink>
          <NuxtLink to="/appointments" class="btn">Book an Appointment</NuxtLink>
          <NuxtLink to="/login" class="btn">Login</NuxtLink>
          <NuxtLink to="/register" class="btn">Register</NuxtLink>
        </div>
      </div>
      <div class="services-summary">
        <h2>Popular Services</h2>
        <ul>
          <li v-for="service in services" :key="service.id">
            <strong>{{ service.name }}</strong> - {{ service.duration }} min - ${{ service.price }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
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
          this.services = response.data.slice(0, 3) // Mostrar apenas os 3 primeiros serviços
        } catch (error) {
          console.error('Failed to fetch services:', error)
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .hero {
    text-align: center;
    padding: 50px 20px;
    background: url('https://images.unsplash.com/photo-1512100356356-de1b842c61f3') no-repeat center center/cover;
    color: white;
    border-radius: 5px;
  }
  
  .hero h1 {
    margin-bottom: 20px;
    font-size: 2.5em;
  }
  
  .hero p {
    font-size: 1.2em;
    margin-bottom: 30px;
  }
  
  .buttons {
    display: flex;
    justify-content: center;
    gap: 10px;
  }
  
  .buttons a {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s;
  }
  
  .buttons a:hover {
    background-color: #0056b3;
  }
  
  .services-summary {
    margin-top: 50px;
  }
  
  .services-summary h2 {
    text-align: center;
    margin-bottom: 20px;
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
  