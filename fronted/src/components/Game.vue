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
      
      
            
      video2:  youtube_api[(Math.floor(Math.random() * 100)).toString()]
      
    }
  },
  methods :{
    Boton_video1(){
      console.log(this.video1[3]["views"])
      if(this.video1[3]["views"] > this.video2[3]["views"]){
        this.points = this.points + 1;
      }
      else{
        this.points = 0;
      }
      this.video1 = youtube_api[(Math.floor(Math.random() * 100)).toString()];
      this.video2 = youtube_api[(Math.floor(Math.random() * 100)).toString()];
      
    },
    Boton_video2(){
      console.log(this.video1[3]["views"])
      if(this.video1[3]["views"] < this.video2[3]["views"]){
        this.points = this.points + 1;
      }
      else{
        this.points = 0;
      }
      this.video1 = youtube_api[(Math.floor(Math.random() * 100)).toString()];
      this.video2 = youtube_api[(Math.floor(Math.random() * 100)).toString()];
      
      
    },
    
    
  }
  
}
</script>



<template>

    <header>
        <div  >
          <h1>{{points}} puntos</h1>
          <h1 class="green">Video 1:</h1>
          <img width="480" height="360" :src ="video1[2].banner">
          
                 
           <h2 >Nombre: {{video1[1]["title"]}}</h2> 
           <h2>Viewers: {{video1[3]["views"]}}</h2>
            <br>
            <button  @click="Boton_video1()" class="btn btn-primary">Video 1</button>

          <h1 class="green">Video 2:</h1>
          <img width="480" height="360" :src ="video2 [2].banner">
            <h2 >Nombre: {{video2[1]["title"]}}</h2>
            <h2>Viewers: ???</h2>

          <br>
          <button  @click="Boton_video2()" class="btn btn-primary">Video 2</button>

        </div>
    </header>
</template>