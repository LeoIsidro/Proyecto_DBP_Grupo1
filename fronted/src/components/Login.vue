<script>
import {ref} from 'vue'
export default {
  name: "App",
  data(){
    return {
      name: "",
      password: "",
      data_list : {},
      logueado: false
    }
  },
  methods :{
    AddLogin(){
      if(!this.listaSkin.includes(this.username)) {
        this.listaSkin.push(this.username);
      }
      console.log(this.username)
    },
    
    inputUsername(e) {
      this.username = e.target.value;
    },
    inputPassword(e) {
      this.password = e.target.value;
    },
  }
  
}
</script>



<template>
    <header>
        <div v-if="!logueado " >
            <h1>Login</h1>
            <br >
            <label for="floatingInput">Username xd </label>            
            <input @input="inputUsername" type="text" :value="username">
            <br>
            <br>
            <label for="floatingInput">Password </label>            
            <input @input="inputPassword" type="password" :value="username">
            <br>
            <br>
            <button  @click="AddLogin" class="btn btn-primary">Agregar</button>
            
     

        </div>
    </header>
</template>