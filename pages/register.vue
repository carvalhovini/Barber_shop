<template>
    <div class="container">
      <h1>Register</h1>
      <form @submit.prevent="register">
        <input v-model="username" placeholder="Username" />
        <span v-if="errors.username" class="error">{{ errors.username }}</span>
        <input type="password" v-model="password" placeholder="Password" />
        <span v-if="errors.password" class="error">{{ errors.password }}</span>
        <select v-model="role">
          <option value="customer">Customer</option>
          <option value="employee">Employee</option>
          <option value="admin">Admin</option>
        </select>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        role: 'customer',
        errors: {}
      }
    },
    methods: {
      validate() {
        const errors = {}
        if (!this.username) errors.username = 'Username is required'
        if (!this.password) errors.password = 'Password is required'
        return errors
      },
      async register() {
        this.errors = this.validate()
        if (Object.keys(this.errors).length > 0) return
  
        try {
          await this.$axios.post('/register', {
            username: this.username,
            password: this.password,
            role: this.role
          })
          this.$router.push('/login')
        } catch (error) {
          console.error('Registration failed:', error)
          this.errors = error.response.data
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
  
  input, select, button {
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
  
  .error {
    color: red;
    font-size: 0.9em;
    margin-bottom: 10px;
  }
  </style>
  