import { Component, OnInit } from '@angular/core';
// @ts-ignore
import  Wave  from "@foobar404/wave";
import { transpileModule } from 'typescript';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  wave = new Wave();
  mainCanvas = document.getElementById("output");
  menu_open: boolean = false;
  page: number = 0;
  sidebars_color = "#DEE1DD";
  font_color = "#28363D";

  pages: string[] = ["Finance","Job monitoring","Energetics","Education","Generator"]
  

  constructor(private router: Router) { 
    this.page = 0;
  }

  ngOnInit(): void {
    //(document.getElementById('video') as HTMLFormElement).controls = false;
  }

  
  canvasClick() {
    this.mainCanvas = document.getElementById("output");
    //(this.mainCanvas as HTMLFormElement).classList.add("show");
    (this.mainCanvas as HTMLFormElement).height = window.innerHeight;
    (this.mainCanvas as HTMLFormElement).width = window.innerWidth;
    (document.getElementById("audio") as HTMLFormElement).play();
    this.wave.fromElement("audio", "output", {
        type: "dualbars blocks",
        colors: ["black", "#DEE1DD", "#658B6F"]
    })

  }

  //menu button
  myFunction() {
    (document.getElementById('menu-btn') as HTMLFormElement).classList.toggle("change");
    this.menu_open = !this.menu_open;
  }

  set_page_to(i: number){
    this.page = i;
    if (i == 4) this.router.navigate(['bot_creator']);
  }

}
