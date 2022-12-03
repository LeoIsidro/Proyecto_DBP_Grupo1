<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template> 
  
  <nav>
    <img class="logo" src="@/assets/UTEC_LOGO.png" width="125" height="-200" />
    
    <img class="logo" src="@/assets/lobby_1.png"/>
    <img class="logo" src="@/assets/lobby_2.png"/>
    <br>
    <br>
    <br>
    <div>
      <RouterLink to="/lobby">Lobby</RouterLink>
      <RouterLink to="/login">Login</RouterLink>
      <RouterLink to="/about">About</RouterLink>

    </div>
    

    <img class="logo" src="@/assets/lobby_2.png"/>
    
  </nav>

  

   
  
  <img/>
      

    


  <RouterView />

</template>

<style scoped>

.fondo{
    margin: 0;
    padding: 0;
    background: url("src/assets/lobby_2.png");   
    background-size: cover;
    background-position: center;
    font-family: sans-serif;
}




header {
  line-height: 1.5;
  max-height: 100vh;
}



.logo {
  display: block;
  margin: 1 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}


</style>
