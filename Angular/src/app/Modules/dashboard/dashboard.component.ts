import { Component, OnInit } from '@angular/core';
// @ts-ignore
import  Wave  from "@foobar404/wave";


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  wave = new Wave();
  mainCanvas = document.getElementById("output");

  constructor() { 
  }

  ngOnInit(): void {
    (document.getElementById('video') as HTMLFormElement).controls = false;
  }

  
  canvasClick() {
    this.mainCanvas = document.getElementById("output");
    //(this.mainCanvas as HTMLFormElement).classList.add("show");
    (this.mainCanvas as HTMLFormElement).height = window.innerHeight;
    (this.mainCanvas as HTMLFormElement).width = window.innerWidth

    this.wave.fromElement("audio", "output", {
        type: "dualbars blocks",
        colors: ["#DEE1DD", "#C4CDC1", "#99AEAD"]
    })
    (document.getElementById("audio") as HTMLFormElement).play();

  }

}
