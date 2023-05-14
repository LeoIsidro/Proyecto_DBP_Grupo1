<script>
import {ref} from 'vue'
import youtube_api from "/src/database/youtube_api.json";
export default {
  
  data(){
    return {
      name:"",
      points:ref( 0),
      data_api : youtube_api  ,
      video1:  youtube_api[(Math.floor(Math.random() * 100)).toString()],
      video2:  youtube_api[(Math.floor(Math.random() * 100)).toString()] == this.video1 ? youtube_api[(Math.floor(Math.random() * 100)).toString()] : youtube_api[(Math.floor(Math.random() * 100)).toString()],
      ad: true,
      success: false,
    }
  },
  methods :{
    Boton_video1(){
      console.log(this.video1[3]["views"])
      this.ad = true;

      if(this.video1[3]["views"] > this.video2[3]["views"]){
        this.points = this.points + 1;
      }
      else{
        const url = "http://44.209.248.143:8004/score";
        const body = {
          username: sessionStorage.getItem("user"),
          points: this.points,
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
            this.success = true;
          });

        this.points = 0;
        this.ad = false;
      }
      
      
      this.video1 = youtube_api[(Math.floor(Math.random() * 100)).toString()];
      this.video2 = youtube_api[(Math.floor(Math.random() * 100)).toString()];
    },
    Boton_video2(){
      console.log(this.video1[3]["views"])
      this.ad = true;
      if(this.video1[3]["views"] < this.video2[3]["views"]){
        this.points = this.points + 1;
      }
      else{
        const url = "http://44.209.248.143:8004/score";
        const body = {
          username: sessionStorage.getItem("user"),
          points: this.points,
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
            this.success = true;
          });
        this.points = 0;
        this.ad=false;
      }
      this.video1 = youtube_api[(Math.floor(Math.random() * 100)).toString()];
      this.video2 = youtube_api[(Math.floor(Math.random() * 100)).toString()];
    
    }, 
  }
  
}
</script>



<template>

    <header>
        <div >
          <iframe src="" frameborder="0"></iframe>
          <h1 class="green">Video 1:</h1>
          <center><img width="480" height="360" :src ="video1[2].banner"></center>
        
           <h2 >Nombre: {{video1[1]["title"]}}</h2> 
           <h2>Viewers: ???</h2>
           <br>
           <button  @click="Boton_video1()" class="btn btn-primary">Video 1</button>
           <br>
           <br>

          <h1 class="green">Video 2:</h1>
          <center><img width="480" height="360" :src ="video2 [2].banner"></center>
            <h2 >Nombre: {{video2[1]["title"]}}</h2>
            <h2>Viewers: ???</h2>

          <br>
          <button  @click="Boton_video2()" class="btn btn-primary">Video 2</button>
          <br>
          <br>

          <h1>{{points}} puntos</h1>
          <h1 v-if="ad==false">Perdiste</h1>


        </div>
    </header>
</template>