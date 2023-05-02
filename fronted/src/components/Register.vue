<script>
import {ref} from 'vue'
export default {
  name: "App",
  data(){
    return {
      name:ref(""),
      password: ref(""),
      data_list :ref([["spiderman216","utec1"],["Steve","utec2"],["Herobrine","utec3"]])
      
      
    }
  },
  methods :{
    AddRegister(){
      if(this.data_list)
      {
        this.data_list.push([this.name,this.password])  // Nuevo cambio
      }
      else{
        this.data_list = [[this.name,this.password]]  // Nuevo cambio
      }
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
        <div  >
            <h1>Register</h1>
            <br>
            <label for="floatingInput">Username </label>            
            <input @input="inputUsername" type="text" :value="username">
            <br>
            <br>
            <label for="floatingInput">Password </label>            
            <input @input="inputPassword" type="password" :value="password">
            <br>
            <br>
            <button  @click="AddRegister" class="btn btn-primary">Agregar</button>
            <h1>{{username }} {{password}} {{data_list}}</h1>

        </div>
    </header>
</template>