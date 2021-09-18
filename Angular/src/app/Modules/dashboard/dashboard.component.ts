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
  constructor() { 
    this.wave.fromElement("audio","output",{type:"wave"});
  }

  ngOnInit(): void {
    (document.getElementById('video') as HTMLFormElement).controls = false;
  }

}
