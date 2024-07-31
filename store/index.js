export const state = () => ({
    token: '',
    user: null
  })
  
  export const mutations = {
    setToken(state, token) {
      state.token = token
    },
    setUser(state, user) {
      state.user = user
    },
    clearAuth(state) {
      state.token = ''
      state.user = null
    }
  }
  
  export const actions = {
    async nuxtServerInit({ commit }, { req }) {
      if (req.headers.cookie) {
        const token = req.headers.cookie.split('=')[1]
        commit('setToken', token)
      }
    },
    async login({ commit, dispatch }, credentials) {
      try {
        const response = await this.$axios.post('/login', credentials)
        const token = response.data.access_token
        commit('setToken', token)
        this.$axios.setToken(token, 'Bearer')
        await dispatch('fetchUser')
      } catch (error) {
        console.error('Login error:', error)
        throw error
      }
    },
    async fetchUser({ commit, state }) {
      try {
        const response = await this.$axios.get('/profile', {
          headers: {
            Authorization: `Bearer ${state.token}`
          }
        })
        commit('setUser', response.data.user)
      } catch (error) {
        console.error('Error fetching user:', error)
      }
    }
  }
  