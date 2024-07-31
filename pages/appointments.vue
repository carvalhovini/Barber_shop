<template>
    <div class="container">
      <h1>Book an Appointment</h1>
      <form @submit.prevent="bookAppointment">
        <select v-model="serviceId">
          <option v-for="service in services" :value="service.id" :key="service.id">
            {{ service.name }}
          </option>
        </select>
        <input type="datetime-local" v-model="appointmentTime" />
        <button type="submit">Book</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    middleware: 'auth',
    data() {
      return {
        services: [],
        serviceId: '',
        appointmentTime: ''
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
      },
      async bookAppointment() {
        try {
          await this.$axios.post('/appointments', {
            service_id: this.serviceId,
            appointment_time: this.appointmentTime
          })
          alert('Appointment booked successfully!')
        } catch (error) {
          console.error('Failed to book appointment:', error)
        }
      }
    }
  }
  </script>
  
  <style scoped>
  form {
    max-width: 600px;
    margin: 50px auto;
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  select, input, button {
    display: block;
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1em;
  }
  
  button {
    background-color: #28a745;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #218838;
  }
  </style>
  