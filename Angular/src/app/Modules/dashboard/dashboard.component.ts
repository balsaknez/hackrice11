import { Component, OnInit } from '@angular/core';
// @ts-ignore
import  Wave  from "@foobar404/wave";
import { transpileModule } from 'typescript';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { User } from 'src/app/models/user.model';
import { NETService } from '../../shared/NET.service';

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
  cur_error = new String();
  sidebars_color = "#DEE1DD";
  font_color = "#28363D";
  colors: string[] = ["#DEE1DD","#C4CDC1","#99AEAD","#6D9197","#658B6F","#2F575D","#28363D"];
  background_color = "#2F575D";

  pages: string[] = ["Home","Finance","Job monitoring","Energetics","Education","Generator"]

  register_screen: boolean = false;

  constructor(public service: NETService, private router: Router) { 
    this.page = 0;  
    this.background_color = this.colors[6];
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
    this.background_color = this.colors[6-i];
  }


  onSubmit(form: NgForm) {
    console.log("submit");
    this.insertRecord(form);
}

resetForm(form?: NgForm) {
  if (form != null)
    form.form.reset();
  this.service.formData = {
    isActive :"1",
    name : "",
    shortName : "",
    nameOnCheck : "",
    companyName : "",
    accNumber : "",
    taxId : "",
    track1099 : "",
    address1 : "",
    address2 : "",
    address3 : "",
    address4 : "",
    addressCity : "",
    addressState : "",
    addressZip : "",
    addressCountry : "",
    email : "",
    fax : "",
    phone : "",
    paymentEmail : "",
    paymentPhone : "",
    description : "",
    contactFirstName : "",
    contactLastName : "",
    accountType : "",
    entity : "",
    vendorId : "",
    accountNumber : "",
    routingNumber : "",
    usersId : "",
    isSavings : "",
    isPersonalAcct : "",
    password: ""

  }
}


insertRecord(form: NgForm) {
  this.cur_error = "";
  this.service.postUser().subscribe(
    res => {
      localStorage.clear();
      console.log(res);
      localStorage.setItem("logged_in", 'y');
      localStorage.setItem("loggedin_name", this.service.formData.name);
      this.resetForm(form);
      this.service.loggedin = true;
      //window.location.reload();
    },
    err => {
      //debugger;
      console.log(err.error);
      this.cur_error = err.error;
    }
  )
}

flip_dialog(){
  this.register_screen = !this.register_screen;
}

}
