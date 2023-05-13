<template>
  <div>
          <h1>Login</h1>
          <br>
          <br>
          <label>Username: </label>            
          <input type="text" v-bind:value="username" v-on:input="OnUsername">
          <br>
          <br>
          <label>Password: </label>            
          <input type="password" v-bind:value="password" v-on:input="OnPassword" >
          <br>
          <br>
          <button v-on:click="OnLogin" type="button" class="btn btn-primary">Iniciar Sesion </button>
          
          <meta
          v-if="loggin && success"
          id="success"
          http-equiv="refresh"
          content="0;
          url='http://127.0.0.1:5173/game'"
          /> 
          
    </div>
</template>


<script>
// JavaScript
export default {
  data() {
    return {
      username: "",
      password: "",
      success: false,
      loggin: false,
    }; // return
  }, //data
  methods: {
    OnUsername(e) {
      this.loggin = false;
      this.username = e.target.value;
    },
    OnPassword(e) {
      this.loggin = false;
      this.password = e.target.value;
    },
    OnLogin() {
      const url = "http://54.196.100.143:8000/login";
      const body = {
        username: this.username,
        password: this.password,
      };  
      fetch(url, {
        method: "POST",
        body: JSON.stringify(body),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          this.loggin = true;
          this.success = data.success;
          if (data.success) {
            sessionStorage.setItem("user", this.username);
            this.$emit("user-login");
          }
        });
    }
  } // methods
}
</script>