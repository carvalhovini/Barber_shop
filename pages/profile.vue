<template>
    <div class="container">
      <h1>Your Appointments</h1>
      <ul>
        <li v-for="appointment in appointments" :key="appointment.id">
          {{ appointment.service.name }} - {{ appointment.appointment_time }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    middleware: 'auth',
    data() {
      return {
        appointments: []
      }
    },
    async mounted() {
      await this.getAppointments()
    },
    methods: {
      async getAppointments() {
        try {
          const response = await this.$axios.get('/appointments')
          this.appointments = response.data.filter(a => a.user.id === this.$store.state.user.id)
        } catch (error) {
          console.error('Failed to fetch appointments:', error)
        }
      }
    }
  }
  </script>
  