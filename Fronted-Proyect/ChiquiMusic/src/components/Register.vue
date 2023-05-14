<template>
  <div>
          <h1>Register</h1>
          <br>
          <label for="floatingInput">Username:  </label>            
          <input @input="onUsernameInput" type="text" :value="username">
          <br>
          <br>
          <label for="floatingInput">Password:  </label>            
          <input @input="onPasswordInput" type="password" :value="password">
          <br>  
          <br>
          <label for="floatingInput">Email:  </label>
          <input @input="onEmailInput" type="email" :value="email">
          <br>
          <br>
          <label for="floatingInput">Age:  </label>
          <input @input="onAgeInput" type="number" :value="age">
          <br>
          <br>
          <button  @click="onRegister" class="btn btn-primary"> Registrarse </button>
      </div>
</template>


<script>
import router from '@/router';
// JavaScript
export default {
  //name: "RegisterView",
  data(){
    return{
      username: "",
      password: "",
      email: "",
      age: "",
      register: false,
      success: false,
    };
  },
  methods: {
    onUsernameInput(e) {
      this.register = false;
      this.username = e.target.value;
    },
    onPasswordInput(e) {
      this.register = false;
      this.password = e.target.value;
    },
    onEmailInput(e) {
      this.register = false;
      this.email = e.target.value;
    },
    onAgeInput(e) {
      this.register = false;
      this.age = e.target.value;
    },
    onRegister() {
      const url = "http://44.209.248.143:8003/register";
      const body = {
        username: this.username,
        email: this.email,
        password: this.password,
        age: this.age,
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
          this.register = true;
          this.success = data.success;
          if (data.success) {
            router.push("/login");
          }
        });
    }
  },
};
</script>



