export default {
  // Global page headers
  head: {
    title: 'barbershop-frontend',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Barbershop Management System' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS
  css: [
    '@/assets/css/main.css'
  ],

  // Plugins to run before rendering page
  plugins: [
  ],

  // Auto import components
  components: true,

  // Modules for dev and build (recommended)
  buildModules: [
  ],

  // Modules
  modules: [
    '@nuxtjs/axios',
  ],

  // Axios module configuration
  axios: {
    baseURL: 'http://127.0.0.1:5000',
  },

  // Router configuration
  router: {
    middleware: ['auth']
  },

  // Build Configuration
  build: {
  }
}
