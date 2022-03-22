import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DockerService {

  constructor(private _http: HttpClient) { }

  add(id: string, name: string){
    let container = {
      'id': id,
      'name': name
    }
    return this._http.post<any>(`${environment.PATH}/add`, container)
  }

  getAll(){
    return this._http.get<any>(`${environment.PATH}/getAll`);
  }

  delete(id: string){
    return this._http.delete<any>(`${environment.PATH}/deleteById/${id}`)
  }

  start(id: string){
    let container = {'id': id}
    return this._http.post<any>(`${environment.PATH}/start`, container);
  }

  stop(id: string){
    let container = {'id': id}
    return this._http.post<any>(`${environment.PATH}/stop`, container);
  }

  pause(id: string){
    let container = {'id': id}
    return this._http.post<any>(`${environment.PATH}/pause`, container);
  }

  unpause(id: string){
    let container = {'id': id}
    return this._http.post<any>(`${environment.PATH}/unpause`, container);
  }
}
