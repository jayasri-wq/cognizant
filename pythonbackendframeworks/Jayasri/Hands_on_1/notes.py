# Task 1 - Django Request Response Cycle

# 1. Request → Response Flow
# Browser → URL Router → View → Model (DB) → View → Response

# 2. Middleware
# Request → Middleware → View → Middleware → Response
# SecurityMiddleware - security features
# SessionMiddleware - manages user sessions

# 3. WSGI vs ASGI
# WSGI - synchronous (default Django)
# ASGI - asynchronous (used for real-time apps like chat)

# 4. MVC vs MVT
# MVC: Model View Controller
# Django MVT:
# Model = Model
# View = Controller
# Template = View