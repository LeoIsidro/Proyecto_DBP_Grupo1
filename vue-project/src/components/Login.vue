<script>
import {ref} from 'vue'
export default {
  name: "App",
  data(){
    return {
      name: "",
      password: ""
    }
  },
  methods :{
    AddUser(){
      if(!this.listaSkin.includes(this.username)) {
        this.listaSkin.push(this.username);
      }
      console.log(this.username)
    },
    ShowTable(){
      this.boolShow = true;
    },
    inputUsername(e) {
      this.username = e.target.value;
    },
    inputPassword(e) {
      this.username = e.target.value;
    },
  }
  
}
</script>



<template>
    <header>
        <div >
            <br>
            <label for="floatingInput">Username </label>            
            <input @input="inputUsername" type="text" :value="username">
            <br>
            <br>
            <label for="floatingInput">Password </label>            
            <input @input="inputPassword" type="password" :value="username">
     

        </div>
    </header>
</template>