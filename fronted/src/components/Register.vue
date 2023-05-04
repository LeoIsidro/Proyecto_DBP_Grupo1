<template>
  <header>
      <div >
          <h1>Register</h1>
          <br>
          <label for="floatingInput">Username:  </label>            
          <input @input="inputUsername" type="text" :value="username">
          <br>
          <br>
          <label for="floatingInput">Password:  </label>            
          <input @input="inputPassword" type="password" :value="password">
          <br>  
          <br>
          <label for="floatingInput">Email:  </label>
          <input @input="inputEmail" type="email" :value="email">
          <br>
          <br>
          <label for="floatingInput">Age:  </label>
          <input @input="inputAge" type="number" :value="age">
          <br>
          <br>
          <button  @click="onRegister" class="btn btn-primary">Registrarse </button>
          <meta
            v-if="register && success"
            id="success"
            http-equiv="refresh"
            content="0;
              url='http://127.0.0.1:5173/login'"/>

      </div>
  </header>
</template>


<script>
export default {
  name: "App",

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



