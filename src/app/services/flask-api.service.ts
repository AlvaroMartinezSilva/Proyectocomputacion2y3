import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class FlaskApiService {

  constructor(private http:HttpClient) { }

  getAll():Observable<any>{
    return this.http.get<any>('http://127.0.0.1:5000/saludo');
  }

  analizarSentimiento(textoSinAnalizar: string):Observable<any>{

    var cuerpo = {'texto': textoSinAnalizar}

    var respuestaAPI = this.http.post<any>('http://127.0.0.1:5000/sentimiento', cuerpo);

    return respuestaAPI;
  }

}
