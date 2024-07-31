<template>
    <div>
      <div class="navbar">
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/login">Login</NuxtLink>
        <NuxtLink to="/register">Register</NuxtLink>
        <NuxtLink to="/services">Services</NuxtLink>
        <NuxtLink to="/appointments">Appointments</NuxtLink>
        <NuxtLink to="/admin">Admin Dashboard</NuxtLink>
        <NuxtLink to="/employee">Employee Dashboard</NuxtLink>
        <NuxtLink to="/profile">Profile</NuxtLink>
      </div>
      <Nuxt />
    </div>
  </template>
  
  <style>
  .navbar {
    display: flex;
    justify-content: center;
    background-color: #333;
    padding: 10px;
  }
  
  .navbar a {
    color: white;
    padding: 14px 20px;
    text-decoration: none;
    text-align: center;
  }
  
  .navbar a:hover {
    background-color: #ddd;
    color: black;
  }
  </style>
  