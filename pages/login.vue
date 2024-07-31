<template>
    <div class="container">
      <h1>Login</h1>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="Username" />
        <span v-if="errors.username" class="error">{{ errors.username }}</span>
        <input type="password" v-model="password" placeholder="Password" />
        <span v-if="errors.password" class="error">{{ errors.password }}</span>
        <button type="submit">Login</button>
        <span v-if="errors.login" class="error">{{ errors.login }}</span>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
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
      async login() {
        this.errors = this.validate()
        if (Object.keys(this.errors).length > 0) return
  
        try {
          await this.$store.dispatch('login', {
            username: this.username,
            password: this.password
          })
          this.$router.push('/')
        } catch (error) {
          console.error('Login failed:', error)
          this.errors.login = 'Invalid credentials'
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
  
  input, button {
    display: block;
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1em;
  }
  
  button {
    background-color: #007bff;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  .error {
    color: red;
    font-size: 0.9em;
    margin-bottom: 10px;
  }
  </style>
  