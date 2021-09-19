import { User } from '../models/user.model';
import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { HttpErrorResponse } from "@angular/common/http";
import { catchError } from 'rxjs/operators'; 
import { throwError, concat, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NETService {
  formData: User;
  loggedin: boolean = false;
  readonly rootURL = 'http://127.0.0.1:5000';
  //list : User[];

  constructor(private http: HttpClient) {
    this.isTesting = false;
    if(localStorage.getItem("logged_in") == "y"){
      this.loggedin = true;
    }
    this.formData = new User();
   }

  isTesting: boolean;

  handleError(error: HttpErrorResponse) {
    return throwError(error);
  }
  postUser() {
      return this.http.post(this.rootURL + '/register/', this.formData).pipe(catchError(this.handleError));
    //return this.http.post(this.rootURL + '/register/', this.formData).pipe(catchError(this.handleError));
  }
  putUser() {
    return this.http.put(this.rootURL + '/userdata/', this.formData).pipe(catchError(this.handleError));
  }
  deleteUser(vendorId: string) {
    return this.http.delete(this.rootURL + '/userdata/'+ vendorId).pipe(catchError(this.handleError));
  }
  loginUser(name: string){
    return this.http.get(this.rootURL + '/userdata/' + name).pipe(catchError(this.handleError));
  }
  GetAllUsers(){
    return this.http.get(this.rootURL + '/userdata/').pipe(catchError(this.handleError));
  }

  /*
  refreshListUser(){
    this.http.get(this.rootURL + '/userdata')
    .toPromise()
    .then(res => this.list = res as User[]);
  }
*/


}
