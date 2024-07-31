export default function ({ store, redirect, route }) {
    const token = store.state.token
    const user = store.state.user
  
    // Permitir acesso sem login às páginas de registro e login
    const publicPages = ['/login', '/register']
    const authRequired = !publicPages.includes(route.path)
  
    if (authRequired && !token) {
      return redirect('/login')
    }
  
    // Verifica o papel do usuário e as rotas permitidas
    const adminRoutes = ['/admin', '/employees', '/services', '/appointments']
    const employeeRoutes = ['/employee', '/services']
    const userRoutes = ['/profile', '/appointments']
  
    if (user && user.role === 'admin' && adminRoutes.includes(route.path)) {
      return
    }
  
    if (user && user.role === 'employee' && employeeRoutes.includes(route.path)) {
      return
    }
  
    if (user && user.role === 'customer' && userRoutes.includes(route.path)) {
      return
    }
  
    if (authRequired) {
      return redirect('/')
    }
  }
  